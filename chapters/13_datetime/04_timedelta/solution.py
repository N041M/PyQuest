from datetime import date, timedelta


def add_days(text, n):
    return (date.fromisoformat(text) + timedelta(days=n)).isoformat()
