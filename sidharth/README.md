# Description

A Python CLI program that aggregates Weather and News information into a daily briefing report.
The program takes the topic of interest and city as input, and outputs the report. I chose to attempt the following bonus challenges:
- Handle invalid API keys gracefully.
- Handle invalid city names
- Display the top news article URL

---


## File Structure

```
.
├── main.py             ← Main script
├── requirements.txt    ← Python dependencies
├── .env                ← API keys
├── .gitignore          ← Keeps .env out of Git
└── README.md
```

---

## APIs used

| Service | Sign-up URL | Free tier |
|---|---|---|
| NewsAPI | https://newsapi.org/register | 100 req/day |
| OpenWeatherMap | https://home.openweathermap.org/users/sign_up | 1 000 req/day |


### 5 — Run the app

```bash
python daily_briefing.py
```

You will be prompted for:
- A **topic** (e.g. `AI`, `Finance`, `Climate`, `Sports`)
- A **city** (e.g. `London`, `Tokyo`, `New York`)

---

## Example Output

```
Enter topic of interest: AI
Enter city name: Kochi

------------------------------------------------------------
PERSONALIZED DAILY BRIEFING
------------------------------------------------------------

Weather in Kochi
Condition   : scattered clouds
Temperature : 29.3°C
Humidity    : 74%

USD → INR Exchange Rate: ₹83.12

Top 5 News Headlines

1. OpenAI launches new model...
   Source : Reuters
   URL    : https://...

2. AI startup raises funding...
   Source : TechCrunch
   URL    : https://...

...

```

---

