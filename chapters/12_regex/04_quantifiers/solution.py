import re


def find_words(text):
    return re.findall(r"[A-Za-z]+", text)
