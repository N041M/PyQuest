from datetime import date


def iso(y, m, d):
    return date(y, m, d).isoformat()
