from dataclasses import dataclass
from datetime import datetime

@dataclass
class Article:
    title: str
    source: str
    published: datetime
    url: str
    content: str
