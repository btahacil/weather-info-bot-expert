# utils/api_handler.py

import csv
from datetime import datetime

import requests
from config.settings import API_KEY, BASE_URL, UNITS, LANG, DEFAULT_CITY, CSV_FILE_PATH

def fetch_weather_data(city=None):
    """
    OpenWeatherMap’ten hava verisini çeker, CSV’e kaydeder ve JSON’u döner.
    """
    # Eğer şehir verilmediyse DEFAULT_CITY kullan
    query_city = city or DEFAULT_CITY

    params = {
        "q": query_city,
        "appid": API_KEY,
        "units": UNITS,
        "lang": LANG
    }

    # API isteği
    response = requests.get(f"{BASE_URL}weather", params=params)
    response.raise_for_status()
    data = response.json()

    # CSV’e yaz (eklenti modu)
    with open(CSV_FILE_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            data["name"],
            data["main"]["temp"],
            data["weather"][0]["description"],
            data["main"]["humidity"],
            data["wind"]["speed"]
        ])

    return data

