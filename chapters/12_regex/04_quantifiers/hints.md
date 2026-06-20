A word is one or more letters in a row. The character class `[A-Za-z]` matches a
single letter; the quantifier `+` makes it match a run.

---

`re.findall(r"[A-Za-z]+", text)` returns every word, stopping each match at the
first non-letter. That's the whole function.

---

import re


def find_words(text):
    return re.findall(r"[A-Za-z]+", text)
