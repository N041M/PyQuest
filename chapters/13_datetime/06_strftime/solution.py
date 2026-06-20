from datetime import date


def pretty(text):
    return date.fromisoformat(text).strftime("%d/%m/%Y")
