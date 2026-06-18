import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY") # fetch the api key from environment variables
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def get_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&pageSize=5&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 401:
        raise Exception("Invalid NewsAPI key.") # 401 error code means request lacks correct auth, so here it means API key is invalid
    data = response.json()
    return data["articles"]


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 401:
        raise Exception("Invalid OpenWeatherMap API key.")
    if response.status_code == 404:
        raise Exception("City not found.")
    data = response.json()

    return {
        "condition": data["weather"][0]["description"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"]
    }


def main():
    topic = input("Enter topic of interest: ")
    city = input("Enter city name: ")

    try:
        news_articles = get_news(topic)
        weather = get_weather(city)

        print("\n" + "-"*60)
        print("PERSONALIZED DAILY BRIEFING")
        print("-"*60)

        print(f"\nWeather in {city}")
        print(f"Condition   : {weather['condition']}")
        print(f"Temperature : {weather['temperature']} C")
        print(f"Humidity    : {weather['humidity']}%")


        print("\nTop 5 News Headlines\n")
        for i, article in enumerate(news_articles, start=1):
            print(f"{i}. {article['title']}")
            print(f"   Source : {article['source']['name']}")
            print(f"   URL    : {article['url']}")
            print("\n")


    except Exception as e:
        print("Error")

if __name__ == "__main__":
    main()
