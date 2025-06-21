# stock-news
get news easily!
# Quantum News Aggregator 🚀

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A modular Python tool that fetches and categorizes the latest quantum computing news, CEO insights, and stock updates from multiple APIs.

## Features ✨

- **Multi-API Integration**: Fetches from NewsAPI, NewsData.io, and The News API
- **Smart Categorization**: 
  - CEO insights (e.g., Jensen Huang)
  - Quantum stocks (Rigetti, IonQ, etc.)
  - Technical developments
- **Deduplication**: Prevents duplicate articles
- **Daily Updates**: Optimized for scheduled execution
- **Modular Architecture**: Easy to extend or modify

## Installation ⚙️

```bash
git clone https://github.com/yourusername/quantum-news-aggregator.git
cd quantum-news-aggregator
```



## Configuration 🔧

1. Create `.env` file:

```bash
NEWS_API_KEY="your_newsapi_key"
NEWSDATA_API_KEY="your_newsdata_key"
THE_NEWS_API_KEY="your_thenewsapi_key"
```

2. Customize query in `config/settings.py`:

```bash
QUERY = "quantum computing OR Jensen Huang OR Rigetti OR IonQ" # Modify as needed
TIME_DELTA_DAYS = 1 # Articles from last 24 hours
```


## Usage 🚀

```bash
python3 main.py
```


**Sample Output:**

```bash
CEO_INSIGHTS (3 articles)
NVIDIA CEO Predicts Quantum Leap by 2030 (TechCrunch)
Jensen Huang: Quantum Will Revolutionize AI (Wired)
QUANTUM_STOCKS (5 articles)
IonQ Stock Surges 12% on New Partnership (Bloomberg)
Rigetti Computing Secures $50M DoD Contract (Reuters)
QUANTUM_TECH (7 articles)
MIT Researchers Achieve Quantum Error Correction Breakthrough (Nature)
Quantum Internet Prototype Succeeds in 100km Test (IEEE Spectrum)
```


## Customization 🛠️
**Add new API:**
1. Create `newapi_client.py` in `clients/`
2. Implement `NewsClient` interface
3. Add to service initialization, in `services/news_service.py`:
```bash
self.clients = [..., NewAPIClient()]
```


## Troubleshooting 🐞
| Issue | Solution |
|-------|----------|
| No articles returned | Verify API keys in `.env` |
| Old articles appearing | Check `TIME_DELTA_DAYS` in settings |
| Rate limit errors | Monitor API usage in provider dashboards |

## Dependencies 📦
- Python 3.8+
- `requests` (API communication)
- `python-dotenv` (environment variables)

## Contributing 🤝
Contributions welcome! Please follow:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open pull request

## License 📄
MIT License - See [LICENSE](LICENSE) for details

---
> **Contact**: your.email@example.com  
> **Project Board**: [GitHub Projects](https://github.com/yourusername/quantum-news-aggregator/projects)
