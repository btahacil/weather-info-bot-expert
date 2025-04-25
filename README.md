# 🌤️ Weather Bot

A simple, command-line **Python** tool to fetch real-time weather data from [OpenWeatherMap](https://openweathermap.org/) and log it for later analysis — perfect for scripts, cron jobs, or demonstrative Upwork portfolios! 🚀

---

## ✨ Features

- Fetch current weather by **city** (default from `.env`) 🏙️
- Choose **units**: Celsius (`metric`) or Fahrenheit (`imperial`) 🌡️
- Nicely formatted console output with emojis and clear labels 💬
- Append each run’s data to a local CSV (`data/weather_data.csv`) for historical tracking 📊
- Log informational and error messages to `logs/error.log` 🔍
- Fully configurable via environment variables (`.env`) 🔐
- Easily extensible & open-source 🛠️

---

## 🚀 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/weather-bot.git
   cd weather-bot
   ```
2. **Create & activate a virtual environment**
   - **macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows PowerShell**:
     ```powershell
     python -m venv venv
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
     .\venv\Scripts\activate
     ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configuration

Create a `.env` file in the project root with the following keys:

```ini
API_KEY=your_openweathermap_api_key
UNITS=metric           # "metric" (°C) or "imperial" (°F)
DEFAULT_CITY=Istanbul  # fallback if no city provided
```

> **Tip:** Get a free API key by signing up at [openweathermap.org](https://openweathermap.org/).

---

## 🎬 Usage

### Show help menu
```bash
python main.py --help
```

**Expected output:**
```
usage: main.py [-h] [-c CITY] [-u {metric,imperial}]

Fetch real‑time weather data from OpenWeatherMap

optional arguments:
  -h, --help            show this help message and exit
  -c CITY, --city CITY  City name (overrides DEFAULT_CITY)
  -u {metric,imperial}, --units {metric,imperial}
                        Units for temperature: metric (°C) or imperial (°F)
```

### Default run (uses `.env` values)
```bash
python main.py
```
```
Program started… Waiting for city name…
Enter city name (leave blank for default Istanbul): 
🌦️ Weather Information for Istanbul:
  • Temperature : 12.34°C
  • Description : Light rain
  • Humidity    : 82%
  • Wind Speed  : 3.5 m/s
```

### Override city & units
```bash
python main.py -c Paris -u imperial
```
```
🌤️ Weather Information for Paris:
  • Temperature : 54.32°F
  • Description : Overcast clouds
  • Humidity    : 76%
  • Wind Speed  : 5.2 m/s
```

---

## 💾 Data Logging

Each run appends a new line to `data/weather_data.csv` with:
```
timestamp,city,temperature,weather,humidity,wind_speed
```
Use tools like Excel or pandas to analyze trends. 📈

---

## 📝 Error & Info Logging

All info and error messages are recorded in `logs/error.log`. Example:
```
2025-04-26 02:04:08 INFO: Fetched weather for Istanbul: mist, 10.68°C
2025-04-26 02:04:08 ERROR: Failed to fetch weather for city: Mars
```

---

## 📂 Project Structure

```text
weather-bot/
├── config/
│   └── settings.py      # Load .env & central constants
├── data/
│   └── weather_data.csv # Historical CSV log
├── logs/
│   └── error.log        # Info & error logs
├── utils/
│   └── api_handler.py   # Fetch & save weather data
├── .env                 # API_KEY & defaults (gitignored)
├── main.py              # CLI entrypoint
├── requirements.txt     # Pip dependencies
└── README.md            # This file
```

---

## 🤝 Contributing

1. **Fork** this repo 🎉
2. Create a feature branch:
   ```bash
   git checkout -b feature/my-awesome-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add awesome feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/my-awesome-feature
   ```
5. Open a **Pull Request** 🚀

---

## 📜 License

This project is **MIT-licensed**. See [LICENSE](LICENSE) for details.

---

> _Built with ❤️ for your portfolio & real-time insights!_



