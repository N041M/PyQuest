import re


def is_valid_code(text):
    return re.fullmatch(r"[A-Z]{2}\d{4}", text) is not None
