import csv
import os
from datetime import datetime
from services.news_service import QuantumNewsService
from clients.newsapi_client import NewsAPIClient
from clients.thenewsapi_client import TheNewsAPIClient
from clients.newsdata_client import NewsDataClient
from dotenv import load_dotenv
load_dotenv()

def main():
    # Initialize clients
    clients = [NewsAPIClient(), NewsDataClient(), TheNewsAPIClient()]
    service = QuantumNewsService([clients[1]])
    news = service.get_categorized_news()

    news = sorted(news, key=lambda x: x.published, reverse=True)

    if not news or len(news) == 0:
        return

    print(news)

    # Create folder if it doesn't exist
    folder_name = 'data'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Generate timestamped filename
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"news_{current_time}.csv"
    file_path = os.path.join(folder_name, filename)

    # Write results to CSV file
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['Title', 'Published', 'URL', 'Source'])

        # Write articles
        for article in news:
            writer.writerow([
                article.title,
                article.published.strftime('%Y-%m-%d %H:%M:%S'),
                article.url,
                article.source
            ])

    print(f'Results written to {file_path}')

if __name__ == '__main__':
    main()
