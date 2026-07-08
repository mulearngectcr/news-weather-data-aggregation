import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def get_news(topic):
    """
    Fetches the latest 5 news articles based on the given topic.
    """

    url = (
        "https://newsapi.org/v2/everything?"
        f"q={topic}"
        "&language=en"
        "&sortBy=publishedAt"
        "&pageSize=5"
        f"&apiKey={NEWS_API_KEY}"
    )

    try:
        response = requests.get(url, timeout=10)

        # Invalid API Key
        if response.status_code == 401:
            return "Invalid News API Key."

        response.raise_for_status()

        data = response.json()

        if data["status"] != "ok":
            return None

        articles = data.get("articles", [])

        if len(articles) == 0:
            return None

        news = []

        for article in articles:
            news.append({
                "title": article.get("title", "No Title"),
                "source": article["source"].get("name", "Unknown"),
                "url": article.get("url", "No URL")
            })

        return news

    except requests.exceptions.RequestException:
        return "Unable to connect to News API."


def get_weather(city):
    """
    Fetches the current weather of the given city.
    """

    url = (
        "http://api.weatherapi.com/v1/current.json"
        f"?key={WEATHER_API_KEY}"
        f"&q={city}"
    )

    try:
        response = requests.get(url, timeout=10)

        # Invalid API Key
        if response.status_code == 401:
            return "Invalid Weather API Key."

        response.raise_for_status()

        data = response.json()

        if "error" in data:
            return None

        return {
            "city": data["location"]["name"],
            "condition": data["current"]["condition"]["text"],
            "temperature": data["current"]["temp_c"],
            "humidity": data["current"]["humidity"]
        }

    except requests.exceptions.RequestException:
        return "Unable to connect to Weather API."