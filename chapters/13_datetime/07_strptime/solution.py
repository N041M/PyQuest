from datetime import datetime


def hour_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").hour
