import requests
from datetime import datetime, timedelta
from typing import List
from models.article import Article
from config.settings import Settings
from clients.base_client import NewsClient

class TheNewsAPIClient(NewsClient):
    def fetch_articles(self) -> List[Article]:
        try:
            # Calculate date range
            published_after = datetime.utcnow() - timedelta(days=Settings.TIME_DELTA_DAYS)
            
            # Prepare API request
            params = {
                "api_token": Settings.THE_NEWS_API_KEY,
                "search": Settings.QUERY.replace(" OR ", " | "),
                "published_after": published_after.strftime("%Y-%m-%dT%H:%M:%S"),
                "language": "en",
                "limit": 10  # Free tier limit
            }
            
            # Execute request
            response = requests.get("https://api.thenewsapi.com/v1/news/all", params=params, timeout=10)
            response.raise_for_status()
            
            # Parse response
            articles = []
            for item in response.json().get("data", []):
                # Handle nullable published_at
                pub_date = datetime.utcnow()
                if item.get("published_at"):
                    pub_date = datetime.fromisoformat(item["published_at"].replace("Z", "+00:00"))
                
                articles.append(Article(
                    title=item["title"],
                    source=item.get("source", "Unknown"),
                    published=pub_date,
                    url=item["url"],
                    content=item.get("snippet", "") or ""
                ))
            return articles
            
        except Exception as e:
            print(f"The News API error: {str(e)}")
            return []
