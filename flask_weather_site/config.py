# config.py
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OWM_API_KEY: str = os.getenv("OWM_API_KEY", "")
    DEFAULT_CITY: str = os.getenv("DEFAULT_CITY", "Tokyo")
    OWM_BASE_URL: str = "https://api.openweathermap.org/data/2.5"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret")
