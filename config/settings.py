import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")
    THE_NEWS_API_KEY = os.getenv("THE_NEWS_API_KEY")
    
    QUERY = (
        # Executive mentions (expandable list)
        '("Jensen Huang" OR "Satya Nadella" OR "Peter Chapman" OR "Chad Rigetti" '
        'OR "Jeremy O\'Brien" OR "Jay Gambetta" OR "Krysta Svore") AND quantum '
        
        # Quantum companies and breakthroughs
        'OR (Rigetti OR IonQ OR IBM OR Google OR Microsoft OR Honeywell OR Quantinuum OR D-Wave) '
        'AND (breakthrough OR milestone OR achievement OR "new record" OR advance) '
        
        # Research advancements
        'OR ("quantum error correction" OR "logical qubits" OR "fault-tolerant" '
        'OR "quantum supremacy" OR "quantum advantage" OR "topological qubits")'
        )

    TIME_DELTA_HOURS = 12
