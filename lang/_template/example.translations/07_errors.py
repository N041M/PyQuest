# PyQuest translations -- language 'example' -- chapter 07_errors -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply example

TRANSLATIONS = {

"7.1 brief": r"""# 7.1 -- try / except

## Concept

You have *caused* plenty of errors by now. Time to **handle** one.

When Python hits something impossible -- like `int("hello")` -- it **raises an
exception**: the normal flow stops dead and, unless someone deals with it, the
program crashes with a traceback. `try`/`except` is how you deal with it:

```python
try:
    n = int(text)
    print("a number!")
except ValueError:
    print("not a number")
```

How it runs:

- The `try` block runs normally -- **until** a line raises.
- If nothing raises, the `except` block is skipped entirely.
- If `int(text)` raises a `ValueError` (its complaint about unconvertible
  text), the rest of the `try` block is abandoned and the `except` block
  runs instead. **No crash.**

The program *recovers*: it chose what failure means instead of falling over.

## Example

Input `7` prints `14`. Input `seven` prints `not a number` -- the same code,
no crash either way.

## Your task

Read one line. If it converts to a whole number, print that number **doubled**.
If it doesn't, print exactly `not a number`. (This is a script puzzle again:
`input()` and `print()` are back.)

## Done when

- `7` prints `14`; `-3` prints `-6`.
- `seven` and `12abc` print `not a number` -- and the program exits cleanly,
  no traceback.
- You used `try`/`except` -- the checker requires the real thing.
""",

"7.1 hints": r"""int("seven") raises a ValueError -- put the conversion inside a try block.

---

try: convert and print the double. except ValueError: print the message.
The except block only runs when the conversion failed.

---

line = input()
try:
    n = int(line)
    print(n * 2)
except ValueError:
    print("not a number")
""",

"7.1 reference": r"""A **`try` / `except`** statement runs risky code and catches the error if it
fails, instead of letting the program crash. The `try` block holds the code that
might **raise**; the `except` block runs only if it does.

- If the `try` block succeeds, the `except` is skipped entirely.
- If a statement in `try` raises, the **rest of the `try` is abandoned** and
  control jumps to the matching `except`; the program then continues below.
- An uncaught error unwinds the whole program with a traceback — `except` is how
  you intervene.

```python
try:
    n = int(text)        # may raise ValueError
except ValueError:
    n = 0                # recover instead of crashing
```
""",

"7.2 brief": r"""# 7.2 -- Catch the RIGHT error

## Concept

`except` can name which error it handles -- and it should. Errors you did not
expect are **information**, and swallowing them hides bugs.

```python
try:
    n = int(text)
except ValueError:        # exactly the error int() raises for bad TEXT
    n = None
```

The tempting shortcut is a bare `except:` (or `except Exception:`) -- "catch
everything, can't crash!" But *everything* includes errors that mean **your
code is being misused**. `int([1, 2])` doesn't raise `ValueError` -- it raises
`TypeError` ("wrong kind of thing entirely"), and that one *should* crash
loudly so the caller's bug gets found, not papered over.

The rule: **catch exactly what you expect; let everything else escape.**

## Example

```python
safe_int("42")      # 42
safe_int("nope")    # None         (ValueError, handled)
safe_int([1, 2])    # TypeError!   (NOT handled -- a misuse, let it crash)
```

## Your task

Define `safe_int(text)` that returns `int(text)`, or `None` when the text
isn't a valid number. Catch **only** `ValueError` -- a `TypeError` from a
non-string must escape.

## Done when

- `safe_int("42")` is `42`; `safe_int("-7")` is `-7`.
- `safe_int("nope")` and `safe_int("")` are `None`.
- `safe_int([1, 2])` raises `TypeError` -- the checker calls it with a list
  on purpose, so catching too much fails.
""",

"7.2 hints": r"""return int(text) inside the try; the except returns None instead.

---

Name the error: `except ValueError:` -- naming nothing (or Exception) also
catches the TypeError the checker sends, and that must escape.

---

def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None
""",

"7.2 reference": r"""An `except` should name the **specific** exception you expect. Catching exactly
the right type lets unexpected errors surface as bugs instead of being silently
swallowed.

- `except ValueError:` catches only that type; an unrelated failure (a typo'd
  name raising `NameError`) still propagates, which is what you want.
- A bare `except:` (or `except Exception:`) catches **everything**, including bugs
  you'd rather see — avoid it unless you genuinely mean "any failure".
- Match the type to the operation: `int()` raises `ValueError`, indexing raises
  `IndexError`, dict lookup raises `KeyError`.

```python
try:
    value = data[key]
except KeyError:         # only a missing key, not other bugs
    value = None
```
""",

"7.3 brief": r"""# 7.3 -- ZeroDivisionError: ask forgiveness

## Concept

Dividing by zero raises `ZeroDivisionError`. There are two ways to write a
division that survives it:

```python
# "look before you leap": test first
if b == 0:
    return None
return a / b

# "easier to ask forgiveness": just try it
try:
    return a / b
except ZeroDivisionError:
    return None
```

Both behave the same *here* -- but Python style strongly favours the second,
and this puzzle requires it. Why:

- The `try` names the actual event ("the division failed") instead of a
  pre-condition you must keep in sync with it.
- Pre-checks don't scale: real operations can fail a dozen ways
  (file missing, permission denied, connection dropped...). You cannot
  pre-test them all -- but one `except` can catch the failure itself.

This style is called **EAFP**: *easier to ask forgiveness than permission*.

## Example

```python
safe_div(10, 4)    # 2.5
safe_div(5, 0)     # None  -- handled, no crash
```

## Your task

Define `safe_div(a, b)` that returns `a / b`, or `None` when `b` is zero --
using `try`/`except`, not an `if`.

## Done when

- `safe_div(10, 4)` is `2.5`; `safe_div(5, 0)` is `None`.
- `safe_div(0, 5)` is `0.0` -- zero on TOP is a fine division.
- You caught `ZeroDivisionError` -- an if-test dodges the lesson and fails.
""",

"7.3 hints": r"""Attempt the division inside try -- don't test b first.

---

`except ZeroDivisionError: return None` -- the early return (6.5) inside try
handles the happy path.

---

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
""",

"7.3 reference": r"""Dividing by zero raises **`ZeroDivisionError`**. Catching it demonstrates the
**EAFP** style — "easier to ask forgiveness than permission": attempt the
operation and handle the failure, rather than testing for every bad case first.

- `a / 0` and `a // 0` and `a % 0` all raise. Wrapping the division in `try`
  lets you supply a fallback when the divisor turns out to be zero.
- EAFP often reads cleaner than a guarding `if b != 0:` and avoids a race between
  the check and the use.

```python
try:
    rate = hits / total
except ZeroDivisionError:
    rate = 0.0           # no data yet -- sensible fallback
```
""",

"7.4 brief": r"""# 7.4 -- IndexError and safe access

## Concept

Indexing past the end of a list raises `IndexError`:

```python
items = ["a", "b"]
items[5]      # IndexError!
```

A "safe get" returns a fallback instead of crashing -- and it is another
place where *trying* beats *pre-testing*. Remember that negative indexes are
**valid** (2.2): `items[-1]` is the last item, `items[-2]` the one before.
A hand-written bounds check has to get `0 <= i`... no wait, `-len <= i <
len`... exactly right, in two directions. Or you just try it:

```python
try:
    return items[i]
except IndexError:
    return default
```

The `except` is correct *by definition* -- it fires precisely when Python
itself says the index is bad, negatives included.

## Example

```python
item_or(["a", "b"], 0, "?")     # "a"
item_or(["a", "b"], -1, "?")    # "b"   -- valid negative index
item_or(["a", "b"], 5, "?")     # "?"   -- out of range, fallback
```

## Your task

Define `item_or(items, i, default)` that returns `items[i]`, or `default`
when `i` is out of range -- using `try`/`except IndexError`.

## Done when

- `item_or(["a", "b"], 1, "?")` is `"b"`; index `5` gives `"?"`.
- `item_or(["a", "b"], -1, "?")` is `"b"` -- negatives that fit are valid.
- `item_or([], 0, "?")` is `"?"` -- an empty list has no valid index.
- You used `try`/`except` -- bounds arithmetic dodges the lesson and fails.
""",

"7.4 hints": r"""Just index it inside a try -- Python already knows exactly which indexes are
bad.

---

`except IndexError: return default` -- this gets negatives right for free,
which a hand-written bounds check usually doesn't.

---

def item_or(items, i, default):
    try:
        return items[i]
    except IndexError:
        return default
""",

"7.4 reference": r"""Indexing past the end of a list (or string) raises **`IndexError`**. Catching it
turns a risky lookup into a **safe access** that returns a fallback when the
position doesn't exist.

- `lst[i]` raises if `i >= len(lst)` (or `i < -len(lst)`); the `except` supplies a
  default instead of crashing.
- This is the EAFP counterpart to checking `if i < len(lst):` first — useful when
  the out-of-range case is normal rather than a bug.

```python
def get(lst, i, default=None):
    try:
        return lst[i]
    except IndexError:
        return default   # position absent -> fallback
```
""",

"7.5 brief": r"""# 7.5 -- raise: errors are yours too

## Concept

So far you have *caught* errors that Python raised. You can also **raise your
own** -- and good functions do, the moment they are handed something
senseless:

```python
def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

`raise` creates the error and throws it right there: the function stops, and
the caller gets the same treatment `int("nope")` gives them -- catchable with
`try`, loud if ignored.

Why raise instead of returning something like `None` or `-1`? Because a wrong
value travels: it gets stored, added, printed, and the crash (if any) happens
far from the real mistake. A raise pins the failure to the moment and the
message -- `ValueError("age cannot be negative")` says exactly what went
wrong, where it went wrong. Garbage in, **error** out -- never garbage out.

## Example

```python
checked_age(30)     # 30
checked_age(0)      # 0    -- zero is a fine age
checked_age(-1)     # ValueError: age cannot be negative
```

## Your task

Define `checked_age(age)` that returns the age unchanged -- but raises a
`ValueError` when it is negative. Give it a message saying what's wrong.

## Done when

- `checked_age(30)` returns `30`; `checked_age(0)` returns `0`.
- `checked_age(-1)` raises `ValueError`.
- You used `raise` -- the checker looks for the statement itself.
""",

"7.5 hints": r"""Guard first, return after: if the age is negative, raise; otherwise it's fine
as-is.

---

The guard is two lines:  if age < 0:  then
raise ValueError("age cannot be negative").

---

def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
""",

"7.5 reference": r"""**`raise`** triggers an exception **yourself**, stopping the function and
signalling that something is wrong. It lets your code reject bad input at the
point it's detected, the same way built-ins do.

- `raise ValueError("amount must be positive")` constructs an exception with a
  message and throws it; execution stops unless a `try` up the call chain catches
  it.
- Choose the type that fits: `ValueError` for a wrong value, `TypeError` for a
  wrong type. The message explains what was expected.
- Raising at the boundary (as input arrives) keeps the rest of the code able to
  trust its data.

```python
def withdraw(amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    ...
```
""",

"7.6 brief": r"""# 7.6 -- Ask again: the retry loop

## Concept

The classic use of `try`/`except` in a real program: **keep asking until the
input makes sense.** Combine a `while True` loop (3.7), `break` (3.11), and
the `except` from 7.1:

```python
while True:
    try:
        n = int(input())
        break              # got a good one -- leave the loop
    except ValueError:
        pass               # bad line -- silently go around again
```

The shape to internalise:

- the **happy path** ends in `break`;
- the **except** absorbs the failure and lets the loop retry;
- after the loop, `n` is guaranteed valid -- the code below can trust it.

(`pass` is Python's "do nothing" statement -- the except block must contain
*something*.)

## Example

For the input lines `cat`, `dog`, `21` the program ignores the first two and
prints `42`.

## Your task

Read lines until one converts to a whole number, then print that number
**doubled**. Bad lines produce no output at all.

## Done when

- `21` as the first line prints `42`.
- `cat`, `dog`, `21` also prints just `42` -- the garbage is silently retried.
- Negative numbers work.
- You used a loop and `try`/`except`.
""",

"7.6 hints": r"""while True around a try: convert-and-break; the except just goes around again.

---

except ValueError: pass  -- `pass` means "do nothing", which here means
"retry". Print AFTER the loop, where n is guaranteed good.

---

while True:
    try:
        n = int(input())
        break
    except ValueError:
        pass
print(n * 2)
""",

"7.6 reference": r"""The **retry loop** keeps asking until it gets a valid value. It combines a
`while True` with `try` / `except`: succeed and `break` out; fail and loop round
to ask again.

- The `try` attempts the parse/operation; a successful path ends with `break`,
  leaving the loop.
- The `except` handles the bad input (often just printing a hint and falling
  through), so the `while True` runs another pass.
- `while True` with no other exit relies on that `break` — the valid case is the
  only way out.

```python
while True:
    try:
        n = int(input("number: "))
        break                 # valid -> leave the loop
    except ValueError:
        print("not a number, try again")
```
""",

"7.7 brief": r"""# 7.7 -- Reading the error: except ... as e

## Concept

An exception is not just a signal -- it is an **object carrying a message**.
Catch it *into a variable* with `as`, and you can use that message:

```python
try:
    n = int(text)
except ValueError as e:
    print(e)
```

For `text = "5x"`, that prints Python's own diagnosis:

```
invalid literal for int() with base 10: '5x'
```

`e` is the error object; printing it shows its message. This is how real
programs log what actually went wrong instead of a vague "something failed" --
the difference between a bug report you can act on and one you can't.

(You don't write the message yourself here -- you *relay* the one Python
attached when it raised.)

## Example

Input `7` prints `7`. Input `5x` prints
`invalid literal for int() with base 10: '5x'`.

## Your task

Read one line. If it converts to a whole number, print the number. If it
doesn't, catch the `ValueError` **as `e`** and print `e` itself -- Python's
message, not your own.

## Done when

- `7` prints `7`.
- `5x` prints the exact `invalid literal ...: '5x'` message -- with the
  offending text quoted inside it.
- You did not type the message by hand (it must match for *any* input, which
  only printing `e` gets right).
""",

"7.7 hints": r"""The `as e` goes right in the except line:  except ValueError as e:

---

Inside the except block, just print(e) -- the object prints as its message.

---

line = input()
try:
    print(int(line))
except ValueError as e:
    print(e)
""",

"7.7 reference": r"""**`except ValueError as e:`** binds the caught exception **object** to a name, so
you can inspect it — most simply by printing it to show what went wrong.

- The exception object carries the detail; `str(e)` (or `print(e)`) yields its
  message. `type(e).__name__` gives the error's class name.
- The name `e` exists only inside the `except` block.
- One handler can catch a family by naming a base class: `except Exception as e:`
  binds any of its subclasses (use sparingly — broad catches hide bugs).

```python
try:
    int("xyz")
except ValueError as e:
    print("bad input:", e)    # bad input: invalid literal for int()...
```
""",

"7.8 brief": r"""# 7.8 -- Capstone: a robust calculator

## Concept

One `try` can have **several** `except` blocks -- one per kind of failure,
each choosing its own recovery:

```python
try:
    ...
except ValueError:
    print("bad number")
except ZeroDivisionError:
    print("cannot divide")
```

Whichever error is raised picks its matching block; the others are skipped.
This capstone wires the whole chapter into the classic exercise: a calculator
that **cannot be crashed** by its input. It also needs `split` (4.4),
indexing (2.1), `elif` (3.4), and `/` (1.9).

## Example

```
input "8 + 5"   ->  13
input "9 / 2"   ->  4.5
input "9 / 0"   ->  cannot divide
input "two * 3" ->  bad number
input "8 ? 5"   ->  unknown op
```

## Your task

Read one line of the form `<number> <op> <number>` (three parts separated by
spaces). For ops `+`, `-`, `*` print the whole-number result; for `/` print
the float result. Handle every failure:

- a part that isn't a whole number -> print `bad number`
- division by zero -> print `cannot divide`
- any other op symbol -> print `unknown op`

## Done when

- `8 + 5` -> `13`, `9 / 2` -> `4.5`, `3 * -2` -> `-6`.
- `9 / 0` -> `cannot divide`; `two * 3` -> `bad number`; `8 ? 5` ->
  `unknown op`.
- No input crashes it: each failure prints its own message via `except`
  blocks (and an `else`/`elif` for the unknown op).
""",

"7.8 hints": r"""split() the line into three parts; convert parts[0] and parts[2] inside the
try.

---

Stack the two excepts after one try: ValueError -> "bad number",
ZeroDivisionError -> "cannot divide". The op chain is if/elif/else, with else
printing "unknown op".

---

parts = input().split()
try:
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("unknown op")
except ValueError:
    print("bad number")
except ZeroDivisionError:
    print("cannot divide")
""",

"7.8 reference": r"""A single `try` can be followed by **several `except` clauses**, each handling a
different failure with its own response. They're tested top to bottom; the
**first** matching type runs, and the rest are skipped.

- This builds robust input handling: one `try` around the work, then an `except`
  per thing that can go wrong (`ValueError` for a bad number,
  `ZeroDivisionError` for `/0`), each giving a tailored message.
- Order from specific to general if types are related, since the first match
  wins.

```python
try:
    a, b = int(x), int(y)
    print(a / b)
except ValueError:
    print("please enter whole numbers")
except ZeroDivisionError:
    print("cannot divide by zero")
```
""",
}
