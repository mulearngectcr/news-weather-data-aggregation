import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

NEWS_KEY = os.getenv("NEWS_API_KEY")
WEATHER_KEY = os.getenv("WEATHER_API_KEY")

def get_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_KEY}&pageSize=5"
    response = requests.get(url).json()
    return response.get("articles", [])

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_KEY}&units=metric"
    return requests.get(url).json()

def main():
    topic = input("Enter a topic of interest: ")
    city = input("Enter city name: ")

    print(f"\n--- Daily Briefing for {city} ---")
    
    # Weather
    w = get_weather(city)
    if w.get("cod") == 200:
        print(f"Weather: {w['weather'][0]['description'].capitalize()}")
        print(f"Temperature: {w['main']['temp']}°C")
        print(f"Humidity: {w['main']['humidity']}%")
    else:
        print("Could not retrieve weather data.")

    # News
    print(f"\n--- Top 5 Headlines for '{topic}' ---")
    articles = get_news(topic)
    if articles:
        for i, art in enumerate(articles, 1):
            print(f"{i}. {art['title']}")
            print(f"   Source: {art['source']['name']}\n")
    else:
        print("No news found for this topic.")

if __name__ == "__main__":
    main()