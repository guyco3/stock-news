from typing import Dict, List
from models.article import Article
from clients import NewsAPIClient, NewsDataClient, TheNewsAPIClient
from processors import Normalizer, Deduplicator, Categorizer

class QuantumNewsService:
    def __init__(self, clients=None):
        self.clients = clients or [
            NewsAPIClient(),
            NewsDataClient(),
            TheNewsAPIClient()
        ]
    
    def fetch_articles(self) -> List[Article]:
        articles = []
        for client in self.clients:
            articles.extend(client.fetch_articles())
        return articles
    
    def get_categorized_news(self) -> Dict[str, List[Article]]:
        raw_articles = self.fetch_articles()
        # normalized = Normalizer.normalize(raw_articles)
        # deduped = Deduplicator.deduplicate(normalized)
        # return Categorizer.categorize(deduped)
        return raw_articles
