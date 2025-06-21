from services.news_service import QuantumNewsService
from clients import NewsAPIClient, NewsDataClient, TheNewsAPIClient

def main():
    
    clients = [NewsDataClient(), NewsDataClient(), TheNewsAPIClient()]
    service = QuantumNewsService([clients[0]])
    news = service.get_categorized_news()    

    # Output results
    for category, articles in news.items():
        print(f"\n{category.upper()} ({len(articles)} articles)")
        for article in articles[:5]:
            print(f"- {article.title} ({article.source})")

if __name__ == "__main__":
    main()
