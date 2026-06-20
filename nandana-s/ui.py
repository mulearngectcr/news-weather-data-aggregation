import tkinter as tk
from tkinter import messagebox

from main import (
    fetch_news,
    fetch_weather,
    fetch_currency,
    save_brief
)


class DailyBriefApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Personalized Daily Brief"
        )

        self.root.geometry(
            "900x700"
        )

        title = tk.Label(
            root,
            text="Personalized Daily Brief",
            font=("Arial", 20, "bold")
        )

        title.pack(pady=10)

        topic_label = tk.Label(
            root,
            text="Topic"
        )

        topic_label.pack()

        self.topic_entry = tk.Entry(
            root,
            width=40,
            font=("Arial", 12)
        )

        self.topic_entry.pack(
            pady=5
        )

        city_label = tk.Label(
            root,
            text="City"
        )

        city_label.pack()

        self.city_entry = tk.Entry(
            root,
            width=40,
            font=("Arial", 12)
        )

        self.city_entry.pack(
            pady=5
        )

        generate_btn = tk.Button(
            root,
            text="Generate Brief",
            command=self.generate_brief
        )

        generate_btn.pack(
            pady=10
        )

        self.result_text = tk.Text(
            root,
            width=110,
            height=35
        )

        self.result_text.pack(
            pady=10
        )

    def generate_brief(self):

        topic = (
            self.topic_entry
            .get()
            .strip()
        )

        city = (
            self.city_entry
            .get()
            .strip()
        )

        if not topic or not city:

            messagebox.showerror(
                "Error",
                "Please enter both topic and city."
            )

            return

        news = fetch_news(topic)

        if news is None:

            messagebox.showerror(
                "Error",
                "Invalid News API Key."
            )

            return

        weather = fetch_weather(city)

        if weather is None:

            messagebox.showerror(
                "Error",
                "Invalid Weather API Key."
            )

            return

        if "error" in weather:

            messagebox.showerror(
                "Error",
                "Invalid city name."
            )

            return

        currency = fetch_currency()

        brief_data = {
            "topic": topic,
            "city": city,
            "weather": weather,
            "news": news,
            "usd_to_inr": currency
        }

        saved_file = save_brief(
            brief_data,
            city
        )

        output = f"""
PERSONALIZED DAILY BRIEF

Topic: {topic}

City: {city}

=====================================

WEATHER

Condition:
{weather['current']['condition']['text']}

Temperature:
{weather['current']['temp_c']} °C

Humidity:
{weather['current']['humidity']} %

=====================================

CURRENCY

1 USD = {currency} INR

=====================================

TOP 5 NEWS
"""

        for index, article in enumerate(news, start=1):

            output += f"""

{index}. {article.get('title', 'N/A')}

Source:
{article.get('source', {}).get('name', 'Unknown')}

URL:
{article.get('url', 'N/A')}
"""

        output += f"""

=====================================

Saved To:
{saved_file}
"""

        self.result_text.delete(
            "1.0",
            tk.END
        )

        self.result_text.insert(
            tk.END,
            output
        )


if __name__ == "__main__":

    root = tk.Tk()

    app = DailyBriefApp(root)

    root.mainloop()