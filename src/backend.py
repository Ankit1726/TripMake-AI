import os,operator,uuid,psycopg

from typing import TypedDict,Annotated
from psycopg.rows import dict_row

from langgraph.graph import StateGraph,START,END 
from langgraph.checkpoint.postgres import PostgresSaver
from langchain_groq import ChatGroq
from langchain_core.messages import (
    AnyMessage,
    HumanMessage,
    AIMessage,
    SystemMessage
)

from src.tools.tavily_tool import tavily_search
from src.tools.flight_tool import search_flights
from src.database.db import get_database_url 

from dotenv import load_dotenv
load_dotenv()

GROQ = os.getenv("GROQ_API_KEY")
if not GROQ:
    raise ValueError(
        "GROQ API KEY is missing ⚠️"
    )

## LLM 
llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key = GROQ
)

## Define State 
class TravelState(TypedDict):
    messages:Annotated[list[AnyMessage],operator.add]
    user_query:str
    flight_results:str
    hotel_results: str
    itinerary:str 
    llm_calls:int 

## Flight Agent 
def flight_agent(state:TravelState):
    query = state["user_query"]
    flight_data = search_flights(query)
    return{
        "flight_results":flight_data,
        "messages":[
            AIMessage(content="flight results fetched..✅")
        ],
        "llm_calls":state.get("llm_calls",0)+1    
    }

## Hotel Agent 
def hotel_agent(state:TravelState):
    query = f"best hotels for {state['user_query']}"
    hotel_results = tavily_search(query)

    return{
        "hotel_results":hotel_results,
        "messages":[
            AIMessage(content="hotel information fetched..✅")
        ],
        "llm_calls":state.get("llm_calls",0)+1
    }

## Itinerary Agent 
def itinerary_agent(state:TravelState):
        prompt = f"""
            Create a complete travel itinerary.

            User Query:
            {state['user_query']}

            Flight Results:
            {state['flight_results']}

            Hotel Results:
            {state['hotel_results']}

            Make the itinerary practical, budget-aware, and easy to follow.
        """
        response = llm.invoke([
            SystemMessage(content="you are an expert travel planner."),
            HumanMessage(content=prompt)
        ])
        return {
            "itinerary": response.content,
            "messages": [response],
            "llm_calls": state.get("llm_calls", 0) + 1
        }

## Final Agent Response
def final_agent(state:TravelState):
      final_prompt = f"""
            Generate the final travel response for the user.

            User Request:
            {state['user_query']}

            Flights:
            {state['flight_results']}

            Hotels:
            {state['hotel_results']}

            Itinerary:
            {state['itinerary']}

            Format the final answer beautifully using these sections:

            1. Trip Summary
            2. Flight Information
            3. Hotel Suggestions
            4. Day-by-Day Itinerary
            5. Estimated Budget
            6. Final Recommendations

            Important:
            - Be clear and practical.
            - Mention that live flight API may not provide ticket prices if pricing is unavailable.
            - Keep the response useful for real travel planning.
        """
      response = llm.invoke([
           SystemMessage(content='you are professional AI Travel Booking Agent'),
           HumanMessage(content=final_prompt)
      ])
      return {
           "messages":[response],
           "llm_calls":state.get("llm_calls",0)+1
    }

## Build Graph 
graph = StateGraph(TravelState)

graph.add_node("flight_agent",flight_agent)
graph.add_node("hotel_agent",hotel_agent)
graph.add_node("itinerary_agent",itinerary_agent)
graph.add_node("final_agent",final_agent)

graph.add_edge(START,"flight_agent")
graph.add_edge("flight_agent","hotel_agent")
graph.add_edge("hotel_agent","itinerary_agent")
graph.add_edge("itinerary_agent","final_agent")
graph.add_edge("final_agent",END)

## Database Checkpointer 
DB_URL = get_database_url()

_conn = psycopg.connect(
    DB_URL,
    autocommit=True,
    row_factory=dict_row
)

checkpointer = PostgresSaver(_conn)
checkpointer.setup()
travel_graph = graph.compile(checkpointer=checkpointer)

# FastAPI Function
def run_travel_agent(user_input: str, thread_id: str | None = None):

    # Create new thread if this is a new chat
    if thread_id is None:
        thread_id = f"user_{uuid.uuid4().hex}"
        prompt = f"""
                Generate a short conversation title (maximum 5 words).

                User:
                {user_input}

                Respond with ONLY the title.
            """
        try:
            thread_title = llm.invoke(prompt).content.strip()
        except Exception:
            thread_title = " ".join(user_input.split()[:5])
    else:
        # Existing chat
        thread_title = None

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }
    result = travel_graph.invoke(
        {
            "messages": [HumanMessage(content=user_input)],
            "user_query": user_input,
            "flight_results": "",
            "hotel_results": "",
            "itinerary": "",
            "llm_calls": 0,
        },
        config=config,
    )

    final_answer = result["messages"][-1].content
    return {
        "thread_id": thread_id,       
        "thread_title": thread_title, 
        "answer": final_answer,
        "flight_results": result.get("flight_results", ""),
        "hotel_results": result.get("hotel_results", ""),
        "itinerary": result.get("itinerary", ""),
        "llm_calls": result.get("llm_calls", 0),
    }