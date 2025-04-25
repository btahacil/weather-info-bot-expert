#!/usr/bin/env python3
# main.py

import argparse
import logging
import os

from dotenv import load_dotenv
from utils.api_handler import fetch_weather_data
from config.settings import LOG_FILE_PATH, DEFAULT_CITY

def parse_args():
    parser = argparse.ArgumentParser(
        description="Fetch real-time weather data from OpenWeatherMap"
    )
    parser.add_argument(
        "-c", "--city",
        type=str,
        default=None,
        help="City name (overrides default from .env)"
    )
    parser.add_argument(
        "-u", "--units",
        choices=["metric", "imperial"],
        default=None,
        help="Units for temperature (metric=°C, imperial=°F)"
    )
    return parser.parse_args()

def main():
    # 1) .env dosyasını yükle
    load_dotenv()

    # 2) Logging ayarları
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 3) Komut satırı argümanlarını işle
    args = parse_args()

    # Birim tercihini ENV'e yaz
    if args.units:
        os.environ["UNITS"] = args.units

    # Şehir tercihi
    city = args.city or None

    # 4) Kullanıcıdan şehir iste (varsa atla)
    print("Program started... Waiting for city name...")
    if not city:
        prompt = f"Enter city name (leave blank for default {DEFAULT_CITY}): "
        city = input(prompt).strip() or None

    # 5) Veriyi çek ve CSV'e ekle
    data = fetch_weather_data(city)

    # 6) Çıktıyı göster ve logla
    if data:
        name       = data.get("name")
        temp       = data["main"]["temp"]
        desc       = data["weather"][0]["description"].capitalize()
        humidity   = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        unit_label = "°C" if os.getenv("UNITS", "metric") == "metric" else "°F"

        print(f"\nWeather Information for {name}:")
        print(f" • Temperature: {temp}{unit_label}")
        print(f" • Description: {desc}")
        print(f" • Humidity: {humidity}%")
        print(f" • Wind Speed: {wind_speed} m/s")

        logging.info(f"Fetched weather for {name}: {desc}, {temp}{unit_label}")
    else:
        print("Failed to retrieve weather data.")
        logging.error(f"Failed to fetch weather for city: {city or 'default'}")

if __name__ == "__main__":
    main()



