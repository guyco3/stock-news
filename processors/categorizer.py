# categorizer.py
from collections import defaultdict
from models.article import Article
from typing import Dict, List

class Categorizer:
    @staticmethod
    def categorize(articles: List[Article]) -> Dict[str, List[Article]]:
        categories = defaultdict(list)
        # for article in articles:
            # ... categorization logic ...
        return categories
