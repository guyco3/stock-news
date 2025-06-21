import requests
from datetime import datetime, timedelta, timezone
from typing import List
from models.article import Article
from config.settings import Settings
from clients.base_client import NewsClient

class NewsDataClient(NewsClient):
    def fetch_articles(self) -> List[Article]:
        try:
     
            params = {
                "apikey": Settings.NEWSDATA_API_KEY,
                "q": Settings.QUERY,
                "language": "en"
            }
            
            # Use archive endpoint (supports date ranges)
            response = requests.get("https://newsdata.io/api/1/latest", params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Filter articles to last 12 hours
            cutoff_time = datetime.now(timezone.utc) - timedelta(hours=Settings.TIME_DELTA_HOURS)
            articles = []
            
            for item in data.get("results", []):
                if not item.get("pubDate"):
                    continue
                    
                pub_date = datetime.strptime(item["pubDate"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
                
                # Only include articles from last 12 hours
                if pub_date > cutoff_time:
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
            if hasattr(e, 'response') and e.response:
                print(f"Error details: {e.response.text}")
            return []
