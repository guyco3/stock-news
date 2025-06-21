import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")
    THE_NEWS_API_KEY = os.getenv("THE_NEWS_API_KEY")
    
    QUERY = "acquisition"
    TIME_DELTA_HOURS = 12
