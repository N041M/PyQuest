# PyQuest translations -- language 'example' -- chapter 01_basics -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply example

TRANSLATIONS = {

"1.1 brief": r"""# 1.1 -- Hello, output

## Concept

A **program** is a list of instructions the computer runs from top to bottom.
The most basic instruction is to **print** -- to put a line of text on the
screen. In Python you do that with `print(...)`. Whatever you put inside the
parentheses, in quotes, is shown.

`print` is a **function**: a built-in action you trigger by writing its name
followed by parentheses. The thing in quotes is **text** (Python calls text a
*string* -- a string of characters).

## Example

```python
print("Good morning")
```

When this runs, the screen shows:

```
Good morning
```

The quotes mark where the text starts and ends; they are not printed. Python
also adds a line break at the end automatically, so the next print starts on a
new line.

## Your task

Make the program print exactly this line:

```
Hello, output
```

Open the chapter workspace `work.py`, write one `print(...)` that produces that
line, **save the file**, then run `check`.

## Done when

- Running `check` shows CHECK PASSED.
- The output reads `Hello, output` -- same words, same comma. (The checker
  ignores capitalisation, but matching the brief exactly is good practice.)
""",

"1.1 hints": r"""Která vestavěná funkce vypíše text na obrazovku? Stačí jediný řádek.

---

Použij `print(...)`. Text patří dovnitř závorek, do dvojitých uvozovek:
`print("nějaký text")`. Dodrž přesné znění včetně čárky.

---

print("Hello, output")
""",

"1.1 reference": r"""`print` writes a textual representation of each argument to standard output (the
terminal), in order, and then writes `end` (a newline by default). It is the
primary way a program shows the user a result.

- Each value is converted to text with `str()` first, so `print(42)` and
  `print("42")` both show `42`.
- With several arguments, `sep` (default a single space) is placed *between*
  adjacent values — never before the first or after the last.
- `end` is appended once, after everything else. Because it defaults to `"\n"`,
  each `print` call ends the current line and the next output starts fresh.
- `print` returns `None`; it is called for its side effect, not its value.

```python
print("Hello, World!")        # Hello, World!
print("a", "b", "c")          # a b c
```
""",

"1.2 brief": r"""# 1.2 -- Printing more

## Concept

Two new ideas, both about `print`.

**1. Many prints run in order.** Each `print(...)` puts its text on its own line,
and Python runs them top to bottom. Three `print` lines make three output lines.

**2. One print can show several values.** Put several things inside the
parentheses separated by **commas**, and `print` shows them on one line with a
single space between each:

```python
print("a", "b", "c")
```

shows:

```
a b c
```

You can mix text and numbers this way. Numbers do **not** need quotes; text does.

## Example

```python
print("Scores:")
print(10, 20, 30)
```

shows:

```
Scores:
10 20 30
```

The first line is one print; the second print has three values separated by
commas, so they share a line with spaces between them.

## Your task

Produce exactly these two lines:

```
Counting:
1 2 3
```

Use two `print` statements: the first prints the word, the second prints the
three numbers `1`, `2`, `3` as separate values (let `print` add the spaces).

## Done when

- The output is exactly two lines: `Counting:` then `1 2 3`.
- The second line comes from numbers separated by commas, not from typing the
  text `"1 2 3"` yourself.
""",

"1.2 hints": r"""You need two print lines. The first prints a word; the second prints numbers.

---

In the second print, separate the numbers with commas: `print(1, 2, 3)`.
Let print put the spaces in -- don't type the spaces yourself.

---

print("Counting:")
print(1, 2, 3)
""",

"1.2 reference": r"""A program runs top to bottom, so successive `print` statements produce successive
lines — each call emits its arguments and then a newline.

Passing **several values to one `print`**, separated by commas, is different from
several `print` calls: the values appear on a *single* line, joined by `sep` (a
space by default). This is comma-separation in the call, not string concatenation
— the values keep their own types and are converted independently.

```python
print("one")
print("two")          # two lines

print("x", "y", 3)    # one line:  x y 3
```
""",

"1.3 brief": r"""# 1.3 -- Choosing the separator

## Concept

When you give `print` several values, it joins them with a space by default. You
can change that join string with a special setting called **`sep`** (short for
*separator*).

A setting like this is written `name=value` inside the parentheses, after your
values:

```python
print("a", "b", "c", sep="-")
```

shows:

```
a-b-c
```

`sep="-"` tells `print` to put a dash between values instead of a space. The
separator goes *between* values only -- not before the first or after the last.
You can use any text as the separator: `sep=", "`, `sep=""` (nothing), `sep="/"`,
and so on.

`sep` must be written exactly, with no space before the `=`, and the value in
quotes because it is text.

## Example

```python
print("home", "user", "docs", sep="/")
```

shows:

```
home/user/docs
```

## Your task

Print this exact date, using three **numbers** joined by dashes:

```
2024-12-25
```

Pass `2024`, `12`, `25` to a single `print` and set `sep` so they are joined with
`-`. Do not type the dashes as part of the text yourself.

## Done when

- The output is exactly `2024-12-25`.
- It comes from three numbers plus a `sep` setting, not from one typed string.
""",

"1.3 hints": r"""Give print the three numbers, then add a setting that changes the separator.

---

The setting is `sep`. After your three numbers, add `sep="-"` inside the same
print: `print(a, b, c, sep="-")`.

---

print(2024, 12, 25, sep="-")
""",

"1.3 reference": r"""`sep` and `end` are keyword-only arguments that control the spacing around a
`print`'s output.

- **`sep`** is the string inserted between each pair of adjacent values. The
  default is `" "`. It never appears before the first value or after the last,
  so *N* values produce *N − 1* separators.
- **`end`** is the string written once after the final value. The default is
  `"\n"`, which is why each `print` ends its line. Set `end=""` to leave the
  cursor on the same line so the next `print` continues it.

```python
print("2024", "01", "15", sep="-")   # 2024-01-15
print("loading", end="")
print("...")                          # loading... (one line)
```
""",

"1.4 brief": r"""# 1.4 -- Comments

## Concept

A **comment** is a note in your code that Python ignores. Anything after a `#` on
a line is skipped when the program runs. Comments are for humans -- to explain
what the code does.

```python
# This whole line is a note and does nothing.
print("Hi")   # Text after # on a code line is also ignored.
```

Only `print("Hi")` runs above. The two notes are skipped.

A second, very practical use: **commenting out** code. If you put a `#` in front
of a line of real code, that line stops running -- without deleting it. This is
how you switch a line off temporarily.

```python
# print("off")
print("on")
```

Only `on` is printed; the first line is now a comment.

## Common misconception

Putting `#` in front of a line does **not** delete it or cause an error -- the
line is simply not run. Remove the `#` and it runs again.

## Your task

The starter file already contains a line that prints `Hidden`. **Comment it out**
so it does not run -- do **not** delete it -- and add a line that prints
`Visible`.

The program must print only:

```
Visible
```

## Done when

- The output is exactly `Visible`.
- The `print("Hidden")` line is still in the file, but commented out with a `#`
  so it does not run. (This puzzle is about *commenting out*, so deleting the
  line does not count.)
""",

"1.4 hints": r"""A line starting with # is ignored. Put one in front of the Hidden line.

---

Change `print("Hidden")` to `# print("Hidden")`, then add `print("Visible")`
on its own line.

---

# print("Hidden")
print("Visible")
""",

"1.4 reference": r"""A `#` begins a **comment**: from the `#` to the end of that line, the text is
ignored by Python. Comments explain *why* code does something; they have no
effect on what runs.

- A comment may sit on its own line or follow code on the same line
  (`x = 1  # set up`).
- A `#` inside a string literal is just a character, not a comment
  (`"#1"` is the text `#1`).
- Python has **no block-comment syntax**: comment each line with `#`, or — for a
  throwaway block — use a string literal, which is evaluated and discarded.

"Commenting out" a line (putting `#` in front) is the quickest way to disable it
without deleting it.

```python
# this whole line is ignored
print("hi")   # and this trailing note is too
```
""",

"1.5 brief": r"""# 1.5 -- Storing a value

## Concept

A **variable** is a name that holds a value so you can use it later. You create
one with `=`, the **assignment** sign:

```python
score = 100
```

Read this as "let `score` be `100`." The name goes on the left, the value on the
right. After that line, writing `score` anywhere means `100`.

This is different from `==` (which you will meet later for comparing). A single
`=` *stores*.

Once stored, you can use the name as many times as you like:

```python
score = 100
print(score)
print(score)
```

shows:

```
100
100
```

Notice `print(score)` has **no quotes** around `score`. Quotes would make it the
literal text "score"; without quotes it means the variable's value, `100`.

## Naming rules (quick version)

A variable name can use letters, digits, and underscores, but cannot start with a
digit and cannot contain spaces. Use clear names: `total`, `user_name`, `count`.

## Your task

Store the number `42` in a variable, then print that variable **twice** so the
output is:

```
42
42
```

Use the variable both times -- do not type `42` inside the prints.

## Done when

- The output is `42` on two separate lines.
- Both lines come from printing your variable (no quotes around its name).
""",

"1.5 hints": r"""First make a variable with `=`, then print its name on two lines.

---

`n = 42` stores the value. Then `print(n)` twice. No quotes around n.

---

n = 42
print(n)
print(n)
""",

"1.5 reference": r"""Assignment with `=` binds a **name** to a value. Afterwards the name *refers to*
that value, and using the name anywhere evaluates to it. Reading code, `=` is
"becomes", not "equals" (equality is `==`).

- Names are not declared and have no fixed type — the first assignment creates
  the name, and it simply points at whatever object you assign.
- A name must start with a letter or underscore and contain letters, digits, or
  underscores; it is case-sensitive (`total` and `Total` are different).
- The right-hand side is fully evaluated first, then the result is bound to the
  name on the left.

```python
greeting = "Hello"
print(greeting)        # Hello  -- the name stands in for the value
```
""",

"1.6 brief": r"""# 1.6 -- Reassigning a variable

## Concept

A variable can be **changed** after it is created. Assigning to the same name
again replaces the old value with a new one. The name always refers to whatever
was stored **most recently**.

```python
x = 10
print(x)   # 10
x = 20
print(x)   # 20
```

The order matters: the program runs top to bottom, so the first `print(x)` sees
`10`, and only after the second assignment does `x` become `20`.

A common and useful pattern is updating a variable using its own current value:

```python
x = 10
x = x + 5   # take the current x (10), add 5, store 15 back in x
print(x)    # 15
```

The right side is worked out first (`10 + 5`), then the result is stored back
into `x`.

## Common misconception

Reassigning does not create a second variable. There is still just one `x`; its
stored value was swapped. The old value is simply gone.

## Your task

Create a variable holding `10` and print it. Then reassign that same variable to
`20` and print it again. The output must be:

```
10
20
```

## Done when

- The output is `10` then `20` on two lines.
- Both lines print the **same** variable, before and after you change it.
""",

"1.6 hints": r"""Print the variable, then assign a new value to the same name, then print again.

---

The order is: `x = 10`, `print(x)`, `x = 20`, `print(x)`.

---

x = 10
print(x)
x = 20
print(x)
""",

"1.6 reference": r"""A variable is a name, not a box: assigning again **rebinds** the name to a new
value. The name always holds its most recent assignment; the previous value is
simply no longer reachable through it.

- Each `=` replaces what the name points to. Order matters — later assignments
  win.
- The right-hand side is evaluated using the name's *current* value, then the
  result is rebound, so `x = x + 1` reads the old `x` and stores the new one.
- The augmented forms (`x += 1`, `x *= 2`, …) are shorthand for exactly that:
  read, combine, rebind.

```python
score = 10
score = 25        # score is now 25
score = score + 5 # reads 25, stores 30
```
""",

"1.7 brief": r"""# 1.7 -- Text vs number

## Concept

Python tells two kinds of values apart, and it matters a lot:

- A **number** like `5` -- written with no quotes. Python calls whole numbers
  `int` (integer).
- A **string** like `"5"` -- written with quotes. It is *text* that happens to
  look like a number. Python calls it `str`.

They behave differently with the `+` sign:

- With numbers, `+` **adds**: `5 + 5` is `10`.
- With strings, `+` **joins** (this is called **concatenation**):
  `"5" + "5"` is `"55"` -- the two pieces of text stuck together.

```python
print(5 + 5)        # 10   (numbers add)
print("5" + "5")    # 55   (text joins)
print("ab" + "cd")  # abcd
```

So `"5"` and `5` look the same on screen but are different types, and `+` treats
them in completely different ways.

## Common misconception

`"5"` is not the number five. The quotes make it text. You cannot do arithmetic
with it and expect addition -- `"5" + "5"` gives `"55"`, not `10`.

## Your task

Print these two lines, in this order:

```
55
10
```

- The first line must come from **joining two strings** `"5"` and `"5"` with `+`.
- The second line must come from **adding two numbers** `5` and `5` with `+`.

## Done when

- Output is `55` then `10`.
- Line one uses string concatenation; line two uses number addition.
""",

"1.7 hints": r"""Quotes decide everything here. With quotes, + joins; without quotes, + adds.

---

First line: `print("5" + "5")`. Second line: `print(5 + 5)`. Note the quotes
on the first and none on the second.

---

print("5" + "5")
print(5 + 5)
""",

"1.7 reference": r"""Every value has a **type**. Two fundamental ones appear immediately:

- a **string** (`str`) is text, written in quotes: `"42"`, `"hello"`;
- an **integer** (`int`) is a number, written as bare digits: `42`.

The quotes are the whole difference. `type("42")` is `str`; `type(42)` is `int`.

The type decides what an operator means. `+` between two **strings**
*concatenates* (joins) them; `+` between two **numbers** *adds* them:

```python
"2" + "2"   # "22"  -- text joined
 2  +  2    #  4    -- numbers added
```

Mixing the two with `+` is an error (`TypeError`), because Python won't guess
whether you meant to add or join. Convert explicitly first: `int("2") + 2` is
`4`, and `"$" + str(2)` is `"$2"`.
""",

"1.8 brief": r"""# 1.8 -- Arithmetic and order

## Concept

Python does math with these signs (called **operators**):

- `+` add
- `-` subtract
- `*` multiply
- `/` divide

```python
print(2 + 3)   # 5
print(10 - 4)  # 6
print(6 * 7)   # 42
```

**Order matters.** Just like in school maths, `*` and `/` happen **before**
`+` and `-`. So:

```python
print(2 + 3 * 4)   # 14, not 20  -- 3*4 first, then +2
```

To force a different order, wrap a part in **parentheses** `( )`. Whatever is
inside parentheses is worked out first:

```python
print((2 + 3) * 4)   # 20  -- 2+3 first, then *4
```

This is the single most common source of "wrong number" bugs, so it is worth
getting comfortable with now.

## Example

```python
print(1 + 2 * 3)     # 7
print((1 + 2) * 3)   # 9
```

## Your task

Print these two lines:

```
14
20
```

- The first line is `2 + 3 * 4` with no parentheses (multiplication first).
- The second line is the same numbers but with parentheses so the addition
  happens first: `(2 + 3) * 4`.

## Done when

- Output is `14` then `20`.
- The difference between the lines comes only from parentheses changing the
  order.
""",

"1.8 hints": r"""Multiplication runs before addition unless parentheses say otherwise.

---

First line: `print(2 + 3 * 4)`. Second line: add parentheses around 2 + 3:
`print((2 + 3) * 4)`.

---

print(2 + 3 * 4)
print((2 + 3) * 4)
""",

"1.8 reference": r"""The arithmetic operators are `+` (add), `-` (subtract), `*` (multiply),
`/` (divide), `//` (floor-divide), `%` (remainder), and `**` (power).

They follow **precedence** (order of operations), highest to lowest:

1. `**`
2. unary `-` (negation)
3. `*`, `/`, `//`, `%`
4. `+`, `-`

Operators of equal precedence evaluate **left to right**, except `**`, which is
right-associative (`2 ** 3 ** 2` is `2 ** 9`). **Parentheses** override all of
this — evaluate them first.

```python
2 + 3 * 4      # 14   -- * before +
(2 + 3) * 4    # 20   -- parentheses first
-3 ** 2        # -9   -- ** before unary minus
```
""",

"1.9 brief": r"""# 1.9 -- Three kinds of division

## Concept

Dividing has three useful operators in Python:

- `/`  normal division -- always gives a decimal number (Python calls these
  `float`). `7 / 2` is `3.5`.
- `//` floor division -- divides and throws away the fractional part, giving a
  whole number. `7 // 2` is `3`.
- `%`  modulo -- gives the **remainder** after division. `7 % 2` is `1`
  (because 2 goes into 7 three times with 1 left over).

```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
```

A number with a decimal point, like `3.5`, is a `float`. A whole number with no
point, like `3`, is an `int`. Notice `/` gives `3.5` even when it divides
evenly-looking numbers: `4 / 2` is `2.0`, not `2`.

`%` is surprisingly handy: a number is even exactly when `n % 2` is `0`.

## Common misconception

`/` does not round to a whole number. `7 / 2` is `3.5`, never `3`. If you want the
whole-number part, that is what `//` is for.

## Your task

Using the number 7 and 2, print these three lines in order:

```
3.5
3
1
```

Use `/` for the first, `//` for the second, and `%` for the third.

## Done when

- Output is exactly `3.5`, then `3`, then `1`.
- Each line uses the matching operator (`/`, `//`, `%`).
""",

"1.9 hints": r"""There are three division operators: /, //, and %. One per line.

---

`print(7 / 2)` gives 3.5, `print(7 // 2)` gives 3, `print(7 % 2)` gives 1.

---

print(7 / 2)
print(7 // 2)
print(7 % 2)
""",

"1.9 reference": r"""Python has three division operators:

- **`/` true division** always produces a **`float`**, even when the result is
  whole: `7 / 2 == 3.5`, and `4 / 2 == 2.0` (note the `.0`).
- **`//` floor division** divides and rounds *down* toward negative infinity,
  giving an `int` for two ints: `7 // 2 == 3`. With a negative operand it still
  rounds down, so `-7 // 2 == -4`, not `-3`.
- **`%` remainder (modulo)** is what's left over: `7 % 2 == 1`. In Python the
  result takes the **sign of the divisor**, so `-7 % 2 == 1`.

For any integers, `a == (a // b) * b + (a % b)` holds. `divmod(a, b)` returns the
pair `(a // b, a % b)` at once. Dividing by zero raises `ZeroDivisionError`.

```python
17 / 5    # 3.4
17 // 5   # 3
17 % 5    # 2   -- 3*5 + 2 == 17
```
""",

"1.10 brief": r"""# 1.10 -- Asking the user

## Concept

`input()` pauses the program, lets the person type a line, and **gives back what
they typed as text** (a string). You usually store that in a variable:

```python
name = input()
print("Hi, " + name)
```

If the person types `Sam`, the program prints `Hi, Sam`.

`input()` always returns a **string**, even if the person types digits. (You will
deal with that in the next puzzle.)

You can join the typed text with other text using `+`, exactly like in puzzle 1.7:

```python
city = input()
print("You live in " + city)
```

> Note: when you run `check`, the checker feeds the input for you automatically
> -- you do not type anything by hand.

## Example

Input typed: `Berlin`

```python
city = input()
print("Welcome to " + city)
```

Output:

```
Welcome to Berlin
```

## Your task

Read one line of input (a name) and greet it. If the input is `World`, the output
must be exactly:

```
Hello, World
```

So: read the name with `input()`, then print `Hello, ` joined with the name. Mind
the comma and the single space after it.

## Done when

- Given input `World`, output is `Hello, World`.
- Given any other name, it greets that name the same way (the checker tries
  more than one).
""",

"1.10 hints": r"""Store what input() returns in a variable, then build the greeting with +.

---

`name = input()` then `print("Hello, " + name)`. The text before the name
includes the comma and a space: "Hello, ".

---

name = input()
print("Hello, " + name)
""",

"1.10 reference": r"""`input` reads **one line** from standard input — everything the user types until
they press Enter — strips the trailing newline, and returns it as a **string**.

- The return value is *always* a `str`, even if the user typed digits:
  `input()` on `42` returns `"42"`, not `42`. To do arithmetic, convert it
  (see `int()`).
- The optional `prompt` argument is written to the screen first, without a
  trailing newline, so the user types on the same line.
- If the input stream ends with no line to read (end-of-file), `input` raises
  `EOFError`.

```python
name = input("Your name? ")   # prompts, then reads a line
print("Hi, " + name)
```
""",

"1.11 brief": r"""# 1.11 -- A number from input

## Concept

`input()` always gives back **text**, even when the person types digits. If you
try to do math on it, `+` will join instead of add -- remember puzzle 1.7:

```python
n = input()      # user types 21  ->  n is the string "21"
print(n + n)     # "2121", not 42
```

To do arithmetic, first **convert** the text to a number with `int(...)`:

```python
n = int(input())   # "21" -> 21, a real number now
print(n * 2)       # 42
```

`int(...)` takes text that looks like a whole number and turns it into an `int`
you can compute with. This pattern -- `int(input())` -- is extremely common.

## Common misconception

`int` does not just "remove the quotes"; it produces a different type. After
`int(input())` the value is a number, so `+`, `*`, `//`, and friends do real math.

## Your task

Read a whole number from input, then print **double** it. Examples:

- input `21` -> output `42`
- input `0`  -> output `0`
- input `-5` -> output `-10`

So: read with `input()`, convert with `int(...)`, multiply by 2, print the result.

## Done when

- For input `21` the output is `42`.
- It also works for `0` and for a negative number like `-5` (the checker tries
  these).
""",

"1.11 hints": r"""input() gives text. You must turn it into a number before doing math.

---

Wrap input in int: `n = int(input())`. Then `print(n * 2)`.

---

n = int(input())
print(n * 2)
""",

"1.11 reference": r"""`int` converts a value to an **integer**. Its most common use is turning the
**string** that `input()` returns into a number you can compute with.

- `int("42")` is `42`. Surrounding whitespace is ignored (`int(" 42 ")` works);
  a leading sign is allowed (`int("-5")`).
- Text that isn't a whole number raises `ValueError` — `int("3.5")` and
  `int("ten")` both fail. For decimals, use `float("3.5")`.
- Called on a `float`, `int` truncates *toward zero* (`int(3.9)` is `3`,
  `int(-3.9)` is `-3`).

Because `input()` always yields text, reading a number is a two-step idiom:

```python
n = int(input("How many? "))   # read text, then parse it to an int
print(n * 2)
```
""",
}
