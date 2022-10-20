import os
from pydantic import BaseSettings
from dotenv import load_dotenv

# load_dotenv()

# Environment Variables

class Settings(BaseSettings):
    # try:
    DB_USERNAME: str
    DB_PASSWORD: str
    QUERY_LIMIT: int
    USER_LIMIT: int
    
    class Config:
        env_file = ".env"


settings = Settings()
