import requests
import json
import os
from dotenv import load_dotenv

#load api key
load_env()

news_api_key=os.getenv("NEWS_API_KEY")
weather_api_keyos.getenv("WEATHER_API_KEY")

def get_news(topic):
    url=(
        f"https://newsapi.org/v2/everything?"
        f"q={topic}&"
        f"sortBy=publishedAt&"
        f"pageSize=5&"
        f"apiKey={NEWS_API_KEY}"
    )
    response=requests.get(url)
    if response.staus_code==401:
        print("invalid news_api_key")
        return []
    data=response.json
    print(data)
    return data.get("articles",[])

def get_weather(city):
    url=(
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&"
        f"appid={WEATHER_API_KEY}&"
        f"units=metric"
    )
    response=requests.get(url)
    if reponse.status_code==401:
        print("Invalid weather api key")
        return None
    if reponse.status_code==404:
        print("city not found")
        return None
    return  response.json()
def save_briefing(briefing):

    with open("briefing.json", "w", encoding="utf-8") as file:
        json.dump(
            briefing,
            file,
            indent=4,
            ensure_ascii=False
        )
def main():

    topic = input("Enter topic: ")
    city = input("Enter city: ")

    news = get_news(topic)
    weather = get_weather(city)

    if weather is None:
        return

    print("\n===== DAILY BRIEF =====\n")

    print(f"City: {city}")
    print(
        f"Weather: "
        f"{weather['weather'][0]['description']}"
    )
    print(
        f"Temperature: "
        f"{weather['main']['temp']} °C"
    )
    print(
        f"Humidity: "
        f"{weather['main']['humidity']}%"
    )

    print("\nTop News Headlines\n")

    briefing = {
        "topic": topic,
        "city": city,
        "weather": {
            "condition": weather["weather"][0]["description"],
            "temperature": weather["main"]["temp"],
            "humidity": weather["main"]["humidity"]
        },
        "news": []
    }

    for i, article in enumerate(news, start=1):

        title = article["title"]
        source = article["source"]["name"]
        url = article["url"]

        print(f"{i}. {title}")
        print(f"   Source: {source}")
        print(f"   URL: {url}\n")

        briefing["news"].append({
            "headline": title,
            "source": source,
            "url": url
        })

    save_briefing(briefing)

    print("Briefing saved to briefing.json")


if __name__ == "__main__":
    main()
