from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from models.article import Article

class NewsClient(ABC):
    @abstractmethod
    def fetch_articles(self) -> List[Article]:
        pass
