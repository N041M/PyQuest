# PyQuest translations -- language 'pt' -- chapter 13_datetime -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"13.1 brief": r"""# 13.1 -- date: a calendar day

## Concept

The **`datetime`** module models real calendar dates and clock times. Its
**`date`** type holds a single day -- year, month, day -- as one object:

```python
from datetime import date

d = date(2026, 6, 20)
d.year      # 2026
d.isoformat()   # '2026-06-20'
```

- `date(year, month, day)` builds the object and **validates** it: `date(2026,
  13, 1)` raises, because there is no month 13.
- `.isoformat()` renders it as the standard `YYYY-MM-DD` string, zero-padded.
- A `date` is far better than three loose integers: it knows the calendar, so it
  can compare, subtract, and format itself.

## Example

```python
from datetime import date

def new_year(year):
    return date(year, 1, 1).isoformat()
```

## Your task

Using **`date`** from `datetime`, define `iso(y, m, d)` that builds the date and
returns its `YYYY-MM-DD` string via `.isoformat()`.

## Done when

- `iso(2026, 6, 20)` returns `"2026-06-20"`.
- `iso(1999, 1, 5)` returns `"1999-01-05"` (note the zero-padding).
- The string comes from a `date` object's `.isoformat()`, not hand-formatting.
""",

"13.1 hints": r"""`from datetime import date`, then `date(y, m, d)` makes the object. It has an
`.isoformat()` method that returns the YYYY-MM-DD string.

---

Chain them: `date(y, m, d).isoformat()`. The zero-padding is handled for you.

---

from datetime import date


def iso(y, m, d):
    return date(y, m, d).isoformat()
""",

"13.1 reference": r"""The **`datetime`** module provides types for calendar dates and clock times. Its
**`date`** type holds one day as a single object: `date(year, month, day)`.

- The constructor **validates** the values against the real calendar —
  `date(2026, 2, 30)` raises `ValueError`, so an impossible date can't slip
  through.
- Attributes `.year`, `.month`, `.day` read the parts back; **`.isoformat()`**
  renders the standard `YYYY-MM-DD` string, always zero-padded.
- A `date` knows the calendar, so it can compare (`<`, `==`), subtract (13.5),
  and report its weekday (13.3) — things three loose integers or a hand-built
  string cannot. `date.today()` returns the current day.

```python
from datetime import date

d = date(2026, 6, 20)
d.month          # 6
d.isoformat()    # '2026-06-20'
date(2026, 1, 5).isoformat()   # '2026-01-05'  -- padded
```
""",

"13.2 brief": r"""# 13.2 -- fromisoformat: text to date

## Concept

Dates usually arrive as **text** -- from a file, a form, an API. **`date.from
isoformat`** parses a standard `YYYY-MM-DD` string into a real `date` object,
the inverse of `.isoformat()`:

```python
from datetime import date

d = date.fromisoformat("2026-06-20")
d.year      # 2026
d.month     # 6
d.day       # 20
```

- It returns a `date`, so you can then read `.year` / `.month` / `.day`, compare
  it, or do arithmetic -- everything a date can do.
- It expects the exact `YYYY-MM-DD` shape; a malformed string raises `ValueError`.

Parsing into a real date (rather than slicing the string yourself) means the
value is validated and ready for calendar work.

## Example

```python
from datetime import date

def month_of(text):
    return date.fromisoformat(text).month
```

## Your task

Using **`date.fromisoformat`**, define `parts(text)` that parses a `YYYY-MM-DD`
string and returns the tuple of integers `(year, month, day)` read from the date
object's attributes.

## Done when

- `parts("2026-06-20")` returns `(2026, 6, 20)`.
- `parts("1999-01-05")` returns `(1999, 1, 5)`.
- The values come from a parsed `date`'s attributes, not `text.split("-")`.
""",

"13.2 hints": r"""`date.fromisoformat(text)` turns the string into a date object. Store it in a
variable.

---

Read `d.year`, `d.month`, `d.day` off that object and return them as a tuple.

---

from datetime import date


def parts(text):
    d = date.fromisoformat(text)
    return (d.year, d.month, d.day)
""",

"13.2 reference": r"""**`date.fromisoformat(text)`** parses a standard `YYYY-MM-DD` string into a `date`
object — the inverse of `.isoformat()`. The result is a real date, so you can read
its attributes, compare it, or do arithmetic on it.

- It expects the exact ISO shape; a malformed or impossible string raises
  `ValueError`, which validates the input as a side effect.
- `.year`, `.month`, `.day` read the components back as integers.
- Parsing into a date (rather than slicing the text yourself) is the point: the
  value is checked and immediately ready for calendar work. For non-ISO layouts,
  `datetime.strptime` parses by an explicit format (13.7).

```python
from datetime import date

d = date.fromisoformat("2026-06-20")
(d.year, d.month, d.day)     # (2026, 6, 20)
d < date.fromisoformat("2026-12-31")   # True
```
""",

"13.3 brief": r"""# 13.3 -- weekday: which day of the week

## Concept

Given a date, what day of the week is it? Working that out by hand means knowing
leap years and every month's length. The `date` object already does -- ask it:

```python
from datetime import date

date(2026, 6, 20).weekday()     # 5  (Saturday)
```

- **`.weekday()`** returns an integer: **Monday is 0**, Tuesday 1, ... Sunday 6.
- (`.isoweekday()` is the same idea but Monday=1 .. Sunday=7.)

This is the kind of thing you let the library do: it encodes the real calendar,
so the answer is correct for any date, leap years and all.

## Example

```python
from datetime import date

def is_weekend(text):
    return date.fromisoformat(text).weekday() >= 5
```

## Your task

Define `weekday(text)` that takes a `YYYY-MM-DD` string and returns its day of
the week as an integer, **Monday=0 .. Sunday=6**, using the date object's
`.weekday()`.

## Done when

- `weekday("2026-06-20")` returns `5` (a Saturday).
- `weekday("2000-01-01")` returns `5`.
- The answer comes from `.weekday()` on a parsed `date`.
""",

"13.3 hints": r"""Parse the string into a date first with `date.fromisoformat(text)`. A date object
can tell you its weekday.

---

`.weekday()` returns 0 for Monday through 6 for Sunday. Call it on the parsed
date and return the result.

---

from datetime import date


def weekday(text):
    return date.fromisoformat(text).weekday()
""",

"13.3 reference": r"""**`date.weekday()`** returns the day of the week as an integer, **Monday = 0**
through **Sunday = 6**. Because a `date` encodes the real calendar — leap years,
varying month lengths — it computes this correctly for any date, which is exactly
the kind of work you delegate to the library rather than derive by hand.

- `.isoweekday()` is the same but **Monday = 1 .. Sunday = 7** (the ISO
  convention).
- A common use is `weekday() >= 5` to test for a weekend.
- The companion `.strftime("%A")` formats the weekday's **name**, but that's
  locale-dependent; the numeric `.weekday()` is stable everywhere.

```python
from datetime import date

date(2026, 6, 20).weekday()      # 5  (Saturday)
date(2026, 6, 22).weekday()      # 0  (Monday)
date(2026, 6, 20).weekday() >= 5 # True -- it's the weekend
```
""",

"13.4 brief": r"""# 13.4 -- timedelta: date arithmetic

## Concept

A **`timedelta`** is a **duration** -- a span of time. Add one to a date and you
get another date, with all the calendar messiness (month lengths, year rollover,
leap days) handled for you:

```python
from datetime import date, timedelta

date(2026, 6, 20) + timedelta(days=40)     # date(2026, 7, 30)
date(2026, 12, 25) + timedelta(days=10)    # date(2027, 1, 4)  -- crosses the year
```

- `timedelta(days=n)` is a duration of `n` days (it also takes `weeks=`,
  `hours=`, etc.). `n` may be **negative** to go backwards.
- `date + timedelta` gives a new `date`; `date - timedelta` goes the other way.
- This is why you never do date maths by hand: the library knows February has 29
  days in a leap year, and you don't have to.

## Example

```python
from datetime import date, timedelta

def tomorrow(text):
    return (date.fromisoformat(text) + timedelta(days=1)).isoformat()
```

## Your task

Define `add_days(text, n)` that takes a `YYYY-MM-DD` string and an integer `n`,
and returns the `YYYY-MM-DD` string for the date `n` days later (using
`timedelta`). `n` may be negative.

## Done when

- `add_days("2026-06-20", 40)` returns `"2026-07-30"`.
- `add_days("2026-01-01", -1)` returns `"2025-12-31"`.
- The shift uses `timedelta` on a real `date`, not hand-rolled day counting.
""",

"13.4 hints": r"""Import both `date` and `timedelta`. Parse the text, then add
`timedelta(days=n)` to the date.

---

`date.fromisoformat(text) + timedelta(days=n)` gives a new date; call
`.isoformat()` on it for the string. Negative `n` just works.

---

from datetime import date, timedelta


def add_days(text, n):
    return (date.fromisoformat(text) + timedelta(days=n)).isoformat()
""",

"13.4 reference": r"""A **`timedelta`** represents a **duration** — a span of time, not a point in it.
Adding one to a `date` produces another `date`, with all the calendar bookkeeping
(month lengths, year boundaries, leap days) handled automatically.

- `timedelta(days=n)` is `n` days; it also accepts `weeks=`, `hours=`,
  `minutes=`, `seconds=`. `n` may be **negative** to move backwards.
- `date + timedelta` and `date - timedelta` give a new date; subtracting two
  *dates* gives a `timedelta` (13.5).
- This is why date arithmetic goes through the library: `date(2026, 12, 25) +
  timedelta(days=10)` correctly rolls into the next year, and February's length
  is never your problem.

```python
from datetime import date, timedelta

date(2026, 6, 20) + timedelta(days=40)    # date(2026, 7, 30)
date(2026, 1, 1) - timedelta(days=1)      # date(2025, 12, 31)
date(2026, 6, 20) + timedelta(weeks=2)    # date(2026, 7, 4)
```
""",

"13.5 brief": r"""# 13.5 -- Subtracting dates: days between

## Concept

Adding a duration to a date gives a date. The reverse also works: **subtract one
date from another** and you get a **`timedelta`** -- the span between them:

```python
from datetime import date

gap = date(2026, 7, 1) - date(2026, 6, 20)
gap            # timedelta(days=11)
gap.days       # 11
```

- `date_b - date_a` is a `timedelta`; its **`.days`** is the whole number of days
  between them.
- If `date_b` is **earlier** than `date_a`, `.days` is **negative**.
- It's exact across months, years and leap days -- the library counts, you don't.

## Example

```python
from datetime import date

def days_old(born, today):
    return (date.fromisoformat(today) - date.fromisoformat(born)).days
```

## Your task

Define `days_between(a, b)` that takes two `YYYY-MM-DD` strings and returns the
number of days **from `a` to `b`** (so later `b` gives a positive number), using
date subtraction.

## Done when

- `days_between("2026-06-20", "2026-07-01")` returns `11`.
- `days_between("2026-07-01", "2026-06-20")` returns `-11`.
- `days_between("2026-06-20", "2026-06-20")` returns `0`.
- The count comes from subtracting two `date` objects, not manual arithmetic.
""",

"13.5 hints": r"""Parse both strings into dates, then subtract them. `date_b - date_a` is a
timedelta.

---

A timedelta has a `.days` attribute. For "from a to b", subtract `a` from `b`:
`(date.fromisoformat(b) - date.fromisoformat(a)).days`.

---

from datetime import date


def days_between(a, b):
    return (date.fromisoformat(b) - date.fromisoformat(a)).days
""",

"13.5 reference": r"""Subtracting one `date` from another yields a **`timedelta`** — the span between
them — and its **`.days`** attribute is the whole number of days, computed exactly
across months, years, and leap days.

- `date_b - date_a` measures from `a` to `b`: if `b` is **earlier**, `.days` is
  **negative**, so the sign tells you the direction.
- The result is a duration, so it composes: add it back to a date, multiply it,
  compare two spans.
- This is the counting counterpart to adding a `timedelta` (13.4) — together they
  make dates a small algebra: `date + duration = date`, `date - date = duration`.

```python
from datetime import date

(date(2026, 7, 1) - date(2026, 6, 20)).days     # 11
(date(2026, 6, 20) - date(2026, 7, 1)).days     # -11
(date(2026, 3, 1) - date(2024, 3, 1)).days      # 730  -- 2024 was a leap year
```
""",

"13.6 brief": r"""# 13.6 -- strftime: format a date your way

## Concept

`.isoformat()` always gives `YYYY-MM-DD`. When you need a different layout,
**`strftime`** ("string format time") renders a date using **format codes**:

```python
from datetime import date

d = date(2026, 6, 20)
d.strftime("%d/%m/%Y")     # '20/06/2026'
d.strftime("%Y.%m.%d")     # '2026.06.20'
```

- `%d` is the day, `%m` the month, `%Y` the four-digit year -- each zero-padded.
  Everything else in the format string (the `/`, `.`, spaces) is copied through
  literally.
- Other codes exist (`%H` hour, `%M` minute, and name codes like `%A`), but the
  numeric ones are the staples.

So one date object can present itself however a report or user expects.

## Example

```python
from datetime import date

def dotted(text):
    return date.fromisoformat(text).strftime("%Y.%m.%d")
```

## Your task

Define `pretty(text)` that takes a `YYYY-MM-DD` string and returns it in
**`DD/MM/YYYY`** form, using `strftime("%d/%m/%Y")` on the parsed date.

## Done when

- `pretty("2026-06-20")` returns `"20/06/2026"`.
- `pretty("1999-01-05")` returns `"05/01/1999"` (zero-padded).
- The formatting is done by `strftime`, not by rearranging split pieces.
""",

"13.6 hints": r"""Parse the date with `date.fromisoformat(text)`, then call `.strftime(...)` on it
with the layout you want.

---

The format string for DD/MM/YYYY is `"%d/%m/%Y"`. The slashes are copied through
literally; the codes fill in the padded numbers.

---

from datetime import date


def pretty(text):
    return date.fromisoformat(text).strftime("%d/%m/%Y")
""",

"13.6 reference": r"""**`strftime(format)`** ("string-format-time") renders a date or datetime into a
string you describe with **format codes**. Where `.isoformat()` gives one fixed
layout, `strftime` gives any layout.

- Common codes: `%Y` four-digit year, `%m` month, `%d` day — all zero-padded;
  `%H` hour, `%M` minute, `%S` second. Any other characters (`/`, `.`, spaces)
  are copied through literally.
- Name codes like `%A` (weekday) and `%B` (month) are **locale-dependent**, so
  prefer the numeric codes for output that must be stable.
- `strptime` is the inverse — it *parses* a string by a format (13.7).

```python
from datetime import date

d = date(2026, 6, 20)
d.strftime("%d/%m/%Y")     # '20/06/2026'
d.strftime("%Y%m%d")       # '20260620'
d.strftime("%d.%m.%y")     # '20.06.26'  -- %y is the 2-digit year
```
""",

"13.7 brief": r"""# 13.7 -- strptime: parse by a format

## Concept

`date.fromisoformat` only reads the one ISO layout. For **any** layout -- a date
with a time, a custom order -- use **`datetime.strptime`** ("parse time"). You
give it the string **and** a format describing it, with the same codes as
`strftime`:

```python
from datetime import datetime

dt = datetime.strptime("2026-06-20 14:30", "%Y-%m-%d %H:%M")
dt.year     # 2026
dt.hour     # 14
dt.minute   # 30
```

- The format must match the string's shape; a mismatch raises `ValueError`, so
  it validates as it parses.
- The result is a **`datetime`** -- a date *and* a time -- with `.year`,
  `.month`, `.day`, `.hour`, `.minute`, `.second` attributes.

`strptime` parses, `strftime` formats: same codes, opposite directions.

## Example

```python
from datetime import datetime

def year_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").year
```

## Your task

Define `hour_of(text)` that takes a timestamp like `"2026-06-20 14:30"` and
returns the **hour** as an integer, by parsing it with `datetime.strptime` and
the format `"%Y-%m-%d %H:%M"`.

## Done when

- `hour_of("2026-06-20 14:30")` returns `14`.
- `hour_of("1999-01-05 09:05")` returns `9`.
- The hour comes from a parsed `datetime`, not string slicing.
""",

"13.7 hints": r"""`datetime.strptime(text, format)` parses the string. The format mirrors the
timestamp: `"%Y-%m-%d %H:%M"`.

---

The parsed object is a datetime with a `.hour` attribute. Return that.

---

from datetime import datetime


def hour_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").hour
""",

"13.7 reference": r"""**`datetime.strptime(text, format)`** parses a string into a **`datetime`** using
the same format codes as `strftime` — it's the inverse direction. Where
`date.fromisoformat` reads only the one ISO layout, `strptime` reads **any**
layout you can describe.

- The `format` must match the string's shape exactly (`"%Y-%m-%d %H:%M"` for
  `"2026-06-20 14:30"`); a mismatch raises `ValueError`, validating as it parses.
- The result is a `datetime` — a date **and** a time — exposing `.year`,
  `.month`, `.day`, `.hour`, `.minute`, `.second`. (`.date()` and `.time()`
  extract just one part.)
- Remember the pair: **strptime** parses (string → datetime), **strftime**
  formats (datetime → string).

```python
from datetime import datetime

dt = datetime.strptime("2026-06-20 14:30", "%Y-%m-%d %H:%M")
dt.hour                      # 14
datetime.strptime("05/01/1999", "%d/%m/%Y").year   # 1999
```
""",

"13.8 brief": r"""# 13.8 -- Capstone: shift a timestamp

## Concept

This pulls the chapter together into one round trip: **parse** a timestamp,
**shift** it by a duration, **format** the result back -- each step a tool you've
met.

```python
from datetime import datetime, timedelta

dt = datetime.strptime("2026-06-20 23:30", "%Y-%m-%d %H:%M")  # parse
dt = dt + timedelta(hours=2)                                  # shift
dt.strftime("%Y-%m-%d %H:%M")                                 # '2026-06-21 01:30'
```

Notice the shift rolled past midnight into the next day -- the library tracks
that automatically, across days, months and years. Doing this by hand would mean
reimplementing the calendar and the clock.

## Your task

Define `add_hours(timestamp, hours)` that takes a `"YYYY-MM-DD HH:MM"` string and
an integer number of `hours` (which may be negative), and returns the timestamp
shifted by that many hours, in the **same `"YYYY-MM-DD HH:MM"` format**.

Use `datetime.strptime` to parse, `timedelta(hours=...)` to shift, and
`strftime` to format.

## Done when

- `add_hours("2026-06-20 23:30", 2)` returns `"2026-06-21 01:30"`.
- `add_hours("2026-01-01 00:30", -1)` returns `"2025-12-31 23:30"`.
- The shift uses `timedelta` on a parsed `datetime`, formatted with `strftime` --
  not hand arithmetic on the string.
""",

"13.8 hints": r"""Three steps, three tools: `datetime.strptime(timestamp, "%Y-%m-%d %H:%M")` to
parse, `+ timedelta(hours=hours)` to shift, `.strftime("%Y-%m-%d %H:%M")` to
format.

---

Import `datetime` and `timedelta`. Parse into a datetime, add the timedelta, then
return the strftime of the result. Negative hours work the same way.

---

from datetime import datetime, timedelta


def add_hours(timestamp, hours):
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    dt = dt + timedelta(hours=hours)
    return dt.strftime("%Y-%m-%d %H:%M")
""",

"13.8 reference": r"""The capstone is the full **round trip** through the module, composing three of its
tools:

1. **Parse** — `datetime.strptime(timestamp, "%Y-%m-%d %H:%M")` reads the string
   into a `datetime`.
2. **Shift** — adding `timedelta(hours=h)` moves it by a duration, rolling across
   minutes, days, months, and years automatically (and backwards for negative
   `h`).
3. **Format** — `.strftime("%Y-%m-%d %H:%M")` renders the result back to the same
   layout.

The point of the chapter in one function: every awkward edge — a time crossing
midnight, a day crossing into a new month or year, a leap day — is handled by the
`datetime` types, not by you. You describe the steps; the library keeps the
calendar honest.

```python
from datetime import datetime, timedelta

def add_hours(timestamp, hours):
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    return (dt + timedelta(hours=hours)).strftime("%Y-%m-%d %H:%M")

add_hours("2026-06-20 23:30", 2)    # '2026-06-21 01:30'
```
""",
}
