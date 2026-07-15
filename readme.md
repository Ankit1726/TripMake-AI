<div align="center">

# ✈️ TripMaKe AI

### 🤖 Multi-Agent AI Travel Planner powered by LangGraph

Plan complete trips using AI with **Flights ✈️ • Hotels 🏨 • Itineraries 🗺️ • Multi-Agent Workflows**

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&weight=600&size=24&duration=3500&pause=1000&color=00C2FF&center=true&vCenter=true&width=700&lines=AI+Travel+Planner;LangGraph+Multi-Agent+Workflow;FastAPI+%7C+Groq+LLM+%7C+PostgreSQL;Built+by+Ankit+Gupta" />
</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi"/>
<img src="https://img.shields.io/badge/LangGraph-Multi--Agent-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql"/>
<img src="https://img.shields.io/badge/Groq-LLM-purple?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Open_Source-❤-red?style=for-the-badge"/>
</p>

<p align="center">
<a href="Preview">
<img src="">
</a>
</p>
</div>

---

### 🌍 About TripMaKe AI

TripMaKe AI is an **AI-powered Multi-Agent Travel Planner** that transforms natural language travel requests into complete travel plans.

Instead of switching between multiple websites for flights, hotels, and itineraries, users simply describe their trip in plain English, and the AI coordinates multiple specialized agents to generate a personalized travel experience.

The project demonstrates how **LangGraph** can orchestrate multiple AI agents working together while maintaining conversation state with PostgreSQL.

---

### ✨ Live Demo

### 🌐 Web App
 - 👉 **YOUR_LIVE_DEMO**

---

### 📸 Project Preview

## Home Page

<p align="center">
<img src="preview.png" width="900">
</p>

---

## Multi-Agent Workflow

<p align="center">
<img src="workflow.png" width="900">
</p>

---

### 🎯 Features
- ✈️ Flight research using AviationStack
- 🏨 Hotel suggestions using Tavily search
- 🧠 Multi-agent orchestration with LangGraph
- 📝 Structured travel itinerary generation
- 🌐 FastAPI backend with a simple web interface
- 💾 Conversation state persistence using PostgreSQL
- ⚡ LLM-powered responses with Groq


---

### ⚡ Example Prompt

```
Plan a 5-day trip to Bali for two people.

Budget: $1800

Include:

• Flights
• Hotels
• Daily itinerary
• Tourist attractions
• Local food recommendations
```

---

### 🤖 Multi-Agent Architecture

```
                User Request
                      │
                      ▼
            LangGraph Workflow
                      │
      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼
 Flight Agent    Hotel Agent    Itinerary Agent
      │               │               │
      └───────────────┼───────────────┘
                      ▼
              Response Formatter
                      │
                      ▼
            Complete Travel Plan
```

---

# 🛠 Tech Stack

| Technology    | Purpose              |
| ------------- | -------------------- |
| Python        | Backend              |
| FastAPI       | REST API             |
| LangGraph     | Multi-Agent Workflow |
| LangChain     | LLM Framework        |
| Groq          | Language Model       |
| PostgreSQL    | Conversation Memory  |
| Tavily        | Web Search           |
| AviationStack | Flight Search        |
| HTML/CSS/JS   | Frontend             |
| Jinja2        | Templates            |

---

### 📂 Project Structure

```text
TripMaKe-AI
│
├── src/
|   ├── backend.py
|   ├──  database/
|         ├── db.py
|   ├── tools/
|       ├── flight.py
|       ├── hotel.py
|       └── search.p
├── static/
│   ├── css
│   ├── js
│   └── images
│
├── templates/
│   └── index.html
├── requirements.txt
├── .env
├──  app.py
└── README.md
```

---

### 📡 API Endpoint

## Health Check

```
GET /health
```

### Generate Travel Plan

```
POST /api/travel
```

Example

```json
{
  "message": "Plan a 4-day trip to Tokyo under $1200"
}
```
---

### 🌟 Future Improvements

- Flight Booking Integration
- Google Maps Integration
- Expense Tracking
- AI Budget Optimizer
- Weather Forecast
- Visa Information
- Email Trip Planner
- Voice Assistant

---

### 🤝 Contributing

- Contributions are always welcome..!
  
- If you'd like to improve TripMaKe AI:
```
Fork Repository

Create Feature Branch

Commit Changes

Push Changes

Open Pull Request
```

---

### 👨‍💻 Developer

<div align="center">

## Ankit Gupta ✈️

### AI Engineer • AI Backend Developer • GenAI & Agentic Developer

Building AI-powered applications using

**LangGraph • LangChain • FastAPI • PyTorch • Machine Learning • LLMs**
</div>

---

### ⭐ Support
- If you found this project helpful,
- please consider giving it a ⭐ on GitHub.
- It motivates me to build more AI-powered open-source projects.

---

<div align="center">

## ✈️ TripMaKe AI

### Plan Smarter. Travel Better. Powered by AI.

Made with ❤️ by **Ankit Gupta**

</div>
