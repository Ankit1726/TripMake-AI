import os 
from dotenv import load_dotenv
load_dotenv()

## Database Setup 
def get_database_url():
    db_url = os.getenv("DATABASE_URL")

    if not db_url:
        raise ValueError(
            "DB url is missing..! please add your database url ⚠️"
        )
    if "sslmode" not in db_url:
        seprator = "&" if "?" in db_url else "?"
        db_url = f"{db_url}{seprator}sslmode=require"
    return db_url