`import re`, then `re.findall(pattern, text)` returns a list of every match. You
want runs of digits.

---

The pattern `r"\d+"` matches one or more digits in a row, so each match is a full
number. `re.findall(r"\d+", text)` is the whole answer.

---

import re


def all_numbers(text):
    return re.findall(r"\d+", text)
