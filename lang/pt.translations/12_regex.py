# PyQuest translations -- language 'pt' -- chapter 12_regex -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"12.1 brief": r"""# 12.1 -- re.search: is the pattern there?

## Concept

A **regular expression** ("regex") is a small language for describing patterns
in text. The **`re`** module matches them. The most basic question is "does this
pattern appear anywhere?" -- **`re.search`**:

```python
import re

re.search(r"\d", "abc4")     # a match object (truthy)
re.search(r"\d", "abc")      # None
```

- The pattern is written as a **raw string** `r"..."` so backslashes mean what
  regex expects (`r"\d"`, not `"\d"`).
- `\d` matches any single **digit**. Other shorthands: `\w` a word character,
  `\s` whitespace, `.` any character.
- `re.search` returns a **match object** if the pattern is found anywhere, or
  **`None`** if not -- so `re.search(...) is not None` is a clean yes/no.

## Example

```python
import re

def has_letter(text):
    return re.search(r"[a-z]", text) is not None
```

## Your task

Using **`re.search`**, define `has_digit(text)` that returns `True` if `text`
contains at least one digit, `False` otherwise.

## Done when

- `has_digit("abc4")` is `True`, `has_digit("abc")` is `False`.
- `has_digit("")` is `False`.
- The test uses `re.search` with `\d`, not a hand-written digit scan.
""",

"12.1 hints": r"""`import re`, then `re.search(pattern, text)`. The pattern for a single digit is
the raw string `r"\d"`.

---

`re.search` returns a match object when it finds the pattern, or `None` when it
doesn't. Turn that into a bool with `is not None`.

---

import re


def has_digit(text):
    return re.search(r"\d", text) is not None
""",

"12.1 reference": r"""A **regular expression** is a pattern describing a set of strings; the **`re`**
module matches them against text. **`re.search(pattern, text)`** scans the whole
string for the **first** place the pattern matches and returns a **match object**
(which is truthy) or **`None`**.

- Write patterns as **raw strings** — `r"\d"` — so the backslashes reach the
  regex engine instead of being interpreted by Python first.
- Shorthand classes: `\d` a digit, `\w` a word character `[A-Za-z0-9_]`, `\s`
  whitespace, and `.` any character but newline.
- `re.search` looks **anywhere** in the string; `re.match` only checks the start.
  Because the result is a match object or `None`, `re.search(...) is not None` is
  a clean membership test.

```python
import re

re.search(r"\d", "abc4")     # <re.Match object; match='4'>
re.search(r"\d", "abc")      # None
bool(re.search(r"\s", "a b"))  # True -- contains whitespace
```
""",

"12.2 brief": r"""# 12.2 -- re.findall: every match

## Concept

`re.search` finds the *first* match. **`re.findall`** returns **all** of them, as
a list of strings:

```python
import re

re.findall(r"\d+", "a12b3c456")     # ['12', '3', '456']
```

- `\d+` means "one or more digits" -- the `+` makes the pattern grab a whole run
  of digits, not just one. So each match is a full number.
- `re.findall` returns a **list of strings** (the matched text), left to right,
  non-overlapping. No match gives the empty list `[]`.
- The matches are still text; convert with `int(...)` if you want numbers.

## Example

```python
import re

def words(text):
    return re.findall(r"[a-z]+", text)
```

## Your task

Using **`re.findall`**, define `all_numbers(text)` that returns a list of every
run of digits in `text`, as strings.

## Done when

- `all_numbers("a12b3c456")` returns `["12", "3", "456"]`.
- `all_numbers("nothing")` returns `[]`.
- The extraction uses `re.findall` with `\d+`, not a hand-written scan.
""",

"12.2 hints": r"""`import re`, then `re.findall(pattern, text)` returns a list of every match. You
want runs of digits.

---

The pattern `r"\d+"` matches one or more digits in a row, so each match is a full
number. `re.findall(r"\d+", text)` is the whole answer.

---

import re


def all_numbers(text):
    return re.findall(r"\d+", text)
""",

"12.2 reference": r"""**`re.findall(pattern, text)`** returns a **list of every** non-overlapping match
of the pattern, left to right — the extract-them-all counterpart to `re.search`'s
find-the-first.

- A **quantifier** makes one pattern match a run: `\d+` is "one or more digits",
  so each match is a whole number rather than a single digit. (`+` one-or-more,
  `*` zero-or-more, `?` optional, `{n}` exactly n.)
- Each item in the returned list is the **matched text** (a string); no match
  gives `[]`. Convert with `int(...)` when you want numbers.
- If the pattern has capture groups, `findall` returns the groups instead of the
  whole match (see 12.5); with one group it's a list of that group's text.

```python
import re

re.findall(r"\d+", "a12b3c456")     # ['12', '3', '456']
re.findall(r"[a-z]+", "Hi there!")  # ['i', 'there']
[int(n) for n in re.findall(r"\d+", "p1 p22")]   # [1, 22]
```
""",

"12.3 brief": r"""# 12.3 -- Character classes: [aeiou]

## Concept

A **character class** `[...]` matches **any one** of the characters listed inside
it:

```python
import re

re.findall(r"[aeiou]", "education")     # ['e', 'u', 'a', 'i', 'o']
```

- `[aeiou]` matches a single vowel; `[abc]` matches `a`, `b`, or `c`.
- A **range** uses a hyphen: `[a-z]` is any lowercase letter, `[0-9]` any digit
  (the same as `\d`), `[A-Za-z0-9]` any letter or digit.
- A leading `^` **negates** the class: `[^aeiou]` is any character that is *not*
  a vowel.

A class is one character; add a quantifier (`[a-z]+`) to match a run of them.

## Example

```python
import re

def count_letters(text):
    return len(re.findall(r"[a-z]", text))
```

## Your task

Using a character class with **`re.findall`**, define `count_vowels(text)` that
returns how many vowels (`a e i o u`) are in `text`.

## Done when

- `count_vowels("education")` returns `5`, `count_vowels("xyz")` returns `0`.
- `count_vowels("")` returns `0`.
- Counting uses `re.findall` with a `[aeiou]` class, not a manual `in` check.
""",

"12.3 hints": r"""A character class in square brackets matches one of the listed characters. For
vowels that's `r"[aeiou]"`.

---

`re.findall(r"[aeiou]", text)` gives a list of every vowel found; `len(...)` of
that list is the count.

---

import re


def count_vowels(text):
    return len(re.findall(r"[aeiou]", text))
""",

"12.3 reference": r"""A **character class** `[...]` matches **exactly one** character from the set
listed inside it. `[aeiou]` matches any single vowel; `[abc]` matches `a`, `b`,
or `c`.

- A **range** with a hyphen covers consecutive characters: `[a-z]` any lowercase
  letter, `[0-9]` any digit, `[A-Za-z0-9]` any letter or digit. Combine sets and
  ranges freely inside one class.
- A leading **`^`** negates: `[^aeiou]` matches any character that is *not* a
  vowel.
- The class matches **one** character; add a quantifier for a run — `[a-z]+` is a
  word, `[0-9]{4}` exactly four digits. Inside a class most metacharacters lose
  their special meaning (`[.]` is a literal dot).

```python
import re

re.findall(r"[aeiou]", "education")   # ['e', 'u', 'a', 'i', 'o']
re.findall(r"[^a-z ]", "a1 b2!")      # ['1', '2', '!']
re.findall(r"[A-Z][a-z]+", "Ada Lovelace")   # ['Ada', 'Lovelace']
```
""",

"12.4 brief": r"""# 12.4 -- Quantifiers: + means one or more

## Concept

A **quantifier** says how many times the pattern before it may repeat:

- **`+`** -- one or more (`[a-z]+` is a run of one or more lowercase letters)
- **`*`** -- zero or more
- **`?`** -- optional (zero or one)
- **`{n}`** -- exactly `n`; **`{n,m}`** -- between `n` and `m`

```python
import re

re.findall(r"[A-Za-z]+", "Hello, world!")     # ['Hello', 'world']
```

Without the `+`, `[A-Za-z]` would match single letters one at a time. The `+`
makes it grab the **whole word**, stopping at the first character that doesn't
fit (a space, comma, digit). That's how you split text into words while ignoring
punctuation.

## Example

```python
import re

def integers(text):
    return re.findall(r"\d+", text)
```

## Your task

Using **`re.findall`** with a quantifier, define `find_words(text)` that returns
a list of the words in `text` -- each a run of one or more letters
(`[A-Za-z]+`), with punctuation and spaces ignored.

## Done when

- `find_words("Hello, world!")` returns `["Hello", "world"]`.
- `find_words("one-two three")` returns `["one", "two", "three"]`.
- `find_words("")` returns `[]`.
- Words are matched with `[A-Za-z]+`, not split by hand.
""",

"12.4 hints": r"""A word is one or more letters in a row. The character class `[A-Za-z]` matches a
single letter; the quantifier `+` makes it match a run.

---

`re.findall(r"[A-Za-z]+", text)` returns every word, stopping each match at the
first non-letter. That's the whole function.

---

import re


def find_words(text):
    return re.findall(r"[A-Za-z]+", text)
""",

"12.4 reference": r"""A **quantifier** controls how many times the pattern immediately before it
repeats:

- **`+`** one or more, **`*`** zero or more, **`?`** zero or one (optional),
- **`{n}`** exactly *n*, **`{n,m}`** between *n* and *m*, **`{n,}`** at least *n*.

`[A-Za-z]+` therefore matches a whole **word** — a run of one or more letters —
stopping at the first character that doesn't fit, which is how you tokenize text
while ignoring spaces and punctuation.

- Quantifiers are **greedy** by default: they match as much as possible. A
  trailing `?` makes one **lazy** (`\d+?` matches as few digits as it can).
- The quantifier applies to the single item before it — a character, a class, or
  a parenthesised group: `(ab)+` matches `ababab`.

```python
import re

re.findall(r"[A-Za-z]+", "Hello, world!")   # ['Hello', 'world']
re.findall(r"\d{4}", "y2024 y2025")          # ['2024', '2025']
re.search(r"colou?r", "color")               # matches (the u is optional)
```
""",

"12.5 brief": r"""# 12.5 -- Groups: capture the parts

## Concept

Parentheses **`(...)`** in a pattern mark a **capture group**: a piece of the
match you want to pull out. The match object then hands each one back:

```python
import re

m = re.match(r"(\d+)-(\d+)-(\d+)", "2026-06-20")
m.group(1)     # '2026'
m.group(2)     # '06'
m.groups()     # ('2026', '06', '20')
```

- `re.match` matches from the **start** of the string and returns a match object
  (or `None`).
- `m.group(n)` returns the text the *n*-th group captured (`group(0)` is the
  whole match); `m.groups()` returns them all as a tuple.
- The captured text is still a string -- `int(m.group(1))` if you want a number.

One pattern thus both checks the shape and extracts the fields.

## Example

```python
import re

def split_pair(text):
    m = re.match(r"(\w+):(\w+)", text)
    return (m.group(1), m.group(2))
```

## Your task

Using **`re.match`** with capture groups, define `parse_date(text)` that takes a
date like `"2026-06-20"` and returns the tuple of **integers**
`(year, month, day)`.

## Done when

- `parse_date("2026-06-20")` returns `(2026, 6, 20)`.
- `parse_date("1999-01-05")` returns `(1999, 1, 5)`.
- The fields come from capture groups, not `text.split("-")`.
""",

"12.5 hints": r"""Wrap each part you want in parentheses: `r"(\d+)-(\d+)-(\d+)"`. Each `(...)` is a
capture group.

---

`m = re.match(pattern, text)` then read `m.group(1)`, `m.group(2)`, `m.group(3)`.
They're strings, so wrap each in `int(...)` for the tuple.

---

import re


def parse_date(text):
    m = re.match(r"(\d+)-(\d+)-(\d+)", text)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
""",

"12.5 reference": r"""Parentheses **`(...)`** in a pattern create a **capture group** — a sub-part of
the match the engine remembers so you can read it back. The match object exposes
them:

- **`m.group(n)`** returns the text the *n*-th group captured, numbered left to
  right from 1; **`m.group(0)`** (or `m.group()`) is the whole match.
- **`m.groups()`** returns every group's text as a tuple — ideal for unpacking.
- Captured text is a **string**; convert with `int(...)` as needed. A group that
  didn't participate is `None`.

So one pattern both **validates** the shape and **extracts** the fields. `re.match`
anchors at the start and returns the match object or `None`; guard for `None`
before reading groups when the input might not match. Name groups with
`(?P<name>...)` and read them via `m.group("name")` for clarity.

```python
import re

m = re.match(r"(\d+)-(\d+)-(\d+)", "2026-06-20")
m.groups()                # ('2026', '06', '20')
tuple(int(p) for p in m.groups())   # (2026, 6, 20)
```
""",

"12.6 brief": r"""# 12.6 -- re.sub: find and replace by pattern

## Concept

`str.replace` swaps a fixed substring. **`re.sub`** swaps everything matching a
**pattern**:

```python
import re

re.sub(r"\d+", "#", "call 555-1234 now")     # 'call #-# now'
```

- `re.sub(pattern, replacement, text)` returns a **new** string with **every**
  match of `pattern` replaced by `replacement`.
- Because `\d+` matches a whole run of digits, each run collapses to a single
  `#` -- one replacement per match, not per character.
- No match leaves the text unchanged. The replacement can also reference captured
  groups (`\1`), but a plain string is the common case.

## Example

```python
import re

def squash_spaces(text):
    return re.sub(r"\s+", " ", text)
```

## Your task

Using **`re.sub`**, define `redact(text)` that replaces every run of digits in
`text` with a single `"#"`.

## Done when

- `redact("call 555-1234")` returns `"call #-#"`.
- `redact("no digits")` returns `"no digits"`.
- Each digit *run* becomes one `#` (use `\d+`), via `re.sub` -- not a character
  loop.
""",

"12.6 hints": r"""`re.sub(pattern, replacement, text)` replaces every match. Your pattern is a run
of digits, your replacement is `"#"`.

---

`r"\d+"` matches a whole run of digits, so each run becomes one `#`:
`re.sub(r"\d+", "#", text)` is the entire function.

---

import re


def redact(text):
    return re.sub(r"\d+", "#", text)
""",

"12.6 reference": r"""**`re.sub(pattern, repl, text)`** is pattern-driven search-and-replace: it returns
a **new** string with **every** non-overlapping match of `pattern` replaced by
`repl`. Where `str.replace` swaps a fixed substring, `re.sub` swaps anything the
pattern describes.

- Because a quantified pattern matches a **run**, each run collapses to one
  replacement: `re.sub(r"\d+", "#", "a12b3")` is `"a#b#"`, not `"a##b#"`.
- No match leaves the text unchanged. An optional `count=` limits how many
  replacements are made.
- `repl` may reference captured groups with `\1`, `\2`, … (e.g.
  `re.sub(r"(\w+)@(\w+)", r"\2.\1", s)`), or be a **function** that receives each
  match and returns its replacement, for logic too complex for a template.

```python
import re

re.sub(r"\s+", " ", "too   many    spaces")   # 'too many spaces'
re.sub(r"\d+", "#", "call 555-1234")           # 'call #-#'
re.sub(r"(\d+)", r"[\1]", "x12")               # 'x[12]'
```
""",

"12.7 brief": r"""# 12.7 -- Anchors: match the whole string

## Concept

`re.search` is happy if the pattern appears **anywhere**. To **validate a
format**, you need the *entire* string to match -- no leftover characters.

Two ways to demand that:

- **Anchors** in the pattern: `^` ties to the **start**, `$` to the **end**, so
  `r"^[A-Z]{2}\d{4}$"` must span the whole string.
- **`re.fullmatch`**, which requires the pattern to cover the whole string for
  you -- no anchors needed.

```python
import re

re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234")     # matches
re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x")    # None -- trailing junk
re.search(r"[A-Z]{2}\d{4}", "AB1234x")       # matches -- search ignores the x
```

A product code here is two uppercase letters then four digits: `AB1234`.

## Example

```python
import re

def is_word(text):
    return re.fullmatch(r"[a-z]+", text) is not None
```

## Your task

Using **`re.fullmatch`** (or `^...$`), define `is_valid_code(text)` that returns
`True` only when `text` is exactly **two uppercase letters followed by four
digits** (e.g. `"AB1234"`), `False` otherwise.

## Done when

- `is_valid_code("AB1234")` is `True`.
- `is_valid_code("ab1234")`, `is_valid_code("AB123")`, `is_valid_code("AB1234x")`
  are all `False`.
- The whole string is matched (fullmatch or anchors), not a hand-written length
  check.
""",

"12.7 hints": r"""The pattern for the code is `r"[A-Z]{2}\d{4}"` -- two uppercase letters, then
four digits. The trick is making the WHOLE string match it.

---

`re.fullmatch(pattern, text)` requires the pattern to cover the entire string, so
trailing characters fail. Return whether it found a match with `is not None`.

---

import re


def is_valid_code(text):
    return re.fullmatch(r"[A-Z]{2}\d{4}", text) is not None
""",

"12.7 reference": r"""By default a pattern can match **anywhere** in the string. Validating a *format*
means the **whole** string must conform — no leftover characters. Two ways to
require that:

- **Anchors** in the pattern: **`^`** matches the start of the string, **`$`** the
  end. `r"^[A-Z]{2}\d{4}$"` must span the entire input.
- **`re.fullmatch(pattern, text)`** demands the pattern cover the whole string
  for you — no anchors needed. It returns a match object or `None`.

The contrast: `re.search(r"[A-Z]{2}\d{4}", "AB1234x")` **matches** (the pattern
occurs), but `re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x")` is **`None`** (the `x` is
left over). Use `search`/`findall` to *find* substrings, `fullmatch`/anchors to
*validate* a whole value.

```python
import re

bool(re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234"))    # True
bool(re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x"))   # False
bool(re.match(r"^\d{5}$", "12345"))               # True -- anchored form
```
""",

"12.8 brief": r"""# 12.8 -- Capstone: parse key=value config

## Concept

Time to combine the chapter's tools. When `re.findall` is given a pattern with
**several capture groups**, it returns a list of **tuples** -- one per match, the
captured pieces inside:

```python
import re

re.findall(r"(\w+)=(\w+)", "host=local port=8080")
# [('host', 'local'), ('port', '8080')]
```

A list of `(key, value)` pairs is exactly what **`dict(...)`** turns into a
dictionary. So one pattern plus `dict` parses a whole config string:

```python
dict(re.findall(r"(\w+)=(\w+)", "host=local port=8080"))
# {'host': 'local', 'port': '8080'}
```

`\w+` matches a run of word characters (letters, digits, underscore), so each key
and value is grabbed whole, and the `=` between them is matched literally.

## Your task

Define `parse_config(text)` that parses a space-separated string of `key=value`
pairs into a dict, using **`re.findall`** with two capture groups.

## Done when

- `parse_config("host=local port=8080")` equals
  `{"host": "local", "port": "8080"}`.
- `parse_config("debug=on")` equals `{"debug": "on"}`.
- `parse_config("")` equals `{}`.
- Pairs are captured with one `(\w+)=(\w+)` pattern, not split by hand.
""",

"12.8 hints": r"""Use two capture groups, one for the key and one for the value, with a literal `=`
between: `r"(\w+)=(\w+)"`.

---

With two groups, `re.findall(pattern, text)` returns a list of `(key, value)`
tuples. `dict(...)` of that list is the config dictionary.

---

import re


def parse_config(text):
    return dict(re.findall(r"(\w+)=(\w+)", text))
""",

"12.8 reference": r"""The capstone composes the chapter: a single pattern with **multiple capture
groups**, handed to **`re.findall`**, extracts structured records in one step.

- With more than one group, `re.findall` returns a list of **tuples** — one per
  match, holding each group's text: `re.findall(r"(\w+)=(\w+)", s)` yields
  `[(key, value), ...]`.
- A list of `(key, value)` pairs is exactly what **`dict(...)`** consumes, so
  `dict(re.findall(...))` is a complete mini-parser.
- `\w+` matches a run of word characters (letters, digits, underscore); the `=`
  between the groups is matched **literally**. No match gives `[]`, so an empty
  input cleanly yields `{}`.

This is the regex payoff: describe the shape of one record, and the engine finds
and dissects every occurrence for you.

```python
import re

dict(re.findall(r"(\w+)=(\w+)", "host=local port=8080"))
# {'host': 'local', 'port': '8080'}
```
""",
}
