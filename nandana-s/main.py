import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
CURRENCY_API_KEY = os.getenv("CURRENCY_API_KEY")


def fetch_news(topic):

    url = (
        "https://newsapi.org/v2/everything"
        f"?q={topic}"
        f"&pageSize=5"
        f"&sortBy=publishedAt"
        f"&apiKey={NEWS_API_KEY}"
    )

    try:

        response = requests.get(url, timeout=10)

        if response.status_code in [401, 403]:
            return None

        response.raise_for_status()

        data = response.json()

        return data.get("articles", [])

    except requests.exceptions.RequestException:
        return []


def fetch_weather(city):

    url = (
        "https://api.weatherapi.com/v1/current.json"
        f"?key={WEATHER_API_KEY}"
        f"&q={city}"
    )

    try:

        response = requests.get(url, timeout=10)

        if response.status_code in [401, 403]:
            return None

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException:
        return {}


def fetch_currency():

    url = (
        f"https://v6.exchangerate-api.com/v6/"
        f"{CURRENCY_API_KEY}/latest/USD"
    )

    try:

        response = requests.get(url, timeout=10)

        if response.status_code in [401, 403]:
            return None

        response.raise_for_status()

        data = response.json()

        return data["conversion_rates"]["INR"]

    except:
        return None


def save_brief(data, city):

    os.makedirs(
        "saved_briefs",
        exist_ok=True
    )

    filename = (
        f"saved_briefs/{city}.json"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    return filename