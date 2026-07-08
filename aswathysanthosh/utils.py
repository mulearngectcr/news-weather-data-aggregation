import json


def save_json(data):
    """
    Saves the daily briefing into a JSON file.
    """

    with open("briefing.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)