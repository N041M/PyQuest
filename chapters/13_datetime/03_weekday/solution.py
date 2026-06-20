from datetime import date


def weekday(text):
    return date.fromisoformat(text).weekday()
