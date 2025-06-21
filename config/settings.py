import os

class Config:
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")
    THE_NEWS_API_KEY = os.getenv("THE_NEWS_API_KEY")
    
    # Common query parameters
    QUERY = "quantum computing OR Jensen Huang OR Rigetti OR IonQ"
    TIME_DELTA_DAYS = 1  # Fetch news from the last day
