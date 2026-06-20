import re


def redact(text):
    return re.sub(r"\d+", "#", text)
