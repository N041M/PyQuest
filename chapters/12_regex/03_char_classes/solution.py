import re


def count_vowels(text):
    return len(re.findall(r"[aeiou]", text))
