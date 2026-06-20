import re


def all_numbers(text):
    return re.findall(r"\d+", text)
