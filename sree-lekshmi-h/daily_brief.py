import tkinter as tk
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("news_API_KEY")
api_key2 = os.getenv("weather_API_KEY")
def get_info():
    topic = topic_entry.get()
    city = city_entry.get()

    output.delete("1.0", tk.END)

    if not api_key:
        output.insert(tk.END, "News API key not found!\n")
        return

    if not api_key2:
        output.insert(tk.END, "Weather API key not found!\n")
        return

    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=popularity&apiKey={api_key}"
    url2 = f"http://api.weatherapi.com/v1/current.json?key={api_key2}&q={city}"

    response = requests.get(url)
    response2 = requests.get(url2)

    output.insert(tk.END, "====== Top 5 News ======\n\n")

    if response.status_code == 200:
        data = response.json()

        if data["totalResults"] == 0:
            output.insert(tk.END, "No news articles found.\n")
        else:
            articles = data["articles"]

            for i, article in enumerate(articles[:5]):
                description = article["description"] or "No description available"

                output.insert(
                    tk.END,
                    f"{i+1}. {article['title']}\n"
                    f"   Source: {article['source']['name']}\n"
                    f"   Description: {description}\n\n"
                )
    else:
        output.insert(tk.END, f"Error: {response.status_code}\n")
        output.insert(tk.END, response.text + "\n")

    output.insert(tk.END, "\n====== Weather ======\n\n")
    if response2.status_code == 200:
        data2 = response2.json()

        temp = data2['current']['temp_c']
        condition = data2['current']['condition']['text']
        humidity = data2['current']['humidity']

        if "Sunny" in condition:
            emoji = "☀️"
        elif "Cloud" in condition:
            emoji = "☁️"
        elif "Rain" in condition:
            emoji = "🌧️"
        elif "Thunder" in condition:
            emoji = "⛈️"
        else:
            emoji = "🌤️"
        output.insert(tk.END, f"Temperature: {temp}°C\n")
        output.insert(tk.END, f"{emoji}   {condition}\n")
        output.insert(tk.END, f"Humidity: {humidity}%\n")

    else:
        output.insert(tk.END, "Error fetching weather data\n")
        output.insert(tk.END, f"{response2.status_code}\n")
        output.insert(tk.END, response2.text + "\n")
root = tk.Tk()
root.title("Weather Brief")
root.geometry("800x600")
tk.Label(root, text="Topic").pack(pady=5)
topic_entry = tk.Entry(root, width=40)
topic_entry.pack()

tk.Label(root, text="City").pack(pady=5)
city_entry = tk.Entry(root, width=40)
city_entry.pack()

tk.Button(
    root,
    text="Get News & Weather",
    command=get_info
).pack(pady=10)
output = tk.Text(root, width=95, height=25)
output.pack(pady=10)
root.mainloop()