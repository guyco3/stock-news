import requests
from datetime import datetime, timedelta
from typing import List
from models.article import Article
from config.settings import Settings
from clients.base_client import NewsClient
from datetime import datetime, timedelta, timezone


class NewsAPIClient(NewsClient):
    def fetch_articles(self) -> List[Article]:
        try:
            # Calculate date range
            published_after = (datetime.now(timezone.utc) - timedelta(hours=Settings.TIME_DELTA_HOURS)).strftime("%Y-%m-%d")

            # Prepare API request
            params = {
                "q": Settings.QUERY,
                "from": published_after,
                "sortBy": "publishedAt",
                "language": "en",
                "apiKey": Settings.NEWS_API_KEY,
                "pageSize": 20  # Max for free tier
            }
            
            # Execute request
            response = requests.get("https://newsapi.org/v2/everything", params=params, timeout=10)
            response.raise_for_status()
            
            print(response.content)
            # Parse response
            articles = []
            for item in response.json().get("articles", []):
                articles.append(Article(
                    title=item.get("title", ""),
                    source=item.get("source", {}).get("name", "Unknown"),
                    published=datetime.fromisoformat(item["publishedAt"].replace("Z", "+00:00")),
                    url=item["url"],
                    content=item.get("content", "") or item.get("description", "")
                ))
            return articles
            
        except Exception as e:
            print(f"NewsAPI error: {str(e)}")
            return []
