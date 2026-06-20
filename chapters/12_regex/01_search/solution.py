import re


def has_digit(text):
    return re.search(r"\d", text) is not None
