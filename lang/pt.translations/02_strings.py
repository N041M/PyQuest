# PyQuest translations -- language 'pt' -- chapter 02_strings -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"2.1 brief": r"""# 2.1 -- Indexing

## Concept

A string is a sequence of characters, and each character has a **position**
(called an *index*). Counting starts at **0**, not 1. So in the string `"cat"`:

```
character:  c  a  t
index:      0  1  2
```

You read a single character with square brackets: `s[index]`.

```python
word = "cat"
print(word[0])   # c
print(word[1])   # a
```

`word[0]` is the first character, because indexing starts at zero. This trips up
almost everyone at first: the "first" character lives at index 0.

## Example

```python
s = "python"
print(s[0])   # p
```

## Your task

Read a word with `input()`, then print only its **first** character.

For input `hello` the output is:

```
h
```

## Done when

- For `hello` it prints `h`.
- It works for any word, including a single-letter word (the checker tries a
  few).
""",

"2.1 hints": r"""Characters are numbered from 0. Square brackets read one of them: s[0].

---

Store the input first, then print index 0: `s = input()` then `print(s[0])`.

---

s = input()
print(s[0])
""",

"2.1 reference": r"""A string is an ordered sequence of characters, and `s[index]` reads the one at a
given position. Positions are **zero-based**: the first character is `s[0]`, the
second `s[1]`, and so on.

- The result is itself a one-character string (Python has no separate character
  type).
- An index at or past the length raises `IndexError`; for a string of length
  *n*, the valid positions are `0` through `n - 1`.
- Strings are **immutable** — indexing reads a character, but `s[0] = "x"` is an
  error. To change text you build a new string.

```python
word = "Python"
word[0]    # 'P'
word[3]    # 'h'
```
""",

"2.2 brief": r"""# 2.2 -- Negative indexing

## Concept

You can also count from the **end** of a string using negative indexes. `-1` is
the last character, `-2` the second-to-last, and so on.

```
character:   c   a   t
index:       0   1   2
from end:   -3  -2  -1
```

```python
word = "cat"
print(word[-1])   # t
print(word[-2])   # a
```

This is handy when you do not want to count the length: `s[-1]` is always the
last character, no matter how long the string is.

## Example

```python
s = "python"
print(s[-1])   # n
```

## Your task

Read a word, then print its **last** character.

For input `hello` the output is:

```
o
```

## Done when

- For `hello` it prints `o`.
- It works for a single-letter word too (`-1` points at that one character).
""",

"2.2 hints": r"""Negative indexes count from the end. -1 is the last character.

---

`s = input()` then `print(s[-1])`.

---

s = input()
print(s[-1])
""",

"2.2 reference": r"""A **negative** index counts from the end of the string: `s[-1]` is the last
character, `s[-2]` the second-to-last, and so on. It saves writing
`s[len(s) - 1]`.

- `s[-1]` and `s[len(s) - 1]` name the same character; the negative form just
  doesn't need the length.
- The valid negative range is `-1` down to `-len(s)`; going further (e.g.
  `s[-99]` on a short string) raises `IndexError`.
- `s[0]` is the first character; there is no `-0` (that's just `0`).

```python
word = "Python"
word[-1]   # 'n'
word[-2]   # 'o'
```
""",

"2.3 brief": r"""# 2.3 -- Slicing

## Concept

A **slice** takes a range of characters at once: `s[start:stop]`. It includes the
character at `start` and goes **up to but not including** `stop`. This is called
*half-open*: the stop index is not included.

```python
s = "python"
print(s[0:3])   # pyt   (indexes 0, 1, 2 -- not 3)
print(s[2:5])   # tho   (indexes 2, 3, 4)
```

Leave out `start` and it begins at 0; leave out `stop` and it runs to the end:

```python
print(s[:3])    # pyt   (same as s[0:3])
print(s[3:])    # hon   (from index 3 to the end)
```

Because the stop is not included, `s[0:3]` gives you exactly **3** characters.

## Example

```python
s = "rainbow"
print(s[0:4])   # rain
```

## Your task

Read a word, then print its **first three** characters.

For input `hello` the output is:

```
hel
```

## Done when

- For `hello` it prints `hel`.
- For a word shorter than three letters it prints the whole word -- slicing past
  the end is safe and does not error. The checker tries `hi`.
""",

"2.3 hints": r"""A slice s[start:stop] takes characters from start up to (but not including) stop.

---

The first three characters are s[0:3], or simply s[:3].

---

s = input()
print(s[:3])
""",

"2.3 reference": r"""A **slice** `s[start:stop]` returns a new string containing the characters from
position `start` up to **but not including** `stop` — a *half-open* range. The
length of the result is `stop - start` (when both are in range).

- `s[2:5]` gives the characters at indexes 2, 3, 4 — three characters.
- Either bound may be omitted: `s[:3]` starts at the beginning, `s[3:]` runs to
  the end, and `s[:]` copies the whole string.
- Slicing never raises for out-of-range bounds — it clamps. `s[:100]` on a short
  string just returns all of it.

```python
s = "Python"
s[0:3]    # 'Pyt'
s[:2]     # 'Py'
s[2:]     # 'thon'
```
""",

"2.4 brief": r"""# 2.4 -- Slicing the middle

## Concept

Slicing mixes happily with negative indexes, and slices never crash -- if a slice
is empty, you simply get the empty string `""`.

`s[1:-1]` means "from index 1 up to (but not including) the last character" -- in
other words, drop the first and last characters:

```python
s = "python"
print(s[1:-1])   # ytho
```

If the string is too short to have a middle, the slice is just empty:

```python
print("ab"[1:-1])   # (nothing -- an empty string)
print("a"[1:-1])    # (nothing)
```

No error. An empty slice is a normal, valid result.

## Common misconception

Going "out of range" with a slice does **not** crash, unlike indexing a single
character. `"hi"[5]` would be an error, but `"hi"[1:5]` is fine -- it just stops
at the end.

## Example

```python
s = "hello"
print(s[1:-1])   # ell
```

## Your task

Read a word, then print it **without its first and last characters**.

For input `hello` the output is:

```
ell
```

## Done when

- For `hello` it prints `ell`.
- For a 1- or 2-letter word it prints an empty line (no middle) and does not
  crash. The checker tries `ab` and `a`.
""",

"2.4 hints": r"""Index 1 is the second character; -1 is the last. Slice between them.

---

Use s[1:-1] to drop the first and last characters.

---

s = input()
print(s[1:-1])
""",

"2.4 reference": r"""Slice bounds can be **negative**, counting from the end, and the two styles mix
freely. `s[1:-1]` drops the first and last character — start at index 1, stop
just before the last.

- A slice whose start is at or past its stop is **empty**, not an error:
  `s[3:3]` and `s[5:2]` both give `""`.
- Out-of-range bounds are clamped, so slicing is forgiving where plain indexing
  raises: `s[1:99]` is fine.
- Because the stop is exclusive, `s[:-1]` removes exactly the last character and
  `s[1:]` removes the first.

```python
s = "Python"
s[1:-1]   # 'ytho'  -- both ends trimmed
s[2:2]    # ''      -- empty, not an error
```
""",

"2.5 brief": r"""# 2.5 -- Steps and reversing

## Concept

A slice can take a third number, the **step**: `s[start:stop:step]`. The step says
how many positions to move each time. A step of `2` takes every second character:

```python
s = "abcdef"
print(s[::2])   # ace   (every 2nd character)
```

A **negative** step walks backwards. The shortcut `s[::-1]` -- empty start, empty
stop, step `-1` -- reverses the whole string:

```python
s = "python"
print(s[::-1])   # nohtyp
```

`s[::-1]` is the standard Python way to reverse a string.

## Example

```python
print("hello"[::-1])   # olleh
```

## Your task

Read a word, then print it **reversed**.

For input `hello` the output is:

```
olleh
```

## Done when

- For `hello` it prints `olleh`.
- For a single letter, or a word that reads the same backwards (like `level`), it
  prints the word unchanged. The checker tries both.
""",

"2.5 hints": r"""A slice can have a step: s[start:stop:step]. A negative step goes backwards.

---

Reverse with the standard idiom: s[::-1].

---

s = input()
print(s[::-1])
""",

"2.5 reference": r"""A slice takes a third part, the **step**: `s[start:stop:step]` takes every
`step`-th character. The default step is 1.

- `s[::2]` takes every second character (indexes 0, 2, 4, …).
- A **negative** step walks backwards. `s[::-1]` is the idiomatic way to
  **reverse** a string; with a negative step the default start/stop flip to the
  end and the beginning.
- `s[::-2]` takes every second character, from the end toward the start.

```python
s = "Python"
s[::2]    # 'Pto'
s[::-1]   # 'nohtyP'  -- reversed
```
""",

"2.6 brief": r"""# 2.6 -- Length, joining, repeating

## Concept

Three everyday string tools:

- `len(s)` gives the **number of characters** in `s` (a number):
  ```python
  len("cat")    # 3
  ```
- `+` joins two strings (you met this in chapter 1):
  ```python
  "cat" + "!"   # "cat!"
  ```
- `*` with a number **repeats** a string:
  ```python
  "ab" * 3      # "ababab"
  "-" * 5       # "-----"
  ```

`len` returns a number, so you can do maths with it. `+` and `*` build new
strings.

## Example

```python
s = "hi"
print(len(s))    # 2
print(s + "!")   # hi!
print(s * 3)     # hihihi
```

## Your task

Read a word and print three lines:

1. the number of characters in the word
2. the word with an exclamation mark added on the end
3. the word repeated three times

For input `hi` the output is:

```
2
hi!
hihihi
```

## Done when

- For `hi` the three lines are `2`, `hi!`, `hihihi`.
- It also works for an empty input: `0`, `!`, and an empty line. The checker
  tries it.
""",

"2.6 hints": r"""len(s) is a number; + joins strings; * repeats them.

---

print(len(s)) for the count, print(s + "!") to append, print(s * 3) to repeat.

---

s = input()
print(len(s))
print(s + "!")
print(s * 3)
""",

"2.6 reference": r"""Three core string operations:

- **`len(s)`** returns the number of characters in `s` as an `int`; `len("")`
  is `0`.
- **`+` concatenates**: `"ab" + "cd"` is `"abcd"`. Both operands must be strings
  — `"n" + 5` raises `TypeError`; convert with `str(5)` first.
- **`*` repeats**: `s * n` (or `n * s`) joins `n` copies. `"ab" * 3` is
  `"ababab"`; `n <= 0` gives the empty string `""`.

All three produce **new** strings and leave the originals unchanged (strings are
immutable).

```python
s = "ab"
len(s)    # 2
s + "c"   # 'abc'
s * 3     # 'ababab'
```
""",

"2.7 brief": r"""# 2.7 -- Cleaning up text

## Concept

Strings come with **methods** -- actions you call with a dot after the string:
`s.method()`. Three common ones:

- `s.upper()` -> an UPPERCASE copy
- `s.lower()` -> a lowercase copy
- `s.strip()` -> a copy with spaces removed from **both ends** (not the middle)

```python
"Hello".upper()     # "HELLO"
"Hello".lower()     # "hello"
"  hi  ".strip()    # "hi"
```

Methods return a **new** string; they do not change the original. You can chain
them -- each one works on the result of the one before:

```python
"  Hi  ".strip().upper()   # "HI"
```

## Example

```python
s = "  python  "
print(s.strip().upper())   # PYTHON
```

## Your task

Read a line, remove any spaces around it, and print it in **uppercase**.

For input `  hello  ` the output is:

```
HELLO
```

## Done when

- For `  hello  ` it prints `HELLO`.
- Spaces in the middle stay; only the ends are trimmed. The checker also tries a
  line that is only spaces (the result is an empty line).
""",

"2.7 hints": r"""Methods are called with a dot: s.strip(), s.upper(). They return new strings.

---

Chain them: s.strip() removes the end spaces, .upper() capitalises the result.

---

s = input()
print(s.strip().upper())
""",

"2.7 reference": r"""Strings carry **methods** — functions called with the `s.method()` syntax that
compute from the string.

- **`.strip()`** returns the string with leading and trailing **whitespace**
  removed (spaces, tabs, newlines). `.lstrip()` / `.rstrip()` trim one side.
- **`.upper()`** / **`.lower()`** return the string with every letter in upper
  or lower case.

Because every method returns a **new** string (the original is never modified),
calls **chain**: each acts on the result of the previous.

```python
"  Hi  ".strip()            # 'Hi'
"Hi".upper()                # 'HI'
"  Hello  ".strip().lower() # 'hello'  -- trimmed, then lowered
```
""",

"2.8 brief": r"""# 2.8 -- Replacing and counting

## Concept

Two more string methods:

- `s.replace(old, new)` returns a copy of `s` with **every** occurrence of `old`
  swapped for `new`:
  ```python
  "banana".replace("a", "o")   # "bonono"
  ```
- `s.count(sub)` returns **how many times** `sub` appears (a number):
  ```python
  "banana".count("a")          # 3
  ```

If `old` is not present, `replace` returns the string unchanged; if `sub` is not
present, `count` returns `0`.

## Example

```python
s = "foo bar"
print(s.replace("o", "0"))   # f00 bar
print(s.count("o"))          # 2
```

## Your task

Read a line and print two lines:

1. the line with every letter `o` replaced by a zero `0`
2. how many `o`s were in the **original** line

For input `foobar` the output is:

```
f00bar
2
```

## Done when

- For `foobar` the lines are `f00bar` and `2`.
- For a line with no `o` it prints the line unchanged and `0`. The checker tries
  it.
""",

"2.8 hints": r"""replace swaps every match; count tells you how many matches there are.

---

print(s.replace("o", "0")) then print(s.count("o")).

---

s = input()
print(s.replace("o", "0"))
print(s.count("o"))
""",

"2.8 reference": r"""Two search-and-survey methods:

- **`s.replace(old, new)`** returns a new string with **every** non-overlapping
  occurrence of `old` swapped for `new`. It replaces all matches, not just the
  first; if `old` doesn't occur, the string comes back unchanged.
- **`s.count(sub)`** returns how many times `sub` appears, counting
  non-overlapping matches left to right. `"aaa".count("aa")` is `1`, not 2.

Both only read `s` and return new information; the original string is untouched.

```python
"a-b-c".replace("-", "_")   # 'a_b_c'  -- every match
"banana".count("a")          # 3
```
""",

"2.9 brief": r"""# 2.9 -- Finding a position

## Concept

`s.find(sub)` returns the **index** where `sub` first appears -- a number you can
then use for slicing. (If `sub` is not found, it returns `-1`.)

```python
s = "name=Sam"
i = s.find("=")    # 4
print(i)           # 4
print(s[i+1:])     # Sam   (everything after the "=")
```

So `find` locates a marker, and a slice extracts the part you want relative to it.
Here `s[i+1:]` means "from one past the `=` to the end".

## Example

```python
s = "color=blue"
i = s.find("=")
print(s[i+1:])     # blue
```

## Your task

Each input is a line shaped like `key=value` (with one `=`). Print just the
**value** -- everything after the `=`.

For input `color=blue` the output is:

```
blue
```

## Done when

- For `color=blue` it prints `blue`.
- For `x=1` it prints `1`; for `a=` it prints an empty line; for `k=a=b` it prints
  `a=b` (only the first `=` splits it). The checker tries these.
""",

"2.9 hints": r"""find tells you where the "=" is. Then slice from just after it.

---

i = s.find("=") gives the position; s[i+1:] is everything after it.

---

s = input()
i = s.find("=")
print(s[i+1:])
""",

"2.9 reference": r"""**`s.find(sub)`** returns the index of the **first** occurrence of `sub` in `s`,
or **`-1`** if it isn't found (it never raises). Pairing it with slicing extracts
the text around a marker.

- The returned index is where `sub` starts, so `s[:i]` is the part before it and
  `s[i + len(sub):]` the part after.
- Check for `-1` before using the result — `s.find` returning `-1` would
  otherwise slice from the end.
- `.index(sub)` is the same but **raises** `ValueError` when absent; use `.find`
  when "not present" is a normal case.

```python
s = "key=value"
i = s.find("=")     # 3
s[:i]               # 'key'
s[i + 1:]           # 'value'
```
""",

"2.10 brief": r"""# 2.10 -- f-strings

## Concept

An **f-string** lets you drop values straight into text. Put an `f` before the
opening quote, then write `{...}` wherever a value should go:

```python
name = "Sam"
print(f"Hello, {name}!")     # Hello, Sam!
```

Inside the `{}` you can put any expression, not just a plain variable -- it is
worked out and its result is placed in the text:

```python
word = "cat"
print(f"{word} has {len(word)} letters")    # cat has 3 letters
print(f"{word} reversed is {word[::-1]}")   # cat reversed is tac
```

f-strings are the clearest way to build text out of values -- much tidier than
joining pieces with `+`.

## Example

```python
s = "python"
print(f"{s} reversed is {s[::-1]}")   # python reversed is nohtyp
```

## Your task

Read a word, then print this exact sentence using an f-string:

```
WORD reversed is REVERSED
```

where `WORD` is the input and `REVERSED` is it backwards. For input `hello`:

```
hello reversed is olleh
```

## Done when

- For `hello` it prints `hello reversed is olleh`.
- It works for any word, including a single letter. The checker tries a few.
""",

"2.10 hints": r"""An f-string starts with f" and inserts values inside { }.

---

You can put an expression in the braces: f"{w} reversed is {w[::-1]}".

---

w = input()
print(f"{w} reversed is {w[::-1]}")
""",

"2.10 reference": r"""An **f-string** (formatted string literal) is a string prefixed with `f` in which
`{ }` holds a Python **expression**; the expression is evaluated and its value
inserted, converted to text.

- Any expression fits inside the braces: `f"{name}"`, `f"{a + b}"`,
  `f"{nums[0]}"`.
- A literal brace is written by doubling it: `f"{{literal}}"` shows `{literal}`.
- A format spec after a colon controls presentation, e.g. `f"{price:.2f}"` shows
  two decimal places and `f"{n:>5}"` right-aligns in a 5-wide field.

f-strings are the clearest way to build text from values, replacing chains of
`+` and `str()`.

```python
name, n = "Ada", 3
f"{name} solved {n} puzzles"   # 'Ada solved 3 puzzles'
f"{1/3:.2f}"                    # '0.33'
```
""",
}
