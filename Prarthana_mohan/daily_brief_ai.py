import requests
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=".env")
NEWS_API_KEY=os.getenv("NEWS_API_KEY")
WEATHER_API_KEY=os.getenv("WEATHER_API_KEY")
print("\n======================")
print("      DAILY BRIEF")
print("======================\n")
topic=input("enter your topic")
newsurl="https://newsapi.org/v2/everything"
query_param={
    "q":topic,
    "apiKey": NEWS_API_KEY
}
response=requests.get(newsurl,params=query_param)
status1=response.status_code
if status1==200:
    print("News")
    print("\n")
    data=response.json()
    for article in data["articles"][:5]:
        print("Title:",article["title"])
        print("Source:",article["source"]["name"])

city=input("enter your city")
url="https://api.weatherapi.com/v1/current.json"
query_param2={
    "q":city,
    "key": WEATHER_API_KEY
}
response=requests.get(url,params=query_param2)
status=response.status_code
if status==200:
    data2=response.json()
    print("weather")
    print("\n")
    print("Name:",data2["location"]["name"])
    print("region:",data2["location"]["region"])
    print("temperature:",data2["current"]["temp_c"])   
    print("Humidity:",data2["current"]["humidity"]) 
print("NEWS KEY:", os.getenv("NEWS_API_KEY"))
print("WEATHER KEY:", os.getenv("WEATHER_API_KEY"))
import os
print("Current working directory:", os.getcwd())
