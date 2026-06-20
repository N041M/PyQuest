A character class in square brackets matches one of the listed characters. For
vowels that's `r"[aeiou]"`.

---

`re.findall(r"[aeiou]", text)` gives a list of every vowel found; `len(...)` of
that list is the count.

---

import re


def count_vowels(text):
    return len(re.findall(r"[aeiou]", text))
