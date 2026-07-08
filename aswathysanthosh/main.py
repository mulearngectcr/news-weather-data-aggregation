from api import get_news, get_weather
from utils import save_json


def main():
    print("=" * 50)
    print("      Personalized Daily Brief")
    print("=" * 50)

    # Get user input
    topic = input("Enter a topic (AI, Technology, Sports, etc.): ").strip()
    city = input("Enter city name: ").strip()

    # Fetch data from APIs
    news = get_news(topic)
    weather = get_weather(city)

    # Handle invalid API keys
    if isinstance(news, str):
        print(f"\n❌ {news}")
        return

    if isinstance(weather, str):
        print(f"\n❌ {weather}")
        return

    # Handle invalid topic
    if news is None:
        print("\n❌ No news found for the given topic.")
        return

    # Handle invalid city
    if weather is None:
        print("\n❌ Invalid city name.")
        return

    # Display Weather
    print("\n" + "=" * 50)
    print("🌤 WEATHER REPORT")
    print("=" * 50)

    print(f"City         : {weather['city']}")
    print(f"Condition    : {weather['condition']}")
    print(f"Temperature  : {weather['temperature']} °C")
    print(f"Humidity     : {weather['humidity']}%")

    # Display News
    print("\n" + "=" * 50)
    print("📰 TOP 5 NEWS HEADLINES")
    print("=" * 50)

    for i, article in enumerate(news, start=1):
        print(f"\n{i}. {article['title']}")
        print(f"   Source : {article['source']}")
        print(f"   URL    : {article['url']}")

    # Combine data
    briefing = {
        "weather": weather,
        "news": news
    }

    # Save to JSON
    save_json(briefing)

    print("\n" + "=" * 50)
    print("✅ Daily briefing has been saved to 'briefing.json'")
    print("=" * 50)


if __name__ == "__main__":
    main()