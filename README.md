# 🌦️ Weather Info Bot Expert

I developed this professional command-line **Python** tool to fetch real-time weather data from [OpenWeatherMap](https://openweathermap.org/). My goal was to build a project that could be used in automation scripts, scheduled tasks, or as a solid portfolio piece showcasing my skills in API integration, data logging, and environment management.

---

## ✨ Features

- The bot fetches live weather data based on a **city** input (or a default city defined in `.env`)
- I added support to choose between **Celsius** (`metric`) and **Fahrenheit** (`imperial`)
- The console output is formatted clearly, with emojis and readable labels
- Each run appends the data into `data/weather_data.csv` so I can track and analyze trends
- Logs are saved into `logs/error.log` for better debugging and error handling
- I used environment variables to store sensitive data and settings (`.env`)
- The bot is modular and easy to expand — future features can be added quickly

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/btahacil/weather-info-bot-expert.git
cd weather-info-bot-expert

# 2. Set up virtual environment
python -m venv venv

# Activate:
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 🔧 Configuration

I used a `.env` file for secure API key management and default settings. Example:

```
API_KEY=your_openweathermap_api_key
DEFAULT_CITY=Istanbul
UNITS=metric
```

You can get a free API key from [OpenWeatherMap](https://openweathermap.org/api).

---

## 🧪 Usage

```bash
# Show help
python main.py --help

# Default run (uses .env values)
python main.py

# Custom city and units
python main.py -c Paris -u imperial
```

**Sample output:**

```
🌤️ Weather Information for Paris:
  • Temperature : 54.3°F
  • Description : Overcast clouds
  • Humidity    : 76%
  • Wind Speed  : 5.2 m/s
```

---

## 💾 Data Logging

Each time I run the bot, it appends a new row into `data/weather_data.csv`, like this:

```
timestamp,city,temperature,weather,humidity,wind_speed
2025-04-26T02:04:08Z,Istanbul,10.68,Mist,87%,1.03
```

---

## 🧠 Error & Info Logging

I also set up logging to store all console messages in `logs/error.log`. This includes both info and error messages, like:

```
2025-04-26 02:04:08 INFO: Fetched weather for Istanbul: mist, 10.68°C
2025-04-26 02:04:08 ERROR: Failed to fetch weather for city: Mars
```

---

## 📁 Project Structure

```
weather-info-bot-expert/
├── config/                # settings.py (env loader)
├── data/                  # weather_data.csv
├── logs/                  # error.log
├── utils/                 # api_handler.py
├── main.py                # CLI entrypoint
├── .env                   # API key & defaults (gitignored)
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🧩 Technologies Used

- Python 3
- OpenWeatherMap API
- Environment variables (.env)
- Logging, CSV, argparse

---

## 🤝 Contributing

Feel free to fork, modify, or suggest improvements — pull requests are always welcome!

---

## 🏷️ License

MIT License — You can use, modify, and share this project freely!







