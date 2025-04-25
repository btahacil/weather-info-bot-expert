# config/settings.py

import os
from pathlib import Path
from dotenv import load_dotenv

# Proje kök dizinini bul ve .env dosyasını yükle
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# .env içinden okunacak
API_KEY      = os.getenv("API_KEY")
DEFAULT_CITY = os.getenv("DEFAULT_CITY", "Istanbul")
UNITS        = os.getenv("UNITS", "metric")
LANG         = "en"  # Hava açıklamaları için dil

# Sabit URL
BASE_URL = "https://api.openweathermap.org/data/2.5/"

# Dosya yolları
CSV_FILE_PATH = "data/weather_data.csv"
LOG_FILE_PATH = "logs/error.log"

# Planlanmış görevler için çekme aralığı (dakika)
FETCH_INTERVAL_MINUTES = 60


