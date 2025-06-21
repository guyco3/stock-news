
# deduplicator.py
from models.article import Article
from typing import List, Set

class Deduplicator:
    @staticmethod
    def deduplicate(articles: List[Article]) -> List[Article]:
        seen_titles: Set[str] = set()
        return [article for article in articles 
                if article.title not in seen_titles 
                and not seen_titles.add(article.title)]
