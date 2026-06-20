import re


def parse_config(text):
    return dict(re.findall(r"(\w+)=(\w+)", text))
