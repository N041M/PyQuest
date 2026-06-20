Use two capture groups, one for the key and one for the value, with a literal `=`
between: `r"(\w+)=(\w+)"`.

---

With two groups, `re.findall(pattern, text)` returns a list of `(key, value)`
tuples. `dict(...)` of that list is the config dictionary.

---

import re


def parse_config(text):
    return dict(re.findall(r"(\w+)=(\w+)", text))
