import requests
from datetime import datetime
from typing import List
from models.article import Article
from config.settings import Settings
from clients.base_client import NewsClient

class NewsDataClient(NewsClient):
    def fetch_articles(self) -> List[Article]:
        try:
            # Prepare API request
            params = {
                "apikey": Settings.NEWSDATA_API_KEY,
                "q": Settings.QUERY,
                "timeframe": "24",  # Last 24 hours
                "language": "en",
                "prioritydomain": "top"  # Focus on high-priority sources
            }
            
            # Execute request
            response = requests.get("https://newsdata.io/api/1/news", params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Parse response
            articles = []
            for item in data.get("results", []):
                # Handle nullable pubDate
                pub_date = datetime.utcnow()
                if item.get("pubDate"):
                    pub_date = datetime.strptime(item["pubDate"], "%Y-%m-%d %H:%M:%S")
                
                articles.append(Article(
                    title=item["title"],
                    source=item.get("source_id", "Unknown"),
                    published=pub_date,
                    url=item["link"],
                    content=item.get("content", "") or item.get("description", "")
                ))
            return articles
            
        except Exception as e:
            print(f"NewsData.io error: {str(e)}")
            return []
