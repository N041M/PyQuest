# PyQuest translations -- EXAMPLE (a complete, real file).
#
# Every translatable piece is one entry in TRANSLATIONS below: the pack name,
# every UI string, and every puzzle's brief/hints/reference. Each value starts as
# the English; change it to your language and `apply` writes it, leave it to keep
# English. A FEW values here are translated to Czech as a demo (the name, the UI
# strings, and "1.1 hints"); the rest are still English, showing where you edit.
#
# Generate your own with: python3 tools/lang_worksheet.py new <code>
#
# Keep each value's markdown and ``` code blocks exactly -- only the prose is
# localized (note print("Hello, output") stays English in "1.1 hints": it is the
# literal the grader checks). Pure data: read with ast.literal_eval, never run.

TRANSLATIONS = {

"name": "Čeština",

"ui menu.learn": "učit se",

"ui menu.play": "hrát",

"ui menu.setup": "nastavit",

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

"3.1 brief": r"""# 3.1 -- Booleans and comparison

## Concept

A **boolean** is a value that is either `True` or `False` -- a yes/no answer.
It is its own type (`bool`), written with a capital letter.

You get booleans by **comparing** values:

| operator | means |
|---|---|
| `==` | equal to |
| `!=` | not equal to |
| `<`  | less than |
| `>`  | greater than |
| `<=` | less than or equal |
| `>=` | greater than or equal |

```python
print(3 < 5)      # True
print(3 == 5)     # False
print(7 >= 7)     # True
```

Note `==` (compare) is **two** equals signs. A single `=` *assigns* a variable;
`==` *asks "are these equal?"*.

## Example

```python
a = 4
b = 9
print(a > b)      # False
```

## Your task

Read two whole numbers (each on its own line). Print whether the **first is
greater than the second** -- that is, print the result of `first > second`
(which will be `True` or `False`).

For input `8` then `3`, the output is:

```
True
```

## Done when

- For `8` then `3` it prints `True`; for `2` then `5` it prints `False`.
- When the two numbers are equal it prints `False` (equal is not "greater").
""",

"3.1 hints": r"""A comparison like a > b is already True or False -- you can print it directly.

---

Read both numbers as ints, then print the comparison:
`print(first > second)`.

---

a = int(input())
b = int(input())
print(a > b)
""",

"3.1 reference": r"""A **boolean** is one of two values, `True` or `False` (type `bool`). The
**comparison operators** produce one by comparing two values:

- `==` equal, `!=` not equal,
- `<` less than, `>` greater than, `<=` at most, `>=` at least.

`==` (a question, "are these equal?") is not `=` (a command, "assign"). Numbers
compare by value; strings compare **lexicographically** (dictionary order, by
character code, so uppercase sorts before lowercase). Comparisons can be
**chained**: `0 <= x < 10` means `0 <= x and x < 10`.

```python
3 < 5        # True
3 == 3.0     # True   -- equal values, different types
"a" < "b"    # True
```
""",

"3.2 brief": r"""# 3.2 -- if

## Concept

An **`if` statement** runs a block of code **only when** a condition is `True`:

```python
if condition:
    do_something()
    do_more()
```

Two things to notice:

1. The line ends with a **colon** `:`.
2. The lines that should run when the condition is true are **indented** (use 4
   spaces). The indentation is how Python knows which lines belong to the `if`.
   When the condition is `False`, the indented lines are skipped.

```python
age = 20
if age >= 18:
    print("adult")     # runs only when age >= 18
```

If `age` were `15`, nothing would print.

## Common misconception

Indentation is not decoration in Python -- it defines the block. Forgetting to
indent (or mixing spaces) is a syntax error.

## Your task

Read a whole number. **If it is negative**, print `negative`. If it is not
negative, print nothing at all.

For input `-4` the output is:

```
negative
```

For input `7` there is no output.

## Done when

- A negative number prints `negative`.
- Zero and positive numbers print nothing (`0` is not negative).
""",

"3.2 hints": r"""A number is negative when it is less than 0:  n < 0.

---

Write `if n < 0:` then, on the next line, an indented `print("negative")`.

---

n = int(input())
if n < 0:
    print("negative")
""",

"3.2 reference": r"""An **`if`** statement runs an indented block **only when** its condition is true.
The condition is evaluated to a boolean; if true, the block runs; if false, it is
skipped and the program continues below.

- The block is defined by **indentation** (conventionally 4 spaces). Every line
  indented under the `if` belongs to it; the first line back at the outer level
  ends it.
- The condition need not be a literal `True`/`False` — any value is tested for
  **truthiness**: `0`, `0.0`, `""`, and empty collections are falsy; everything
  else is truthy.

```python
if temperature > 30:
    print("hot")        # runs only when the test is True
print("done")           # always runs -- not indented under the if
```
""",

"3.3 brief": r"""# 3.3 -- if / else

## Concept

`else` gives an `if` a second branch: code to run when the condition is
**False**. Exactly one of the two blocks runs.

```python
if temperature > 30:
    print("hot")
else:
    print("not hot")
```

The `else:` lines up with the `if` (same indentation), and its block is indented
just like the `if` block.

## A reminder

`n % 2` is the remainder when `n` is divided by 2 (you met `%` in chapter 1). A
number is **even** exactly when `n % 2 == 0`.

## Example

```python
n = 7
if n % 2 == 0:
    print("even")
else:
    print("odd")
# prints: odd
```

## Your task

Read a whole number and print `even` if it is even, or `odd` if it is not.

For input `10` the output is:

```
even
```

## Done when

- Even numbers print `even`, odd numbers print `odd`.
- It works for `0` (even) and for negative numbers too.
""",

"3.3 hints": r"""Even means the remainder after dividing by 2 is zero:  n % 2 == 0.

---

Use if/else: if `n % 2 == 0` print "even", else print "odd".

---

n = int(input())
if n % 2 == 0:
    print("even")
else:
    print("odd")
""",

"3.3 reference": r"""An **`else`** clause gives an `if` a second branch: its block runs exactly when
the `if` condition is **false**. Together they are a two-way choice — one branch
or the other always runs, never both.

- `else` takes no condition; it is the catch-all for "the `if` was false".
- It must pair with an `if` at the same indentation, and its block is indented
  the same way.

```python
if n % 2 == 0:
    print("even")
else:
    print("odd")        # runs only when n % 2 == 0 is False
```
""",

"3.4 brief": r"""# 3.4 -- elif

## Concept

`elif` (short for "else if") adds **more branches** between `if` and `else`.
Python checks each condition in order and runs the **first** one that is `True`;
the rest are skipped. `else` (optional) catches everything left over.

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

Order matters: because the first true branch wins, you usually go from the most
specific or highest condition downward.

## Example

```python
n = 0
if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")
# prints: zero
```

## Your task

Read a whole number and print exactly one of:

- `negative` if it is less than 0,
- `zero` if it is 0,
- `positive` if it is greater than 0.

For input `0` the output is:

```
zero
```

## Done when

- `-3` prints `negative`, `0` prints `zero`, `5` prints `positive`.
- Exactly one line is printed for any input.
""",

"3.4 hints": r"""Three cases means if ... elif ... else.

---

`if n < 0:` -> negative; `elif n == 0:` -> zero; `else:` -> positive.

---

n = int(input())
if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")
""",

"3.4 reference": r"""**`elif`** ("else if") adds more branches between `if` and `else`. Python checks
each condition **in order** and runs the block of the **first** one that is true,
then skips the rest. An optional final `else` handles "none matched".

- Only one branch ever runs — the first true one. Later conditions aren't even
  evaluated.
- Because the first match wins, order matters: put the more specific or
  higher-priority tests first.
- An `elif` chain is flatter and clearer than nesting an `if` inside each
  `else`.

```python
if score >= 90:
    grade = "A"
elif score >= 80:       # only checked if the first was False
    grade = "B"
else:
    grade = "C"
```
""",

"3.5 brief": r"""# 3.5 -- and / or / not

## Concept

You can combine booleans with three words:

- `and` -- True only if **both** sides are True.
- `or` -- True if **either** side is True.
- `not` -- flips a boolean: `not True` is `False`.

```python
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

age = 25
print(age >= 18 and age < 65)   # True  (both hold)
```

These let one condition test several things at once.

## Example

```python
n = 12
print(n % 2 == 0 and n % 3 == 0)   # True  (12 is divisible by both)
```

## Your task

Read a whole number. Print whether it is divisible by **both** 2 and 3 -- that
is, print the result of `(n % 2 == 0) and (n % 3 == 0)` (which is `True` or
`False`).

For input `12` the output is:

```
True
```

## Done when

- `12` and `6` print `True`; `4` and `9` print `False`.
- `0` prints `True` (0 is divisible by everything).
""",

"3.5 hints": r""""Divisible by 2" is n % 2 == 0. You need that AND the same for 3.

---

Join the two checks with `and`, and print the whole thing:
`print(n % 2 == 0 and n % 3 == 0)`.

---

n = int(input())
print(n % 2 == 0 and n % 3 == 0)
""",

"3.5 reference": r"""The **boolean operators** combine conditions:

- **`and`** is true only when **both** sides are true.
- **`or`** is true when **at least one** side is true.
- **`not`** inverts a single value.

They **short-circuit**: `and` stops at the first false operand, `or` at the first
true one, so the right side isn't evaluated when the left already decides the
result. Precedence is `not` > `and` > `or`; parentheses make intent obvious.

```python
0 < x and x < 100      # True only inside the range
done or out_of_time    # True if either holds
not finished           # flips the flag
```
""",

"3.6 brief": r"""# 3.6 -- Nested conditions

## Concept

An `if` block can contain **another** `if`. This is called **nesting**. The inner
check only happens when the outer condition is already true. Each level is
indented one step further.

```python
if logged_in:
    if is_admin:
        print("admin panel")
    else:
        print("user page")
else:
    print("please log in")
```

Here `is_admin` is only checked when `logged_in` is true.

## Example

```python
n = 250
if n > 0:
    if n < 100:
        print("small")
    else:
        print("big")
else:
    print("non-positive")
# prints: big
```

## Your task

Read a whole number and classify it:

- if it is **0 or negative**, print `non-positive`;
- otherwise (it is positive), print `small` when it is **less than 100**, or
  `big` when it is **100 or more**.

Use a nested `if` (an outer check for positive, an inner check for the size).

For input `42` the output is:

```
small
```

## Done when

- `-1` and `0` print `non-positive`; `42` prints `small`; `100` and `500` print
  `big`.
""",

"3.6 hints": r"""First decide positive vs not. Only if positive do you ask small vs big.

---

Outer: `if n > 0:` ... `else: print("non-positive")`. Inside the if, another
if/else comparing n to 100.

---

n = int(input())
if n > 0:
    if n < 100:
        print("small")
    else:
        print("big")
else:
    print("non-positive")
""",

"3.6 reference": r"""An `if` block may itself contain another `if` — **nesting**. The inner test runs
**only when** the outer condition was true, so nesting expresses "this, and then
within that, this".

- Each level adds a step of indentation; the inner block is indented under the
  inner `if`.
- Nesting and `and` can express the same thing — `if a: if b:` is like
  `if a and b:` — but nesting is the right tool when the outer case needs its own
  handling (e.g. an `else`) separate from the inner one.
- Keep nesting shallow; deep pyramids are hard to read, and an `elif` chain or
  early `return` often reads better.

```python
if logged_in:
    if is_admin:
        show_admin_panel()   # only when logged_in AND is_admin
    else:
        show_user_panel()    # logged_in but not admin
```
""",

"3.7 brief": r"""# 3.7 -- while

## Concept

A **`while` loop** repeats a block **as long as** a condition stays `True`. It
checks the condition, runs the block, then checks again -- over and over:

```python
count = 1
while count <= 3:
    print(count)
    count = count + 1   # move toward making the condition False
# prints 1, 2, 3
```

The line `count = count + 1` is essential: it changes `count` so the condition
will eventually become `False`. Without it the loop never stops.

## Common misconception -- the endless loop

If the condition never becomes `False`, the loop runs forever. Always make sure
something inside the loop moves toward the stopping point. (If your program seems
to hang, that is usually an endless loop.)

## Example

```python
n = 4
i = 1
while i <= n:
    print(i)
    i = i + 1
# prints 1, 2, 3, 4
```

## Your task

Read a whole number `n`, then print every number from `1` up to `n`, each on its
own line, using a `while` loop.

For input `3` the output is:

```
1
2
3
```

## Done when

- `3` prints `1`, `2`, `3`. `1` prints just `1`.
- `0` (or a negative) prints nothing -- the loop body never runs.
""",

"3.7 hints": r"""Start a counter at 1 and loop while it is still <= n.

---

`i = 1`, then `while i <= n:` print i and then `i = i + 1`.

---

n = int(input())
i = 1
while i <= n:
    print(i)
    i = i + 1
""",

"3.7 reference": r"""A **`while`** loop repeats its block **as long as** its condition stays true. The
condition is checked **before** each pass; when it becomes false, the loop ends
and the program continues below.

- Something inside the loop must eventually make the condition false (e.g.
  advancing a counter), or it loops forever — an infinite loop.
- If the condition is false at the very first check, the body runs zero times.
- Use `while` when you don't know the number of passes up front (you loop until
  something happens); use `for` when you're counting a known range.

```python
n = 3
while n > 0:
    print(n)
    n = n - 1        # moves toward ending the loop -> 3, 2, 1
```
""",

"3.8 brief": r"""# 3.8 -- Looping until a sentinel

## Concept

A loop does not have to count. It can keep going until the user enters a special
**sentinel** value that means "stop". The trick is to read once *before* the
loop, then read again *at the end* of each pass:

```python
line = input()
while line != "quit":
    print("you said:", line)
    line = input()        # read the next one
print("done")
```

The loop keeps running while the input is not the sentinel (`"quit"` here). As
soon as the sentinel arrives, the condition is false and the loop ends.

## Example

Read numbers and add them up until a `0` is entered:

```python
total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
```

## Your task

Read whole numbers, one per line, and add them up. Stop when the number `0` is
entered (do not add the `0`). Then print the total.

For the input `4`, `5`, `0` the output is:

```
9
```

## Done when

- `4`, `5`, `0` prints `9`; a lone `0` prints `0`.
- The `0` itself is not added; numbers can be negative.
""",

"3.8 hints": r"""Read one number before the loop, and read the next at the end of each pass.

---

`total = 0`, read n, then `while n != 0:` add to total and read the next n.
After the loop, print total.

---

total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
""",

"3.8 reference": r"""A **sentinel** loop reads values repeatedly and stops when it sees a special
"stop" value rather than after a fixed count. The pattern is a `while` whose
condition tests the most recent input against the sentinel.

- Read once before the loop (or read at the top of each pass), then compare to
  the sentinel to decide whether to continue.
- The sentinel itself is **not** processed — the check happens before the work,
  so the stop value ends the loop instead of being counted.

```python
line = input()
while line != "quit":     # "quit" is the sentinel
    print("you said:", line)
    line = input()        # read the next, then re-check
```
""",

"3.9 brief": r"""# 3.9 -- for and range

## Concept

A **`for` loop** runs its block once for each item in a sequence. Combined with
**`range`**, it is the usual way to repeat something a set number of times.

`range(n)` produces the numbers `0, 1, 2, ..., n-1` (it stops *before* `n`):

```python
for i in range(4):
    print(i)
# prints 0, 1, 2, 3
```

Each time round, the loop variable (`i` here) takes the next value. You do not
manage a counter yourself -- `range` does it for you, so there is no endless-loop
risk.

`range` can also take a start and step: `range(1, 5)` is `1,2,3,4`;
`range(0, 10, 2)` is `0,2,4,6,8`.

## Example

```python
for i in range(3):
    print(i)
# prints 0, 1, 2
```

## Your task

Read a whole number `n`, then print every number from `0` up to `n-1`, each on
its own line, using a `for` loop with `range`.

For input `4` the output is:

```
0
1
2
3
```

## Done when

- `4` prints `0,1,2,3` (each on a line). `1` prints just `0`.
- `0` prints nothing.
""",

"3.9 hints": r"""range(n) gives 0, 1, ..., n-1. Loop over it with for.

---

`for i in range(n):` then an indented `print(i)`.

---

n = int(input())
for i in range(n):
    print(i)
""",

"3.9 reference": r"""**`range(n)`** produces the integers `0, 1, …, n - 1` — `n` numbers starting at
zero — and a **`for`** loop runs its block once for each, binding the loop
variable to the current value.

- `range(n)` stops **before** `n` (half-open), so `range(5)` is `0,1,2,3,4` —
  five passes.
- `range(start, stop)` begins at `start`; `range(start, stop, step)` counts by
  `step` (which may be negative to count down).
- `range` is lazy — it yields numbers on demand without building a list — so a
  huge range costs nothing until iterated.

```python
for i in range(3):
    print(i)              # 0, 1, 2

for i in range(2, 6):
    print(i)              # 2, 3, 4, 5
```
""",

"3.10 brief": r"""# 3.10 -- Looping over a string

## Concept

A `for` loop works on more than ranges. A **string is a sequence of characters**,
so you can loop straight over it -- one character per pass:

```python
for ch in "cat":
    print(ch)
# prints:
# c
# a
# t
```

No indexing needed: `ch` is each character in turn. (You can loop over many kinds
of sequences this way; strings are the first.)

## Example

```python
word = "hi"
for ch in word:
    print(ch)
# prints h then i
```

## Your task

Read a word and print each of its characters on its own line, using a `for`
loop over the string.

For input `cat` the output is:

```
c
a
t
```

## Done when

- `cat` prints `c`, `a`, `t` on separate lines.
- A single letter prints that letter; empty input prints nothing.
""",

"3.10 hints": r"""You can loop directly over a string -- each pass gives one character.

---

`for ch in word:` then an indented `print(ch)`.

---

word = input()
for ch in word:
    print(ch)
""",

"3.10 reference": r"""A string is **iterable**, so a `for` loop walks it **one character at a time**,
in order, binding the loop variable to each character. You don't index by hand.

- Each pass gives a one-character string; the loop runs `len(s)` times.
- This is the direct way to examine or tally characters — pair it with an `if`
  inside the loop to act on certain ones.
- The same `for ... in` form iterates any sequence (lists, ranges, …), not just
  strings.

```python
for ch in "cat":
    print(ch)             # c, then a, then t
```
""",

"3.11 brief": r"""# 3.11 -- break and continue

## Concept

Two keywords change how a loop flows:

- **`break`** stops the loop **immediately** -- no more passes.
- **`continue`** skips the **rest of the current pass** and jumps to the next
  one.

```python
for ch in "a,b,c":
    if ch == ",":
        continue        # skip commas
    print(ch)
# prints a, b, c (commas skipped)

for n in range(100):
    if n == 3:
        break           # stop the whole loop at 3
    print(n)
# prints 0, 1, 2
```

`continue` skips one item; `break` ends the loop.

## Example

```python
for ch in "abxcd":
    if ch == "x":
        break
    print(ch)
# prints a, b   (stops at x)
```

## Your task

Read a word and loop over its characters:

- **skip** the letter `o` (use `continue` -- do not print it),
- **stop** completely at the letter `x` (use `break` -- print nothing from `x`
  onward),
- print every other character on its own line.

For input `boxes` the output is:

```
b
```

(`b`, then `o` is skipped, then `x` stops the loop.)

## Done when

- `boxes` prints `b`; `good` prints `g` then `d` (the `o`s skipped); `abc` prints
  `a`, `b`, `c`.
""",

"3.11 hints": r"""Inside the loop, check for "x" first (break), then "o" (continue), then print.

---

`for ch in word:` -> `if ch == "x": break`, then `if ch == "o": continue`,
then `print(ch)`.

---

word = input()
for ch in word:
    if ch == "x":
        break
    if ch == "o":
        continue
    print(ch)
""",

"3.11 reference": r"""Two statements alter a loop's flow from inside it:

- **`break`** ends the loop **immediately**, skipping any remaining passes and
  jumping to the code after the loop. Use it to stop as soon as you've found
  what you need.
- **`continue`** skips the **rest of the current pass** and jumps straight to the
  loop's next iteration (re-checking the condition / taking the next item).

Both affect only the **innermost** loop that encloses them.

```python
for n in range(10):
    if n == 5:
        break             # stop the whole loop at 5
    if n % 2 == 0:
        continue          # skip evens, go to the next n
    print(n)              # 1, 3
```
""",

"3.12 brief": r"""# 3.12 -- The accumulator pattern

## Concept

A very common loop pattern: keep a **running total** in a variable, start it at
`0`, and add to it on each pass. The variable "accumulates" the result.

```python
total = 0
for n in [4, 2, 9]:
    total = total + n
print(total)        # 15
```

The key steps are: **start at 0 before the loop**, **add inside the loop**, **use
the result after the loop**. The same shape works for counting (start at 0, add 1
each time) or building a string (start at "", add a piece each time).

This puzzle combines what you have learned: a `for` loop, `range`, reading input,
and an accumulator.

## Example

```python
total = 0
for _ in range(3):
    total = total + int(input())
print(total)
```

(`_` is a normal variable name often used when you don't need the loop value.)

## Your task

Read a whole number `n` (a count). Then read `n` more whole numbers, one per
line, and print their **sum**.

For the input `3`, then `10`, `20`, `5`, the output is:

```
35
```

## Done when

- Count `3` with `10, 20, 5` prints `35`.
- A count of `0` reads no further numbers and prints `0`.
- The numbers may be negative.
""",

"3.12 hints": r"""Read the count first. Start a total at 0, then loop that many times adding each
number.

---

`n = int(input())`, `total = 0`, then `for _ in range(n):` add `int(input())`
to total. Print total after the loop.

---

n = int(input())
total = 0
for _ in range(n):
    total = total + int(input())
print(total)
""",

"3.12 reference": r"""The **accumulator** pattern builds up a result across a loop. You initialise a
variable **before** the loop, then update it on **every** pass; after the loop it
holds the combined result.

- For a sum, start the total at `0` and add each value (`total = total + x`, or
  `total += x`). Starting at `0` is the identity for `+`, so an empty loop
  leaves it `0`.
- The same shape counts (start at 0, `+= 1` per match), builds a string (start
  `""`, `+=`), or collects a list (start `[]`, `.append`).
- The accumulator must live **outside** the loop — declaring it inside would
  reset it every pass.

```python
total = 0
for n in [3, 1, 4]:
    total += n            # 3, then 4, then 8
print(total)             # 8
```
""",

"4.1 brief": r"""# 4.1 -- Lists and append

## Concept

A **list** holds several values in order, in one variable. You write a list with
square brackets, items separated by commas:

```python
nums = [10, 20, 30]
print(nums)        # [10, 20, 30]
print(nums[0])     # 10   (index like a string -- from 0)
print(len(nums))   # 3
```

A list can start empty and grow. `.append(x)` adds `x` to the **end**:

```python
nums = []
nums.append(10)
nums.append(20)
print(nums)        # [10, 20]
```

This "start empty, append in a loop" pattern is how you build a list from input.

## Example

```python
items = []
items.append(1)
items.append(2)
print(items)       # [1, 2]
```

## Your task

Read a whole number `n`, then read `n` more whole numbers (one per line). Collect
them into a list with `.append()`, and print the finished list.

For input `3`, then `1`, `2`, `3`:

```
[1, 2, 3]
```

## Done when

- `3` with `1, 2, 3` prints `[1, 2, 3]`.
- A count of `0` prints `[]` (an empty list).
""",

"4.1 hints": r"""Start with an empty list [], then append each number inside a loop.

---

`nums = []`, read n, then `for _ in range(n): nums.append(int(input()))`.
Finally `print(nums)`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(nums)
""",

"4.1 reference": r"""A **list** is an ordered, mutable sequence of values, written in square brackets:
`[10, 20, 30]`. The empty list is `[]`. Items are reached by index just like
string characters (`lst[0]`, `lst[-1]`).

- **`.append(x)`** adds `x` to the **end**, growing the list by one. It changes
  the list in place and returns `None` (so never write `lst = lst.append(x)`).
- The build-from-empty pattern: start with `[]`, then `.append` once per pass of
  a loop to collect results.
- Unlike strings, a list may hold values of mixed types.

```python
nums = []
for i in range(3):
    nums.append(i * i)   # -> [0, 1, 4]
```
""",

"4.2 brief": r"""# 4.2 -- Changing a list

## Concept

Unlike strings, lists can be **changed in place** (they are *mutable*). A few ways:

- Replace an item by index: `nums[0] = 99`
- Remove and return the **last** item: `nums.pop()`
- Remove the first matching **value**: `nums.remove(20)`

```python
nums = [10, 20, 30]
nums[0] = 99      # [99, 20, 30]   replace by position
nums.pop()        # [99, 20]       drop the last item (returns 30)
print(nums)       # [99, 20]
```

These change the existing list -- the variable still points at the same list,
now modified.

## Example

```python
xs = [1, 2, 3]
xs[1] = 0
xs.pop()
print(xs)         # [1, 0]
```

## Your task

Read a count `n` (at least 1), then `n` numbers, into a list. Then:

1. **double the first item** (replace `nums[0]` with `nums[0] * 2`), and
2. **remove the last item** with `.pop()`.

Print the resulting list. For input `3`, then `5`, `2`, `9`:

```
[10, 2]
```

(`[5, 2, 9]` -> double first -> `[10, 2, 9]` -> pop -> `[10, 2]`.)

## Done when

- `5, 2, 9` gives `[10, 2]`.
- A single number `n=1` (e.g. just `4`) gives `[]` -- doubled to `[8]`, then the
  last (only) item is popped.
""",

"4.2 hints": r"""Build the list as before, then change it in place.

---

`nums[0] = nums[0] * 2` to double the first item; `nums.pop()` to drop the last.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums[0] = nums[0] * 2
nums.pop()
print(nums)
""",

"4.2 reference": r"""Lists are **mutable**: their contents can change in place, unlike strings.

- **`lst[i] = x`** replaces the item at index `i`. The index must already exist
  (assigning past the end raises `IndexError`).
- **`.pop()`** removes and **returns** the last item, shrinking the list;
  `.pop(i)` removes the item at index `i`. Popping from an empty list raises.
- Other in-place changes: `.insert(i, x)`, `.remove(value)`, `del lst[i]`.

Because the change is in place, every name referring to the same list object sees
it.

```python
lst = [10, 20, 30]
lst[1] = 99      # [10, 99, 30]
last = lst.pop() # last == 30, lst == [10, 99]
```
""",

"4.3 brief": r"""# 4.3 -- Looping over a list

## Concept

Just like a string, a list is a sequence -- so a `for` loop walks straight over
its items, one per pass:

```python
nums = [10, 20, 30]
for x in nums:
    print(x)        # 10, then 20, then 30
```

`len(nums)` gives the number of items, and slicing works too -- `nums[1:]` is all
but the first, `nums[:2]` is the first two:

```python
print(len(nums))    # 3
print(nums[:2])     # [10, 20]
```

## Example

```python
xs = [1, 2, 3]
for x in xs:
    print(x * 10)   # 10, 20, 30
```

## Your task

Read a count `n`, then `n` numbers, into a list. First print how many numbers
there are, then print each number **doubled**, one per line.

For input `3`, then `5`, `2`, `9`:

```
3
10
4
18
```

## Done when

- `5, 2, 9` prints `3`, then `10`, `4`, `18`.
- A count of `0` prints just `0` (no numbers to double).
""",

"4.3 hints": r"""After building the list, print len(nums), then loop over it.

---

`print(len(nums))`, then `for x in nums: print(x * 2)`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(len(nums))
for x in nums:
    print(x * 2)
""",

"4.3 reference": r"""A list is iterable, so **`for x in lst`** visits each item in order, binding the
loop variable to the item itself (not its index).

- This is the usual way to read a list. When you also need the position, pair it
  with `range(len(lst))` or `enumerate` (chapter 5).
- **`len(lst)`** gives the item count; **slicing** (`lst[1:3]`, `lst[::-1]`)
  works exactly as on strings and returns a new list.

```python
for name in ["Ada", "Linus"]:
    print(name)

total = 0
for n in [3, 1, 4]:
    total += n           # iterate and accumulate
```
""",

"4.4 brief": r"""# 4.4 -- split: text into a list

## Concept

`s.split()` breaks a string into a **list of pieces**. With no argument it splits
on whitespace, so it turns a sentence into its words:

```python
"the quick brown fox".split()    # ['the', 'quick', 'brown', 'fox']
```

The result is a real list, so everything you know about lists applies -- `len`,
indexing, looping:

```python
words = "a b c".split()
print(len(words))    # 3
print(words[0])      # a
```

You can also split on a specific separator by passing it in:
`"a,b,c".split(",")` gives `['a', 'b', 'c']`.

## Example

```python
parts = "one two three".split()
print(len(parts))    # 3
```

## Your task

Read a line of words separated by spaces, and print **how many words** it
contains.

For input `the quick brown fox`:

```
4
```

## Done when

- `the quick brown fox` prints `4`; a single word prints `1`.
- An empty line prints `0`.
""",

"4.4 hints": r""".split() turns the line into a list of words. Then count them.

---

`print(len(input().split()))`.

---

line = input()
print(len(line.split()))
""",

"4.4 reference": r"""**`s.split()`** breaks a string into a **list of pieces**. With no argument it
splits on runs of **whitespace** and discards leading/trailing blanks — the usual
way to get the words of a line.

- `s.split(sep)` splits on the exact separator `sep`, keeping empty pieces
  between adjacent separators (`"a,,b".split(",")` is `["a", "", "b"]`).
- `s.split(sep, maxsplit)` splits at most `maxsplit` times — handy to peel off a
  prefix, e.g. `"key=a=b".split("=", 1)` is `["key", "a=b"]`.
- It is the inverse of `join` (next).

```python
"the quick fox".split()        # ['the', 'quick', 'fox']
"2024-01-15".split("-")        # ['2024', '01', '15']
```
""",

"4.5 brief": r"""# 4.5 -- join: a list into text

## Concept

`.join()` is the opposite of `split`: it glues a **list of strings** into one
string, putting a separator between each piece. You call it *on the separator*:

```python
words = ["a", "b", "c"]
print("-".join(words))    # a-b-c
print(", ".join(words))   # a, b, c
print("".join(words))     # abc   (no separator)
```

Read it as "join these words with this separator between them". The list must
contain strings.

## Common mistake

`join` is written separator-first: `"-".join(words)`, **not** `words.join("-")`.

## Example

```python
parts = ["2024", "12", "25"]
print("/".join(parts))    # 2024/12/25
```

## Your task

Read a count `n`, then `n` words (one per line), into a list. Print them joined
with a dash `-`.

For input `3`, then `a`, `b`, `c`:

```
a-b-c
```

## Done when

- `a, b, c` prints `a-b-c`; a single word prints just that word.
- A count of `0` prints an empty line (nothing to join).
""",

"4.5 hints": r"""Collect the words into a list, then join them. join is called on the separator.

---

Build the list, then `print("-".join(words))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print("-".join(words))
""",

"4.5 reference": r"""**`sep.join(parts)`** glues an iterable of **strings** into one string, placing
`sep` between adjacent items. The separator is the string you call it on, which
reads oddly at first but lets the separator be any string.

- Every item must already be a string; numbers raise `TypeError`. Convert first,
  e.g. `", ".join(str(n) for n in nums)`.
- `"".join(parts)` concatenates with no separator — the efficient way to build a
  string from many pieces (far better than repeated `+`).
- It is the inverse of `split`.

```python
"-".join(["2024", "01", "15"])   # '2024-01-15'
" ".join(["the", "fox"])          # 'the fox'
```
""",

"4.6 brief": r"""# 4.6 -- Lists inside lists

## Concept

A list can hold **other lists**. This is how you represent rows of data, pairs,
grids, and so on:

```python
pairs = [[1, 2], [3, 4], [5, 6]]
print(pairs)        # [[1, 2], [3, 4], [5, 6]]
print(pairs[0])     # [1, 2]        the first inner list
print(pairs[0][1])  # 2            first inner list, second item
```

Two indexes: the first picks an inner list, the second picks an item inside it.
Looping gives you each inner list in turn:

```python
for p in pairs:
    print(p[0] + p[1])   # 3, 7, 11
```

## Example

```python
grid = [[1, 1], [2, 2]]
for row in grid:
    print(row[0] + row[1])   # 2, 4
```

## Your task

Read a count `n`, then `n` **pairs** of numbers (each pair is two numbers, on two
lines). Build a list of `[a, b]` pairs. First print the whole nested list, then
print the **sum of each pair**, one per line.

For input `2`, then `1`, `2`, `3`, `4`:

```
[[1, 2], [3, 4]]
3
7
```

## Done when

- `1,2` and `3,4` print `[[1, 2], [3, 4]]` then `3` then `7`.
- A count of `0` prints `[]` and nothing else.
""",

"4.6 hints": r"""For each pair, read two numbers and append them as a two-item list [a, b].

---

`pairs.append([a, b])` builds the nested list. Print it, then loop:
`for p in pairs: print(p[0] + p[1])`.

---

n = int(input())
pairs = []
for _ in range(n):
    a = int(input())
    b = int(input())
    pairs.append([a, b])
print(pairs)
for p in pairs:
    print(p[0] + p[1])
""",

"4.6 reference": r"""A list can contain other lists — a **nested** list — modelling a grid or table.
`grid[r]` selects an inner list (a row); `grid[r][c]` then selects an item from
it (a column), so two indexes reach one cell.

- The first index picks the row, the second the item within that row.
- A `for row in grid:` loop yields each inner list; nest a second loop
  (`for cell in row:`) to reach every item.
- The inner lists are ordinary lists — mutable and independently sized (rows
  need not be the same length).

```python
grid = [[1, 2, 3],
        [4, 5, 6]]
grid[0][2]    # 3   -- row 0, column 2
grid[1][0]    # 4
```
""",

"4.7 brief": r"""# 4.7 -- Tuples and unpacking

## Concept

A **tuple** is like a list, but **immutable** -- once made, it can't be changed.
You write one with parentheses (or just commas):

```python
point = (3, 7)
print(point[0])    # 3
```

**Unpacking** assigns several variables at once from a tuple (or list):

```python
x, y = point       # x = 3, y = 7
```

The left side names match the items on the right, in order. A neat trick this
enables is **swapping** two variables without a temporary:

```python
a, b = 1, 2
a, b = b, a        # now a = 2, b = 1
```

The right-hand side `b, a` builds a tuple, which is then unpacked into `a, b`.

## Example

```python
a, b = 10, 20
a, b = b, a
print(a)    # 20
print(b)    # 10
```

## Your task

Read two whole numbers (each on its own line). **Swap** them using tuple
unpacking, then print the first, then the second.

For input `3` then `7`:

```
7
3
```

## Done when

- `3, 7` prints `7` then `3`.
- It works for any two numbers (including two equal ones).
""",

"4.7 hints": r"""Read both numbers, then swap them in one line with a, b = b, a.

---

`a = int(input())`, `b = int(input())`, then `a, b = b, a`, then print a and b.

---

a = int(input())
b = int(input())
a, b = b, a
print(a)
print(b)
""",

"4.7 reference": r"""A **tuple** is an ordered, **immutable** sequence, written with commas (often in
parentheses): `(3, 4)`, or just `3, 4`. Once made it cannot be changed.

- **Unpacking** assigns the items of a sequence to several names at once:
  `a, b = point`. The count on each side must match.
- This enables the one-line **swap** `a, b = b, a`: the right side is built into
  a tuple first, then unpacked, so no temporary is needed.
- Use a tuple for a fixed group of related values (a coordinate, a record); use a
  list when the collection grows or changes.

```python
point = (3, 4)
x, y = point        # x = 3, y = 4
a, b = b, a         # swap in one line
```
""",

"4.8 brief": r"""# 4.8 -- Dictionaries

## Concept

A **dictionary** (`dict`) maps **keys** to **values** -- a lookup table. You write
one with curly braces and `key: value` pairs:

```python
ages = {"sam": 20, "ada": 36}
print(ages["sam"])     # 20      look up by key
ages["lee"] = 41       # add a new key
ages["sam"] = 21       # update an existing key
```

You look things up by **key** (not by position), which is what makes dicts fast
and handy for "given X, what is its Y?". Start from empty with `{}` and fill it in:

```python
d = {}
d["x"] = 1
```

## Example

```python
prices = {}
prices["apple"] = 3
print(prices["apple"])   # 3
```

## Your task

Read a count `n`, then `n` pairs of a **word** and a **number** (word on one line,
number on the next) into a dictionary (the word is the key, the number the value).
Then read one more **query word** and print the number stored for it.

For input `2`, `apple`, `3`, `banana`, `5`, then the query `banana`:

```
5
```

## Done when

- Building `{apple: 3, banana: 5}` and querying `banana` prints `5`.
- A later pair with the same key updates it (the test relies on the last value
  for any repeated key).
""",

"4.8 hints": r"""Make an empty dict, then store each pair as d[word] = number.

---

`d = {}`, loop reading word + number with `d[word] = int(input())`, then read
the query and `print(d[query])`.

---

n = int(input())
d = {}
for _ in range(n):
    word = input()
    d[word] = int(input())
query = input()
print(d[query])
""",

"4.8 reference": r"""A **dictionary** (`dict`) maps **keys** to **values**: `{"a": 1, "b": 2}`. It is
the tool for lookup by name rather than by position.

- **`d[key]`** reads the value for a key; **`d[key] = value`** adds the key (if
  new) or updates it (if present). Keys are unique — assigning an existing key
  overwrites.
- Reading a **missing** key with `d[key]` raises `KeyError` (see `.get`, 4.10).
- Keys must be immutable (strings, numbers, tuples); values can be anything.
  `len(d)` counts the pairs; `key in d` tests for a key.

```python
ages = {"Ada": 36}
ages["Ada"]          # 36
ages["Linus"] = 21   # add a new pair
```
""",

"4.9 brief": r"""# 4.9 -- Looping over a dictionary

## Concept

To visit everything in a dict, loop over `.items()`, which gives each **key and
value** together:

```python
ages = {"sam": 20, "ada": 36}
for name, age in ages.items():
    print(name, age)      # sam 20, then ada 36
```

The `for name, age in ...` part is unpacking each pair into two variables. Dicts
remember the order you inserted keys, so you get them back in that order.

There are also `.keys()` (just the keys) and `.values()` (just the values), but
`.items()` is the usual one when you need both.

## Example

```python
d = {"x": 1, "y": 2}
for k, v in d.items():
    print(f"{k}={v}")     # x=1, then y=2
```

## Your task

Read a count `n`, then `n` pairs of a **word** and a **number** into a dict. Then
print one line `key=value` for each pair, in the order they were added.

For input `2`, `a`, `1`, `b`, `2`:

```
a=1
b=2
```

## Done when

- `a=1`, `b=2` are printed in insertion order.
- A count of `0` prints nothing.
""",

"4.9 hints": r"""Build the dict, then loop over d.items() to get each key and value.

---

`for k, v in d.items(): print(f"{k}={v}")`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
for k, v in d.items():
    print(f"{k}={v}")
""",

"4.9 reference": r"""**`d.items()`** yields each `(key, value)` pair, so a `for` loop with two
variables walks the whole dictionary, unpacking each pair as it goes.

- `for k, v in d.items():` binds `k` to the key and `v` to its value each pass.
- `d.keys()` and `d.values()` iterate just the keys or just the values; looping
  the dict directly (`for k in d`) iterates the **keys**.
- Iteration order is the **insertion order** (the order keys were first added).

```python
prices = {"pen": 2, "ink": 5}
for item, cost in prices.items():
    print(item, cost)        # pen 2 / ink 5
```
""",

"4.10 brief": r"""# 4.10 -- Missing keys and .get()

## Concept

Looking up a key that isn't in the dict with `d[key]` **crashes** (a `KeyError`):

```python
ages = {"sam": 20}
print(ages["lee"])    # KeyError!
```

`.get()` is the safe way. It returns `None` for a missing key instead of
crashing -- or a **default** you supply:

```python
print(ages.get("lee"))        # None
print(ages.get("lee", 0))     # 0      (your default)
print(ages.get("sam", 0))     # 20     (key exists, so its value)
```

So `d.get(key, default)` means "the value if the key is there, otherwise
`default`".

## Example

```python
d = {"a": 1}
print(d.get("a", 0))    # 1
print(d.get("z", 0))    # 0
```

## Your task

Read a count `n`, then `n` pairs of a word and a number into a dict. Then read a
**query word** and print its number -- but if the word isn't in the dict, print
`0` instead (do not crash).

For input `2`, `a`, `1`, `b`, `2`, then the query `c`:

```
0
```

(`c` isn't a key, so the default `0` is printed.)

## Done when

- A present key prints its value; a missing key prints `0`.
- It never crashes on a missing key (use `.get`).
""",

"4.10 hints": r"""d[key] crashes if the key is missing. d.get(key, 0) returns 0 instead.

---

After building the dict and reading the query, `print(d.get(query, 0))`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
query = input()
print(d.get(query, 0))
""",

"4.10 reference": r"""**`d.get(key, default)`** looks a key up safely: it returns the value if the key
is present, otherwise the `default` — without raising. With no default it returns
`None` for a missing key.

- Use it instead of `d[key]` whenever a missing key is a normal, expected case
  rather than a bug.
- It powers the **tally** idiom: `counts[k] = counts.get(k, 0) + 1` reads the
  running count (0 the first time) and writes the new one.
- `.get` only reads; it never inserts the key (unlike `setdefault`).

```python
ages = {"Ada": 36}
ages.get("Ada", 0)     # 36
ages.get("Nobody", 0)  # 0  -- no KeyError
```
""",

"4.11 brief": r"""# 4.11 -- Sets

## Concept

A **set** is an unordered collection of **unique** items -- it automatically drops
duplicates. Write one with curly braces, or build one from a list with `set(...)`:

```python
s = {1, 2, 2, 3}
print(s)              # {1, 2, 3}   (the duplicate 2 is gone)

nums = [1, 1, 2, 3, 3]
print(set(nums))      # {1, 2, 3}
print(len(set(nums))) # 3           how many *distinct* values
```

Sets are great for "how many different things?" and for fast membership tests
with `in`:

```python
print(2 in s)         # True
```

(Sets have no order and no indexing -- you can't do `s[0]`.)

## Example

```python
words = ["a", "b", "a"]
print(len(set(words)))   # 2
```

## Your task

Read a count `n`, then `n` words. Print how many **distinct** words there are.

For input `4`, `a`, `b`, `a`, `c`:

```
3
```

(`a` appears twice but counts once.)

## Done when

- `a, b, a, c` prints `3`.
- A count of `0` prints `0`.
""",

"4.11 hints": r"""A set drops duplicates. Put the words in a set, then count it.

---

Collect the words in a list, then `print(len(set(words)))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print(len(set(words)))
""",

"4.11 reference": r"""A **set** is an unordered collection of **unique** items: `{1, 2, 3}`. It models
"a group of distinct things" and tests membership fast.

- Building a set from a sequence **drops duplicates**: `set([1, 1, 2])` is
  `{1, 2}`. The empty set is `set()` — `{}` is an empty *dict*.
- **`x in s`** tests membership and is much faster than scanning a list, because
  sets are hash-based.
- Sets are unordered (no indexing, no slicing) and hold only immutable items.
  Add with `.add(x)`, remove with `.discard(x)`.

```python
seen = set()
seen.add("a"); seen.add("a")   # {'a'} -- duplicate ignored
"a" in seen                    # True
set([3, 1, 3, 2])              # {1, 2, 3}
```
""",

"4.12 brief": r"""# 4.12 -- Combining sets

## Concept

Sets can be combined like in maths:

- **intersection** `a & b` -- items in **both**
- **union** `a | b` -- items in **either**
- **difference** `a - b` -- items in `a` but not `b`

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)    # {2, 3}
print(a | b)    # {1, 2, 3, 4}
print(a - b)    # {1}
```

These answer questions like "which items do two groups share?" without writing a
loop. (`a.intersection(b)` and `a.union(b)` do the same as `&` and `|`.)

## Example

```python
x = {"a", "b"}
y = {"b", "c"}
print(len(x & y))   # 1   (just "b")
```

## Your task

Read a first group: a count `n`, then `n` words. Then a second group: a count
`m`, then `m` words. Print **how many distinct words appear in both** groups.

For first group `a`, `b` and second group `b`, `c`:

```
1
```

(Only `b` is in both.)

## Done when

- `{a, b}` and `{b, c}` print `1`.
- Empty groups give `0`; duplicates within a group count once.
""",

"4.12 hints": r"""Put each group in a set, then use the intersection of the two.

---

Build set `a` and set `b`, then `print(len(a & b))`.

---

n = int(input())
a = set()
for _ in range(n):
    a.add(input())
m = int(input())
b = set()
for _ in range(m):
    b.add(input())
print(len(a & b))
""",

"4.12 reference": r"""Sets support the algebra of collections:

- **`a & b`** (intersection) — items in **both**.
- **`a | b`** (union) — items in **either**.
- **`a - b`** (difference) — items in `a` but **not** in `b`.

Each returns a **new** set. (`^` is the symmetric difference — in exactly one.)
These express set questions directly, replacing hand-written loops that compare
two collections.

```python
a, b = {1, 2, 3}, {2, 3, 4}
a & b     # {2, 3}
a | b     # {1, 2, 3, 4}
a - b     # {1}
```
""",

"4.13 brief": r"""# 4.13 -- Choosing the right collection

## Concept

You now have four collections. Picking the right one makes a problem easy:

- **list** -- ordered items, duplicates allowed (`[1, 2, 2]`). Use for sequences.
- **tuple** -- like a list but fixed/immutable. Use for fixed groups.
- **set** -- unordered, **unique** items. Use for "distinct" and fast membership.
- **dict** -- key -> value lookup. Use for "given X, find its Y".

This puzzle combines a few:

- `len(nums)` -- how many items (a **list** keeps every value, including repeats).
- `len(set(nums))` -- how many **distinct** values (a **set** drops duplicates).
- the **sum** -- a loop with an accumulator (or `sum(nums)`).

## Example

```python
nums = [1, 2, 2, 3]
print(len(nums))        # 4
print(len(set(nums)))   # 3
```

## Your task

Read a count `n`, then `n` numbers. Print three lines:

1. how many numbers there are,
2. how many **distinct** numbers there are,
3. their **total**.

For input `4`, then `1`, `2`, `2`, `3`:

```
4
3
8
```

## Done when

- `1, 2, 2, 3` prints `4`, `3`, `8`.
- A count of `0` prints `0`, `0`, `0`.
""",

"4.13 hints": r"""Build the list. The count is len(nums); the distinct count uses a set.

---

`print(len(nums))`, `print(len(set(nums)))`, then the total (a loop, or sum).

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(len(nums))
print(len(set(nums)))
total = 0
for x in nums:
    total = total + x
print(total)
""",

"4.13 reference": r"""The three core collections fit different jobs — choosing the right one makes code
simpler and faster:

- **list** — an **ordered** sequence that may repeat. Use it to keep every value,
  in order (a log, a queue of items to process).
- **set** — an unordered group of **distinct** items with fast membership. Use it
  to drop duplicates or ask "have I seen this?".
- **dict** — a mapping from **keys to values**. Use it to look something up by
  name (a count per word, a price per item).

Ask: do I need order and repeats (list), uniqueness and membership (set), or
lookup by key (dict)?

```python
order  = ["a", "b", "a"]    # keep all, in order
unique = {"a", "b"}         # distinct only
price  = {"a": 2, "b": 5}   # look up by key
```
""",

"5.1 brief": r"""# 5.1 -- in: membership testing

## Concept

You met `in` with sets (4.11). It actually works on almost everything:

```python
"e" in "hello"        # True   (substring of a string)
3 in [1, 2, 3]        # True   (item of a list)
"sam" in {"sam": 20}  # True   (KEY of a dict)
```

`x in s` is an expression that gives a **boolean** (`True`/`False`), so it
slots straight into an `if`:

```python
if "@" in address:
    print("looks like an email")
```

There is also the opposite, `not in`:

```python
if "x" not in word:
    print("no x here")
```

Compare that with chapter 2, where you used `s.find()` and checked for `-1`.
`in` says the same thing in plain English -- prefer it whenever you only need
*whether* something is there, not *where*.

## Example

```python
word = "banana"
print("n" in word)     # True
print("z" in word)     # False
```

## Your task

Read a word, then a single letter. Print `yes` if the letter appears in the
word, and `no` if it doesn't.

For input `banana`, then `n`:

```
yes
```

## Done when

- A letter that appears prints `yes`; one that doesn't prints `no`.
- It works for a one-letter word too.
- You used the `in` operator (not `.find()` or `.count()`).
""",

"5.1 hints": r"""`letter in word` is already True or False -- put it straight in an `if`.

---

Read the word, read the letter, then branch: `if letter in word:` print yes,
`else:` print no.

---

word = input()
letter = input()
if letter in word:
    print("yes")
else:
    print("no")
""",

"5.1 reference": r"""The **`in`** operator tests membership and yields a boolean, so it drops straight
into an `if` or `while`. `x in c` is `True` when `x` is found in `c`.

- For a **string**, `in` tests for a **substring**: `"cat" in "concatenate"` is
  `True`.
- For a **list** or **tuple**, it tests for an item (scanning the sequence).
- For a **dict** or **set**, it tests for a **key**/member — and is fast
  (hash-based), unlike the linear scan of a list.
- `x not in c` is the readable negation.

```python
"a" in "cat"          # True
3 in [1, 2, 3]        # True
"key" in {"key": 1}   # True  -- tests keys
```
""",

"5.2 brief": r"""# 5.2 -- sum()

## Concept

In 3.12 you wrote the **accumulator pattern** by hand:

```python
total = 0
for x in nums:
    total = total + x
```

That pattern is so common Python ships it as a built-in function:

```python
total = sum(nums)
```

`sum(list_of_numbers)` adds every item and returns the total. On an empty list
it returns `0` -- exactly what your hand-written accumulator started with.

This chapter is full of such **power tools**: built-ins that replace a loop you
have already written yourself once. You earn the shortcut by knowing what it
replaces.

## Example

```python
nums = [3, 1, 4]
print(sum(nums))    # 8
print(sum([]))      # 0
```

## Your task

Read a count `n`, then `n` whole numbers (one per line). Print their total
using `sum()`.

For input `3`, then `3`, `1`, `4`:

```
8
```

## Done when

- `3, 1, 4` prints `8`; negatives work too.
- A count of `0` prints `0`.
- You used `sum()` -- not a hand-written loop this time.
""",

"5.2 hints": r"""Build the list of numbers first (like 4.13), then hand the whole list to one
function call.

---

`sum(nums)` returns the total -- print that. No `total = 0` needed.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(sum(nums))
""",

"5.2 reference": r"""**`sum(numbers)`** adds up an iterable of numbers and returns the total — the
accumulator loop of 3.12 as one built-in call.

- It works on any iterable of numbers (list, tuple, range, generator). `sum([])`
  is `0`.
- An optional second argument is the **start** value: `sum(nums, 100)` begins the
  total at 100.
- It only adds numbers; to total something derived from each item, feed it a
  comprehension or generator, e.g. `sum(len(w) for w in words)`.

```python
sum([3, 1, 4])              # 8
sum(range(1, 101))          # 5050
sum(len(w) for w in words)  # total characters
```
""",

"5.3 brief": r"""# 5.3 -- min() and max()

## Concept

Finding the smallest or largest item is another loop you could write by hand
("keep a best-so-far, compare each item") -- and another loop Python ships as
a built-in:

```python
nums = [3, 7, 1]
print(min(nums))    # 1
print(max(nums))    # 7
```

`min()` and `max()` take a list (any non-empty collection, in fact) and return
its smallest / largest item. They also work on strings -- "smallest" then means
earliest in alphabetical order:

```python
min("cab")     # "a"
```

One caution: on an **empty** list they crash (there is no smallest of
nothing), so this puzzle guarantees at least one number.

## Example

```python
nums = [4, -2, 9]
print(min(nums))    # -2
print(max(nums))    # 9
```

## Your task

Read a count `n` (always at least 1), then `n` whole numbers. Print two lines:
the smallest, then the largest.

For input `3`, then `4`, `-2`, `9`:

```
-2
9
```

## Done when

- `4, -2, 9` prints `-2` then `9`.
- A single number prints itself twice (it is both the min and the max).
- You used `min()` and `max()`.
""",

"5.3 hints": r"""Build the list first; then the smallest and largest are each one function call.

---

`print(min(nums))` then `print(max(nums))` -- two lines, two calls.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(min(nums))
print(max(nums))
""",

"5.3 reference": r"""**`min(items)`** and **`max(items)`** return the smallest and largest item of a
non-empty collection.

- They compare with `<`/`>`, so they work on numbers and on strings (which
  compare lexicographically).
- Called on an **empty** iterable they raise `ValueError`; pass `default=` to
  supply a fallback.
- A `key=` function ranks by a derived value instead of the item itself:
  `max(words, key=len)` returns the **longest** word.

```python
min([3, 1, 4])             # 1
max("apple", "pear")       # 'pear'
max(words, key=len)        # the longest word
```
""",

"5.4 brief": r"""# 5.4 -- sorted()

## Concept

`sorted(nums)` returns a **new list** with the same items in order, smallest
first:

```python
nums = [3, 1, 2]
print(sorted(nums))    # [1, 2, 3]
print(nums)            # [3, 1, 2]  -- the original is untouched
```

Two things to know:

- It returns a *copy*; the original list keeps its order. (There is also
  `nums.sort()`, a method that reorders the list **in place** -- handy later,
  but `sorted()` is the safer default because nothing is changed behind your
  back.)
- Largest-first is one keyword away: `sorted(nums, reverse=True)`.

Duplicates are kept -- sorting reorders, it never removes.

## Example

```python
for x in sorted([3, 1, 2]):
    print(x)
# 1
# 2
# 3
```

## Your task

Read a count `n`, then `n` whole numbers. Print them smallest to largest,
one per line.

For input `4`, then `3`, `1`, `3`, `2`:

```
1
2
3
3
```

## Done when

- `3, 1, 3, 2` prints `1, 2, 3, 3` -- the duplicate `3` appears twice.
- A count of `0` prints nothing.
- You used `sorted()`.
""",

"5.4 hints": r"""Build the list, then loop over `sorted(nums)` instead of `nums`.

---

`for x in sorted(nums):` visits the items smallest-first; print each one.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for x in sorted(nums):
    print(x)
""",

"5.4 reference": r"""**`sorted(items)`** returns a **new** list with the items in ascending order,
leaving the original untouched.

- It accepts any iterable and always returns a list. Numbers sort numerically,
  strings lexicographically.
- **`reverse=True`** sorts descending. **`key=`** sorts by a derived value:
  `sorted(words, key=len)` orders by length, `sorted(d.items(), key=lambda kv:
  kv[1])` orders dict pairs by value.
- The list method `lst.sort()` sorts **in place** and returns `None`; use
  `sorted` when you want a new list or are sorting a non-list.

```python
sorted([3, 1, 2])               # [1, 2, 3]
sorted([3, 1, 2], reverse=True) # [3, 2, 1]
sorted(words, key=len)          # shortest to longest
```
""",

"5.5 brief": r"""# 5.5 -- enumerate()

## Concept

Sometimes a loop needs both the **item** and its **position**. You could track
a counter by hand, but Python has a built-in for exactly this:

```python
words = ["tea", "milk"]
for i, w in enumerate(words):
    print(i, w)
# 0 tea
# 1 milk
```

Each pass, `enumerate` hands you a pair `(position, item)`, which you unpack
into two variables (4.7) -- the same trick as `for k, v in d.items()`.

Counting from `0` is rarely what you want to *show* a person. The second
argument sets the starting number:

```python
for i, w in enumerate(words, 1):
    print(i, w)
# 1 tea
# 2 milk
```

## Example

```python
for i, ch in enumerate("hi", 1):
    print(f"{i}. {ch}")
# 1. h
# 2. i
```

## Your task

Read a count `n`, then `n` words. Print them as a numbered list starting at 1,
in the format `1. word` (a dot and a space after the number).

For input `3`, then `tea`, `milk`, `sugar`:

```
1. tea
2. milk
3. sugar
```

## Done when

- Three words print as `1. ...`, `2. ...`, `3. ...`.
- A count of `0` prints nothing.
- You used `enumerate()` -- no hand-kept counter.
""",

"5.5 hints": r"""`for i, w in enumerate(words, 1):` gives you the number and the word together,
starting at 1.

---

Inside the loop, build the line with an f-string: `f"{i}. {w}"`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
for i, w in enumerate(words, 1):
    print(f"{i}. {w}")
""",

"5.5 reference": r"""**`enumerate(items)`** pairs each item with its position, so a `for` loop gets
both at once — no hand-kept counter.

- `for i, item in enumerate(lst):` binds `i` to the index (from 0) and `item` to
  the value each pass.
- A second argument sets the **starting number**: `enumerate(lst, 1)` numbers
  from 1, handy for human-facing lists.
- It's lazy (yields pairs on demand) and works on any iterable.

```python
for i, name in enumerate(["a", "b"], 1):
    print(i, name)        # 1 a / 2 b
```
""",

"5.6 brief": r"""# 5.6 -- zip(): pairing lists

## Concept

Two lists often belong together item-by-item: names and scores, questions and
answers. `zip()` walks them **in step**, handing you one pair per pass:

```python
names = ["amy", "ben"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)
# amy 90
# ben 85
```

Like `enumerate`, each pass gives a pair that you unpack into two variables.
The name is the image of a zipper: two rows of teeth joined one-to-one.

If the lists have different lengths, `zip` stops at the **shorter** one --
extra items on the longer list are simply never visited.

## Example

```python
for a, b in zip("ab", [1, 2]):
    print(a, b)
# a 1
# b 2
```

## Your task

Read a count `n`, then `n` names, then `n` scores (whole numbers). Print one
line per pair: the name, a space, the score.

For input `2`, then `amy`, `ben`, then `90`, `85`:

```
amy 90
ben 85
```

## Done when

- Two names and two scores print as two `name score` lines, in order.
- A count of `0` prints nothing.
- You used `zip()` to pair the two lists.
""",

"5.6 hints": r"""Read ALL the names into one list first, then all the scores into another --
only then pair them.

---

`for name, score in zip(names, scores):` gives one pair per pass; print the
two with a space between (plain `print(name, score)` does that).

---

n = int(input())
names = []
for _ in range(n):
    names.append(input())
scores = []
for _ in range(n):
    scores.append(input())
for name, score in zip(names, scores):
    print(name, score)
""",

"5.6 reference": r"""**`zip(a, b)`** walks several iterables **in step**, yielding one tuple of
matching items per pass — the *i*-th from each. It pairs up parallel sequences
without indexing.

- `for x, y in zip(xs, ys):` binds `x` and `y` to the matching items each pass.
- It stops at the **shortest** input, so extra items in a longer one are ignored.
- Any number of iterables can be zipped; `dict(zip(keys, values))` builds a dict
  from two parallel lists.

```python
names, scores = ["Ada", "Linus"], [90, 85]
for n, s in zip(names, scores):
    print(n, s)           # Ada 90 / Linus 85
```
""",

"5.7 brief": r"""# 5.7 -- List comprehensions

## Concept

A very common loop shape is *"build a new list by doing something to each
item"*:

```python
doubled = []
for x in nums:
    doubled.append(x * 2)
```

Python has a one-line form of exactly that, called a **list comprehension**:

```python
doubled = [x * 2 for x in nums]
```

Read it inside-out: *"for each `x` in `nums`, put `x * 2` in a new list"*. The
square brackets say "I am building a list"; the expression before `for` is
what each item becomes.

It works with anything you can loop over -- including `range`. Reading `n`
numbers (which you have done a dozen times now) collapses to:

```python
nums = [int(input()) for _ in range(n)]
```

## Example

```python
nums = [1, 2, 3]
squares = [x * x for x in nums]
print(squares)    # [1, 4, 9]
```

## Your task

Read a count `n`, then `n` whole numbers. Build a new list where every number
is **doubled**, then print its items one per line.

For input `3`, then `4`, `-1`, `0`:

```
8
-2
0
```

## Done when

- `4, -1, 0` prints `8, -2, 0` -- each doubled, order kept.
- A count of `0` prints nothing.
- You used a list comprehension to build a list.
""",

"5.7 hints": r"""The pattern is  new_list = [<what each item becomes> for x in old_list].

---

`doubled = [x * 2 for x in nums]` -- then a plain for loop prints each item.
(Reading the numbers can be a comprehension too: `[int(input()) for _ in range(n)]`.)

---

n = int(input())
nums = [int(input()) for _ in range(n)]
doubled = [x * 2 for x in nums]
for d in doubled:
    print(d)
""",

"5.7 reference": r"""A **list comprehension** builds a new list in one expression: for each `x` in
`items`, it evaluates `expr` and collects the results, in order. It is the
build-by-loop-and-append pattern compressed into a line.

- `[expr for x in items]` is equivalent to starting `result = []` and
  `result.append(expr)` in a loop — same result, more direct.
- `expr` can be any expression in `x`: `[n * n for n in nums]`,
  `[w.upper() for w in words]`.
- Comprehensions also build sets (`{...}`) and dicts (`{k: v for ...}`).

```python
[n * n for n in range(5)]       # [0, 1, 4, 9, 16]
[w.upper() for w in ["a", "b"]] # ['A', 'B']
```
""",

"5.8 brief": r"""# 5.8 -- Filtering with comprehensions

## Concept

A comprehension can also **choose** which items to keep. Add an `if` at the
end:

```python
evens = [x for x in nums if x % 2 == 0]
```

Read it: *"each `x` from `nums` -- but only if `x % 2 == 0`"*. Items that fail
the test are simply left out.

The two parts are independent and combine freely:

```python
[x * 2 for x in nums]                 # transform every item   (5.7)
[x for x in nums if x > 0]            # keep some, unchanged   (this puzzle)
[x * 2 for x in nums if x > 0]        # keep some AND transform
```

Reminder from 1.9: `x % 2` is the remainder of dividing by 2, so it is `0`
exactly for even numbers -- and that includes `0` itself and negatives like
`-4`.

## Example

```python
nums = [1, 2, 3, 4]
print([x for x in nums if x % 2 == 0])    # [2, 4]
```

## Your task

Read a count `n`, then `n` whole numbers. Keep only the **even** ones (in
their original order) and print them one per line.

For input `5`, then `1`, `2`, `3`, `4`, `-6`:

```
2
4
-6
```

## Done when

- `1, 2, 3, 4, -6` prints `2, 4, -6` -- negatives and zero count as even.
- If no number is even, nothing is printed.
- You used a comprehension with an `if` clause.
""",

"5.8 hints": r""""Even" means the remainder after dividing by 2 is zero: `x % 2 == 0`.

---

Put that test at the end of the comprehension:
`evens = [x for x in nums if x % 2 == 0]` -- then print each item.

---

n = int(input())
nums = [int(input()) for _ in range(n)]
evens = [x for x in nums if x % 2 == 0]
for e in evens:
    print(e)
""",

"5.8 reference": r"""Adding an **`if`** to a comprehension keeps only the items that pass the test.
`[x for x in items if test]` collects each `x` for which `test` is true,
**skipping** the rest.

- The `if` clause filters; the leading expression still transforms, so the two
  combine: `[n * n for n in nums if n % 2 == 0]` squares only the evens.
- It replaces the loop-with-an-`if`-and-`append` pattern.
- Don't confuse it with a **conditional expression** in the value position
  (`[a if cond else b for x in items]`), which chooses per item rather than
  filtering.

```python
[n for n in range(10) if n % 2 == 0]   # [0, 2, 4, 6, 8]
[w for w in words if len(w) > 3]       # only long words
```
""",

"5.9 brief": r"""# 5.9 -- Counting with a dict

## Concept

*"How many times does each thing appear?"* is one of the most useful questions
in programming. The answer is the **tally pattern**: a dict where each key is a
thing you have seen and its value is how many times you have seen it.

The whole trick is one line, built on `.get()` from 4.10:

```python
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
```

Read the line slowly: *"the count for `w` becomes whatever it was -- or 0 if
`w` is new -- plus one."* `.get(w, 0)` is what makes the first sighting work:
there is no entry yet, so it counts up from 0.

After the loop, `counts.get(thing, 0)` answers "how many?" for anything --
including things never seen, which are `0`, not a crash.

## Example

```python
words = ["tea", "milk", "tea"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts.get("tea", 0))     # 2
print(counts.get("cocoa", 0))   # 0
```

## Your task

Read one line of words (separate them with `.split()`, like 4.4), then read a
**query word** on a second line. Print how many times the query appears in the
line.

For input `tea milk tea`, then `tea`:

```
2
```

## Done when

- `tea milk tea` with query `tea` prints `2`; query `milk` prints `1`.
- A query that never appears prints `0` (no crash).
- You built a dict tally (not a one-off scan).
""",

"5.9 hints": r"""Split the line into a list of words, then loop over it building the tally dict.

---

The tally line is  counts[w] = counts.get(w, 0) + 1  -- and the final answer is
another .get with a default: counts.get(query, 0).

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
query = input()
print(counts.get(query, 0))
""",

"5.9 reference": r"""The **tally** pattern counts how many times each distinct thing appears, using a
dict whose keys are the things and whose values are running counts.

- For each item, `counts[k] = counts.get(k, 0) + 1` reads the current count
  (`0` the first time the key is seen, via `.get`'s default) and writes one more.
- Start from an empty dict `{}`; keys appear as they're first encountered.
- The standard-library `collections.Counter` does this in one step, but the
  `.get(k, 0) + 1` idiom shows exactly what's happening.

```python
counts = {}
for w in ["a", "b", "a"]:
    counts[w] = counts.get(w, 0) + 1   # {'a': 2, 'b': 1}
```
""",

"5.10 brief": r"""# 5.10 -- Capstone: word report

## Concept

Nothing new this time -- this puzzle combines the chapter (and chapter 4) into
one small, real program: a **word frequency report**, the heart of every
"most common words" feature you have ever seen.

The pieces, all of which you have:

- `.split()` -- the line into words (4.4)
- the tally pattern -- count each word (5.9)
- `sorted()` -- order the report (5.4). One new convenience: looping over a
  dict visits its **keys**, so `sorted(counts)` is simply the keys in
  alphabetical order.
- printing a word and its count on one line (1.2)

## Example

For the line `b a b`:

```python
counts = {"b": 2, "a": 1}
for w in sorted(counts):
    print(w, counts[w])
# a 1
# b 2
```

## Your task

Read one line of words. Print one line per **distinct** word -- the word, a
space, and how many times it appeared -- in **alphabetical** order.

For input `tea milk tea`:

```
milk 1
tea 2
```

## Done when

- `tea milk tea` prints `milk 1` then `tea 2` -- distinct words, alphabetical.
- A single repeated word prints one line with its full count.
- An empty line prints nothing.
- You used a dict tally and `sorted()`.
""",

"5.10 hints": r"""Three steps: split the line, tally the words (5.9), then print -- and
`sorted(counts)` gives the dict's keys in alphabetical order.

---

After the tally loop:  `for w in sorted(counts): print(w, counts[w])`.

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
for w in sorted(counts):
    print(w, counts[w])
""",

"5.10 reference": r"""A **word-frequency report** composes the chapter's tools into a small pipeline:

1. **`split()`** the text into a list of words;
2. **tally** them into a dict of `word -> count` with `counts.get(w, 0) + 1`;
3. **`sorted`** the `dict.items()` to order the report — by word, or by count
   with `key=lambda kv: kv[1]` (and `reverse=True` for most-frequent first).

Each step is a tool you've met; the skill is seeing that a real task is their
composition.

```python
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
for word, n in sorted(counts.items(), key=lambda kv: kv[1], reverse=True):
    print(word, n)        # most frequent first
```
""",

"6.1 brief": r"""# 6.1 -- def: your first function

## Concept

A **function** is a named, reusable piece of code. You have *called* functions
all along -- `print()`, `len()`, `sorted()`. Now you get to **define** your
own:

```python
def double(x):
    return x * 2
```

- `def` starts the definition; `double` is the name you choose.
- `x` is a **parameter**: a variable that receives whatever value the caller
  passes in.
- `return` hands a value **back to the caller**. Calling `double(3)` is then
  an expression worth `6`:

```python
result = double(3)     # result is 6
print(double(10))      # 20
```

**This chapter checks your code differently.** Until now your file *ran* and
printed. From here, the checker **imports** your file and **calls your
functions directly**, passing in many different arguments -- so there is no
`input()` and no `print()` needed at all. Your file just defines the function.

## Example

```python
def double(x):
    return x * 2
```

That whole file is a valid answer to this puzzle: it defines `double`, and
`double(21)` returns `42`.

## Your task

Define a function `double(x)` that **returns** `x` doubled.

## Done when

- `double(3)` returns `6`, `double(0)` returns `0`, `double(-5)` returns `-10`.
- Your file only defines the function -- no `input()`, no `print()`.
""",

"6.1 hints": r"""The shape is:  def name(parameter):  then an indented body that returns
something.

---

`def double(x):` on the first line; the body is one line: return x times 2.

---

def double(x):
    return x * 2
""",

"6.1 reference": r"""A **function** packages a piece of work under a name so it can be run on demand,
as many times as needed. **`def`** introduces one: a header `def name():` and an
indented body.

- **Calling** it — `name()` — runs the body. Defining a function does not run it;
  the call does.
- **`return value`** hands a result back to the caller and ends the function
  immediately. The call expression `name()` then *becomes* that value.
- A function with no `return` (or a bare `return`) hands back `None`.

```python
def greet():
    return "hello"

greet()        # 'hello'  -- the call evaluates to the returned value
```
""",

"6.2 brief": r"""# 6.2 -- Two parameters

## Concept

A function can take several parameters -- list them with commas, and the
caller's values arrive **in the same order**:

```python
def rect_area(width, height):
    return width * height

rect_area(3, 4)     # 12  (width=3, height=4)
```

Inside the body, the parameters are ordinary variables. Everything you know
already works on them -- arithmetic, comparisons, f-strings, loops.

A subtlety worth meeting early: parameters are **local** to the function. The
`width` inside `rect_area` exists only while a call is running; it is not
visible (and does not clash with) anything outside.

## Example

```python
def diff(a, b):
    return a - b

print(diff(10, 4))   # 6
print(diff(4, 10))   # -6  -- order matters
```

## Your task

Define `rect_area(width, height)` that returns the area of a rectangle
(width times height).

## Done when

- `rect_area(3, 4)` returns `12`; `rect_area(4, 3)` does too.
- A zero side returns `0`.
- No `input()`, no `print()` -- the checker passes the values in.
""",

"6.2 hints": r"""Two parameters are listed with a comma:  def rect_area(width, height):

---

The body is one line: return the product of the two parameters.

---

def rect_area(width, height):
    return width * height
""",

"6.2 reference": r"""A **parameter** is a name in the function header that stands for a value the
caller supplies. The values passed in a call are the **arguments**, matched to
parameters left to right.

- `def f(a, b):` declares two parameters; `f(3, 4)` calls with `a = 3`, `b = 4`.
- Parameters are **local**: they exist only during the call and don't clash with
  names outside. The function works on whatever it's given, making it reusable.
- Passing the wrong number of arguments raises `TypeError`.

```python
def add(a, b):
    return a + b

add(3, 4)      # 7
```
""",

"6.3 brief": r"""# 6.3 -- return, not print

## Concept

`print()` and `return` look similar when you test by eye, but they do
completely different jobs:

- `print(x)` **shows** `x` on the screen -- and that's all. The caller gets
  nothing.
- `return x` **hands `x` back** to the caller, who can store it, compare it,
  or pass it on.

A function that prints instead of returning actually returns `None` (the
"no value" value). The difference bites the moment someone *uses* the result:

```python
def shout_wrong(word):
    print(word.upper() + "!")     # shows it... returns None

answer = shout_wrong("hi")        # HI! appears, but...
print(answer)                     # None  -- the caller got nothing
```

The rule: **a function's job is to compute and return.** Let the *caller*
decide whether to print.

## Example

```python
def shout(word):
    return word.upper() + "!"

print(shout("hi"))      # HI!  -- printed BY THE CALLER
loud = shout("ok")      # and it can be stored instead
```

## Your task

Define `shout(word)` that **returns** the word in UPPERCASE with a `!` stuck
on the end. (`.upper()` is from 2.7.)

## Done when

- `shout("hi")` returns `"HI!"`; `shout("")` returns `"!"`.
- The value is *returned* -- a version that only prints will fail, because the
  checker receives `None`.
""",

"6.3 hints": r"""If the checker says it got None, your function printed instead of returning.

---

Build the string with .upper() and + "!", then return it -- no print anywhere.

---

def shout(word):
    return word.upper() + "!"
""",

"6.3 reference": r"""**Returning** a value and **printing** it are different acts, and confusing them
is a common bug.

- **`return`** hands a value back to the calling code, which can store it, do
  arithmetic on it, or pass it on. The value travels.
- **`print`** writes text to the screen and returns `None`. The value is shown but
  not captured — `x = print(5)` makes `x` be `None`.
- A function that prints instead of returning can't be built on. Prefer to
  `return` the result and let the **caller** decide whether to print it.

```python
def double(n):
    return n * 2        # caller can use it
print(double(5) + 1)    # 11  -- works because double returned
```
""",

"6.4 brief": r"""# 6.4 -- Default values

## Concept

A parameter can carry a **default**: the value used when the caller leaves it
out. Write it with `=` in the `def` line:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Ada")              # "Hello, Ada!"   -- default used
greet("Ada", "Hi")        # "Hi, Ada!"      -- default overridden
```

You have already *used* this: `print(..., sep=" ")` from 1.3 -- `sep` has a
default of one space, which you overrode with `sep=", "`. Now you can build
the same flexibility into your own functions.

Rules: parameters with defaults go **after** the ones without, and the
default is used *only* when the caller omits that argument.

## Example

```python
def repeat(word, times=2):
    return word * times

repeat("ha")        # "haha"
repeat("ha", 3)     # "hahaha"
```

## Your task

Define `greet(name, greeting="Hello")` that returns `"<greeting>, <name>!"` --
exactly: the greeting, a comma and a space, the name, an exclamation mark.

## Done when

- `greet("Ada")` returns `"Hello, Ada!"` (the default at work).
- `greet("Ada", "Hi")` returns `"Hi, Ada!"`.
- Without the default, the one-argument call would crash -- the checker makes
  both kinds of call.
""",

"6.4 hints": r"""The default goes in the def line:  def greet(name, greeting="Hello"):

---

Build the result with an f-string: the greeting, then ", ", then the name,
then "!".

---

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
""",

"6.4 reference": r"""A **default value** in the header makes a parameter optional: if the caller omits
that argument, the default is used.

- `def greet(name, greeting="hi"):` can be called `greet("Ada")` (uses `"hi"`) or
  `greet("Ada", "hello")` (overrides it).
- Parameters **with** defaults must come **after** those without.
- Use a *new* default each call for mutable types — write `def f(items=None):`
  then `if items is None: items = []`, never `def f(items=[]):` (one shared list
  persists between calls).

```python
def power(base, exp=2):
    return base ** exp

power(5)       # 25  -- exp defaults to 2
power(5, 3)    # 125
```
""",

"6.5 brief": r"""# 6.5 -- return ends the function

## Concept

`return` doesn't just hand back a value -- it **stops the function on the
spot**. Nothing after an executed `return` runs. That makes branching
functions read cleanly: settle each case and leave.

```python
def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
```

Notice there is no `else` -- none is needed. If the first `return` fired, the
function is already over; reaching the last line *means* `n` was positive.
This style is called an **early return**.

A function with several `return` statements still returns exactly **one**
value per call: whichever `return` runs first.

## Example

```python
sign(-3)    # "negative"
sign(0)     # "zero"
sign(42)    # "positive"
```

## Your task

Define `sign(n)` that returns `"negative"`, `"zero"`, or `"positive"` for a
whole number `n`.

## Done when

- `sign(-3)`, `sign(0)`, `sign(42)` return the three words above.
- The boundary cases `-1` and `1` are right too.
""",

"6.5 hints": r"""Each case is an if with its own return. Once a return runs, the function is
over.

---

Check `n < 0` first, then `n == 0`; if neither returned, n must be positive --
just return "positive" with no condition.

---

def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
""",

"6.5 reference": r"""A `return` can appear **anywhere** in a function, and reaching it ends the call at
once — later lines don't run. An **early return** uses this to handle a case and
leave immediately.

- It flattens code: handle the special or invalid case up front with a guard
  (`if bad: return ...`), then write the main path without nesting it in an
  `else`.
- The first `return` reached wins; nothing after it in that call executes.

```python
def reciprocal(n):
    if n == 0:
        return None     # bail out early on the bad case
    return 1 / n        # main path, not indented under an else
```
""",

"6.6 brief": r"""# 6.6 -- Returning two values

## Concept

`return` can hand back **several values at once** -- separate them with a
comma and Python packs them into a **tuple** (4.7):

```python
def min_max(nums):
    return min(nums), max(nums)
```

The caller can keep the tuple, or unpack it straight into variables -- the
same unpacking you used for `a, b = b, a`:

```python
pair = min_max([3, 1, 4])     # (1, 4)  -- one tuple
lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4  -- unpacked
```

This is how Python functions return "two answers" -- there is no special
trick, just a tuple and unpacking.

## Example

```python
def split_name(full):
    parts = full.split()
    return parts[0], parts[-1]

first, last = split_name("Ada King Lovelace")
# first = "Ada", last = "Lovelace"
```

## Your task

Define `min_max(nums)` that returns the smallest and largest item of a
non-empty list, **in that order**, as a tuple. (`min()`/`max()` are from 5.3.)

## Done when

- `min_max([3, 1, 4])` returns `(1, 4)` -- a tuple, smallest first.
- `min_max([7])` returns `(7, 7)`.
- Negative numbers work.
""",

"6.6 hints": r"""Two values after one return, separated by a comma, come back as a tuple.

---

You already have both halves from 5.3: `return min(nums), max(nums)`.

---

def min_max(nums):
    return min(nums), max(nums)
""",

"6.6 reference": r"""A function returns **one** object, but that object can be a **tuple**, so
`return a, b` hands back several values at once (Python packs them into a tuple).
The caller **unpacks** them with matching names.

- `return lo, hi` returns the tuple `(lo, hi)`; `low, high = bounds(xs)` unpacks
  it into two names.
- The counts must match on unpacking. Catch the whole tuple with one name if you
  prefer: `result = bounds(xs)` then `result[0]`, `result[1]`.

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4
```
""",

"6.7 brief": r"""# 6.7 -- Building on built-ins

## Concept

Functions shine when they bundle a small *recipe* behind a good name. The
recipe for an average:

> the total, divided by how many there are

You own every ingredient: `sum()` (5.2), `len()` (2.6), and `/` (1.9).
Remember from 1.9 that `/` **always returns a float** -- `4 / 2` is `2.0`,
not `2`. That is correct here: an average is naturally a decimal number.

```python
def average(nums):
    return sum(nums) / len(nums)
```

One function, one line, instantly reusable -- and the name says what the line
means.

## Example

```python
average([1, 2])        # 1.5
average([10, 20, 30])  # 20.0
```

## Your task

Define `average(nums)` that returns the average of a non-empty list of
numbers.

## Done when

- `average([1, 2])` returns `1.5`; `average([10, 20, 30])` returns `20.0`.
- The result is a **float** even when the division is exact (use `/`,
  not `//`).
- A one-item list returns that item (as a float).
""",

"6.7 hints": r"""An average is the total divided by the count -- and you have a built-in for
each half.

---

`sum(nums)` over `len(nums)`, with `/` (the float division from 1.9).

---

def average(nums):
    return sum(nums) / len(nums)
""",

"6.7 reference": r"""Functions **compose built-ins** into a named, reusable operation. An `average`
function is the model: it wraps `sum` and `len` behind one clear name.

- `return sum(nums) / len(nums)` computes the mean — but `len(nums)` is `0` for an
  empty list, which raises `ZeroDivisionError`, so guard it with an early return.
- Naming the operation (`average(scores)`) makes calling code read as intent, and
  fixing or improving the logic happens in one place.

```python
def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

average([2, 4, 9])    # 5.0
```
""",

"6.8 brief": r"""# 6.8 -- Functions calling functions

## Concept

Your functions can call **each other**. That is the real power move: solve a
small problem once, name it, and build the next function on top.

```python
def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
```

`same_word` doesn't repeat the strip-and-lower recipe -- it *delegates* to
`clean`. If you ever improve `clean` (say, also removing punctuation), every
function built on it improves for free. Repeating the recipe in both places
is how bugs are born: fix one copy, forget the other.

Note `same_word` returns the result of a comparison -- a **boolean**
(`True`/`False`), like 3.1. No `if` needed: `clean(a) == clean(b)` already
*is* the answer.

## Example

```python
clean("  Tea ")              # "tea"
same_word("  Tea ", "tea")   # True
same_word("tea", "milk")     # False
```

## Your task

Define **both** functions:

- `clean(text)` -- returns the text with surrounding spaces stripped and
  lowercased (2.7).
- `same_word(a, b)` -- returns `True` exactly when the two texts are the same
  after cleaning. It must **call `clean`** rather than redo the recipe.

## Done when

- `clean("  Tea ")` returns `"tea"`.
- `same_word("  Tea ", "tea")` is `True`; `same_word("tea", "milk")` is `False`.
- `same_word` calls `clean` -- the checker looks for the delegation.
""",

"6.8 hints": r"""Write clean first and get it passing in your head: .strip() then .lower(),
chained.

---

same_word is one line: compare clean(a) with clean(b) using == and return the
result -- a comparison already IS True or False.

---

def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
""",

"6.8 reference": r"""Functions **call other functions**, so a larger task is built from small, tested
pieces. The result of one becomes the argument or building block of the next.

- A helper does one job well; a higher-level function calls several helpers and
  combines their results. This is the core of structuring a program.
- `f(g(x))` feeds `g`'s result straight into `f`. Each function stays simple and
  independently checkable.

```python
def clean(s):  return s.strip().lower()
def is_yes(s): return clean(s) == "yes"

is_yes("  YES ")   # True  -- is_yes builds on clean
```
""",

"6.9 brief": r"""# 6.9 -- Recursion: a function calling itself

## Concept

A function may call **itself**. That is called **recursion**, and it works
whenever a problem contains a smaller copy of the same problem.

The factorial is the classic: `5!` means `5 * 4 * 3 * 2 * 1`. But look again:

> `5!` is just `5 * 4!` -- and `4!` is `4 * 3!` ...

A recursive function states exactly that, plus a **base case** -- the smallest
input answered directly, with no further calls:

```python
def fact(n):
    if n == 0:
        return 1            # base case: 0! is 1
    return n * fact(n - 1)  # the smaller copy of the same problem
```

`fact(3)` runs as `3 * fact(2)` -> `3 * 2 * fact(1)` -> `3 * 2 * 1 * fact(0)`
-> `3 * 2 * 1 * 1` = `6`. Without the base case the calls would never stop --
recursion's version of an endless loop.

You could compute a factorial with a `for` loop -- but the *lesson* here is the
self-call, so this puzzle requires it.

## Example

```python
fact(0)    # 1
fact(3)    # 6
fact(5)    # 120
```

## Your task

Define `fact(n)` that returns `n!` **recursively**: a base case for `0`, and
`n * fact(n - 1)` for the rest. `n` is never negative.

## Done when

- `fact(0)` is `1`, `fact(1)` is `1`, `fact(5)` is `120`.
- `fact` calls itself -- the checker looks for the self-call, so a loop
  version won't pass.
""",

"6.9 hints": r"""Answer the smallest case first: if n is 0, return 1 -- no call needed.

---

For everything else, trust the function you are writing:
return n * fact(n - 1). The early return (6.5) keeps the base case clean.

---

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
""",

"6.9 reference": r"""A **recursive** function calls **itself** to solve a smaller version of the same
problem. Two parts are essential:

- a **base case** that returns directly **without** recursing — this stops the
  recursion;
- a **recursive case** that calls the function on a smaller input and builds on
  the result, moving toward the base case each time.

Miss or never reach the base case and the calls nest until Python raises
`RecursionError`. Many recursions have a simpler loop form; recursion shines when
the problem is itself self-similar.

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)   # smaller subproblem

factorial(4)   # 24
```
""",

"6.10 brief": r"""# 6.10 -- Capstone: a tiny library

## Concept

Nothing new -- this capstone is the chapter in miniature: several functions,
each with one clear job, the later ones **delegating** to the earlier ones
(6.8). A file of related functions like this is the seed of every real
*library* you will ever import.

The pieces: `for ch in word` (3.10), `in` (5.1), the tally idea (5.9),
f-strings (2.10), and early returns (6.5).

## Example

```python
count_vowels("tea")        # 2   ("e" and "a")
count_vowels("xyz")        # 0
describe("tea")            # "tea has 2 vowels"
describe("xyz")            # "xyz has no vowels"
```

## Your task

Define **both** functions:

- `count_vowels(word)` -- returns how many characters of `word` are vowels
  (`a`, `e`, `i`, `o`, `u`; the words are lowercase).
- `describe(word)` -- returns the string `"<word> has <n> vowels"`, except
  when the count is zero: then it is `"<word> has no vowels"`. It must **call
  `count_vowels`**.

## Done when

- `count_vowels("tea")` is `2`; `count_vowels("xyz")` is `0`.
- `describe("tea")` is `"tea has 2 vowels"`; `describe("xyz")` is
  `"xyz has no vowels"`.
- `describe` delegates to `count_vowels` -- the checker looks for the call.
""",

"6.10 hints": r"""count_vowels is a tally over the characters: loop with `for ch in word` and
test `ch in "aeiou"`.

---

describe calls count_vowels once, stores the number, then early-returns the
"no vowels" wording when it is 0; otherwise an f-string with the count.

---

def count_vowels(word):
    count = 0
    for ch in word:
        if ch in "aeiou":
            count = count + 1
    return count

def describe(word):
    n = count_vowels(word)
    if n == 0:
        return f"{word} has no vowels"
    return f"{word} has {n} vowels"
""",

"6.10 reference": r"""A **library** here means a set of related functions you've written, each named
for its job, that together form a reusable toolkit — the payoff of the chapter.

- Build small functions that each do one thing and `return` their result; then
  higher-level functions call them. Calling code reads as a sequence of intents.
- Keeping logic inside named functions (rather than copied inline) means a fix or
  improvement lands in one place and every caller benefits.

```python
def clean(s):    return s.strip().lower()
def words(s):    return clean(s).split()
def wordcount(s): return len(words(s))

wordcount("  The quick fox ")   # 3  -- each function builds on the last
```
""",

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

"8.1 brief": r"""# 8.1 -- Opening a file

## Concept

So far every value came from a literal you typed or from `input()`. Real
programs also read **files** -- text already sitting on disk.

`open(name)` hands you a *file object*. The clean way to use one is a `with`
block:

```python
with open("note.txt") as f:
    text = f.read()
```

- `with open(...) as f:` opens the file and binds it to `f`;
- `f.read()` returns the file's **entire contents** as one string;
- when the block ends, Python **closes the file for you** -- even if the code
  inside raised. That automatic close is the whole reason to prefer `with`
  over a bare `open()`.

The file is found relative to where the program runs, so `"note.txt"` means "a
file called note.txt next to me".

## Example

If `note.txt` contains:

```
buy milk
call sam
```

then `text` is the string `"buy milk\ncall sam\n"` -- newlines and all.

## Your task

A file named `note.txt` sits beside your program. Read its whole contents and
print them.

## Done when

- The program prints exactly what `note.txt` contains.
- It works whatever the file holds -- one line, many lines, or nothing.
- You opened the file with a `with` statement.
""",

"8.1 hints": r"""A `with open(name) as f:` block gives you the file as `f`. Inside it, ask the
file for everything it holds.

---

`f.read()` returns the whole file as a single string. Store it, then print it
after (or inside) the block.

---

with open("note.txt") as f:
    text = f.read()
print(text)
""",

"8.1 reference": r"""**`open(name)`** connects to a file on disk; the **`with`** statement manages it
so the file is **closed automatically** when the block ends, even if an error
occurs. Inside the block, the file object `f` provides the contents.

- `with open(name) as f:` opens for **reading** text (the default mode `"r"`) and
  binds the open file to `f`.
- **`f.read()`** returns the entire contents as one string. (`f.read(n)` reads at
  most `n` characters.)
- Opening a path that doesn't exist raises `FileNotFoundError`. Always use `with`
  rather than a bare `open` — it guarantees the close.

```python
with open("notes.txt") as f:
    text = f.read()      # whole file as a string
# file is closed here
```
""",

"8.2 brief": r"""# 8.2 -- A file, line by line

## Concept

`f.read()` gives you everything at once. More often you want the file **one
line at a time** -- and a file object is *iterable*, so a `for` loop walks its
lines for you:

```python
with open("tasks.txt") as f:
    for line in f:
        ...
```

One catch: each `line` still carries the newline that ended it -- `"wash\n"`,
not `"wash"`. Strip it with `line.strip()` (3.7) before you use the text, or
your output grows blank lines.

## Example

For a `tasks.txt` of:

```
wash
cook
sleep
```

numbering each line gives:

```
1. wash
2. cook
3. sleep
```

`enumerate` (5.5) is the natural fit -- start it at `1`:

```python
for i, line in enumerate(f, start=1):
    print(f"{i}. {line.strip()}")
```

## Your task

Read `tasks.txt` and print every line **numbered from 1**, in the form
`1. wash`. Drop the trailing newline so there are no stray blank lines.

## Done when

- Each line is printed as `<number>. <text>`, counting from 1.
- It works for a file of any length.
- You opened the file with `with` and looped over it with `for`.
""",

"8.2 hints": r"""A file object is iterable: `for line in f:` hands you one line per pass.

---

`enumerate(f, start=1)` gives `(1, firstline), (2, secondline), ...`. Each line
still ends in `\n` -- use `line.strip()` to drop it.

---

with open("tasks.txt") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")
""",

"8.2 reference": r"""A file object is **iterable**: looping over it yields the file **one line at a
time**, without loading the whole thing into memory. This is the standard way to
process a file line by line.

- `for line in f:` binds `line` to each line **including its trailing newline**
  `"\n"`; call `line.strip()` (or `.rstrip("\n")`) to drop it.
- It reads lazily, so it handles large files comfortably.
- `f.readlines()` instead returns a **list** of all lines at once — fine for
  small files, wasteful for big ones.

```python
with open("log.txt") as f:
    for line in f:
        print(line.strip())   # one line per pass, newline removed
```
""",

"8.3 brief": r"""# 8.3 -- Adding up a file

## Concept

A file is always **text**. A line that looks like `42` arrives as the string
`"42\n"`, not the number 42 -- so before you can do arithmetic you must convert
it with `int()` (1.11), exactly as you did with `input()`.

`int()` is happy to ignore the surrounding whitespace, so `int("42\n")` is
`42` -- you don't even need to strip first.

```python
total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
```

## Example

For a `prices.txt` of:

```
10
25
7
```

the total is `42`.

## Your task

`prices.txt` holds one whole number per line. Read them, add them all up, and
print the total.

## Done when

- The program prints the sum of every number in the file.
- Negative numbers and a single-line file both work.
- You opened the file with `with` and converted each line with `int()`.
""",

"8.3 hints": r"""Start a running total at 0, open the file, and loop over its lines.

---

Each line is a string like `"25\n"`. `int(line)` turns it into a number you can
add. Print the total after the loop.

---

total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
print(total)
""",

"8.3 reference": r"""File contents are always **text**, so a line like `"42\n"` is a *string*. To do
arithmetic you must convert each line to a number first.

- `int(line)` parses an integer; it tolerates surrounding whitespace (including
  the trailing newline), so `int("42\n")` is `42`. Use `float(line)` for
  decimals.
- A blank or non-numeric line raises `ValueError` — skip blanks
  (`if not line.strip(): continue`) or wrap the conversion in `try`.
- Accumulate as you go: keep a running total and add each parsed value.

```python
total = 0
with open("nums.txt") as f:
    for line in f:
        total += int(line)    # text -> number, then add
```
""",

"8.4 brief": r"""# 8.4 -- Writing a file

## Concept

Reading is half the story; programs also **create** files. Open with the mode
`"w"` (for *write*) and call `.write()`:

```python
with open("out.txt", "w") as f:
    f.write("hello\n")
```

Two things to know:

- `"w"` makes a brand-new file (or **empties** an existing one), then writes.
- `.write()` puts down **exactly** the text you give it -- no automatic
  newline like `print()` adds. If you want line breaks, include `"\n"`
  yourself.

A common shape is **read one file, write another**:

```python
with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
```

## Example

If `in.txt` contains `quiet please`, then `out.txt` should end up holding
`QUIET PLEASE`.

## Your task

Read `in.txt`, and write its contents **in upper case** (7.x `.upper()` from
2.7) into a new file called `out.txt`.

## Done when

- `out.txt` contains exactly the text of `in.txt`, uppercased.
- An empty `in.txt` produces an empty `out.txt` -- no crash.
- You used `with` and opened `out.txt` in `"w"` mode.
""",

"8.4 hints": r"""Two steps: first read in.txt into a string, then open out.txt in `"w"` mode and
write the uppercased string.

---

`open("out.txt", "w")` is the write half; `text.upper()` does the uppercasing.
`.write()` writes the string as-is.

---

with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
""",

"8.4 reference": r"""Opening with mode **`"w"`** opens a file for **writing**. It **creates** the file
if absent and **truncates** it (empties it) if it already exists, so existing
contents are lost.

- **`f.write(text)`** writes a string and, unlike `print`, adds **no** trailing
  newline — include `"\n"` yourself where you want line breaks.
- `f.write` takes strings only; convert numbers with `str()` or an f-string
  first.
- Use `with` so the data is flushed and the file closed properly.

```python
with open("out.txt", "w") as f:
    f.write("first line\n")
    f.write("second line\n")   # newlines are explicit
```
""",

"8.5 brief": r"""# 8.5 -- Append, don't overwrite

## Concept

Mode `"w"` is ruthless: it **empties** the file before writing. That's wrong
when you want to *add* to a file -- a log you keep growing, say. For that there
is mode `"a"` (for *append*):

```python
with open("log.txt", "a") as f:
    f.write("another line\n")
```

`"a"` leaves everything already in the file untouched and writes your new text
**after** it (and if the file doesn't exist yet, `"a"` simply creates it).
Same `.write()`, same need to add your own `"\n"` -- only the mode letter
changes, and that one letter is the whole difference between "add to" and
"wipe and replace". The whole point of `"a"` is that you *don't* read the file
first -- you just write at the end.

## Example

If `log.txt` already contains:

```
woke up
ate
```

then appending the line `ran` leaves it holding `woke up`, `ate`, `ran` -- all
three, in order.

## Your task

A file `log.txt` already exists. Read one line of text from input (`input()`)
and **append** it to `log.txt` as a new line, keeping everything already there.

## Done when

- The original contents of `log.txt` are still present, in order.
- The new entry is added as its own line at the end.
- Using `"w"` would erase the old lines -- so you must use `"a"`.
""",

"8.5 hints": r"""Read the entry with `input()`, then open the file in a mode that *keeps* what
is already there.

---

Mode `"a"` appends instead of wiping. Don't forget the `"\n"` so the new entry
sits on its own line.

---

entry = input()
with open("log.txt", "a") as f:
    f.write(entry + "\n")
""",

"8.5 reference": r"""Mode **`"a"`** opens a file for **appending**: writes go to the **end**, and any
existing contents are kept. It's the non-destructive counterpart to `"w"`.

- `"a"` creates the file if it doesn't exist; if it does, `f.write` adds after
  what's already there — nothing is overwritten.
- `"w"` empties the file first; reach for `"a"` to grow a log or accumulate
  results across runs.
- As with `"w"`, newlines are not added for you.

```python
with open("log.txt", "a") as f:
    f.write("another entry\n")   # added at the end, old lines kept
```
""",

"8.6 brief": r"""# 8.6 -- Filtering lines into a new file

## Concept

Put reading and writing together and you get the everyday data chore: walk an
input file line by line, **decide** which lines to keep (3.2 `if`), and write
just those to an output file.

```python
with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if keep(line):
            f.write(line)
```

`f.readlines()` reads the whole file into a list of lines up front -- handy
when you want to finish reading before you start writing.

A line that is empty or only spaces is "blank": `line.strip()` returns `""` for
it, and an empty string is falsey (3.1), so `if line.strip():` is a tidy test
for "this line has real content".

## Example

From a `lines.txt` of:

```
keep me

and me
```

the blank middle line is dropped, leaving `keep me` and `and me`.

## Your task

Read `lines.txt` and write only its **non-blank** lines to `kept.txt`, in the
same order. Drop any line that is empty or just whitespace.

## Done when

- `kept.txt` holds exactly the non-blank lines of `lines.txt`, in order.
- A file with no blank lines is copied unchanged; an all-blank file yields an
  empty `kept.txt`.
- You used `with`, a loop, and an `if` to decide what to keep.
""",

"8.6 hints": r"""Read all the lines first, then open the output file in `"w"` mode and loop,
writing only the ones you want to keep.

---

`if line.strip():` is true only when the line has real content. Write the
original `line` (it already ends in `\n`), not a stripped copy.

---

with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if line.strip():
            f.write(line)
""",

"8.6 reference": r"""A **filtering** pass reads one file, keeps only the lines an `if` accepts, and
writes them to another — the file form of the comprehension-with-`if` pattern.

- Open the source for reading and the destination for writing, loop the source,
  and `f_out.write(line)` only when the line passes your test.
- Lines from the input keep their newline, so writing them back reproduces line
  breaks without adding any.
- Reading and writing the **same** path at once is unsafe; write to a new file
  (or collect results, then write).

```python
with open("all.txt") as src, open("kept.txt", "w") as out:
    for line in src:
        if "ERROR" in line:
            out.write(line)       # keep only matching lines
```
""",

"8.7 brief": r"""# 8.7 -- A frequency report

## Concept

This puzzle puts the chapter together with the dictionary tally from 5.9: read
a file, **count** something across it, and write the result to another file.

Read the words in, then tally them with a dict (the `dict.get` pattern):

```python
with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
```

`f.read().split()` reads the whole file and splits on any whitespace, so it
hands you a flat list of words however they were spaced.

Then write the report, **sorted by count, highest first**, ties broken
alphabetically. `sorted` with a `key` (5.4) does both at once:

```python
for w in sorted(counts, key=lambda w: (-counts[w], w)):
    f.write(f"{w}: {counts[w]}\n")
```

The key `(-counts[w], w)` sorts by descending count (negate it) and then by the
word itself for ties.

## Example

A `words.txt` of `fig fig pear fig pear` becomes a `report.txt` of:

```
fig: 3
pear: 2
```

## Your task

Count how often each word appears in `words.txt`, and write `report.txt` with
one `word: count` line per distinct word -- ordered by count (highest first),
ties in alphabetical order.

## Done when

- Each distinct word appears once, as `word: count`.
- Lines are ordered by descending count, alphabetical within a tie.
- You used `with`, a dict to tally, and read the words from the file.
""",

"8.7 hints": r"""Read the words into a list, then build a dict of counts with the
`counts[w] = counts.get(w, 0) + 1` pattern from 5.9.

---

To order the report, sort the dict's keys with a key function:
`sorted(counts, key=lambda w: (-counts[w], w))` gives highest count first,
alphabetical within ties. Write each `f"{w}: {counts[w]}\n"`.

---

with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as f:
    for w in sorted(counts, key=lambda w: (-counts[w], w)):
        f.write(f"{w}: {counts[w]}\n")
""",

"8.7 reference": r"""A **frequency report** is a three-stage file pipeline: **read** the file, **tally**
into a dict, then **write** a sorted summary.

- Loop the lines (or words), counting with `counts[k] = counts.get(k, 0) + 1`.
- Order the result with `sorted(counts.items(), ...)` — by key, or by count with
  `key=lambda kv: kv[1]` (add `reverse=True` for most-frequent first).
- Write each pair as a formatted line, e.g. `out.write(f"{word}: {n}\n")`.

It composes the file I/O of this chapter with the dict and `sorted` tools from
earlier ones.

```python
counts = {}
with open("words.txt") as f:
    for line in f:
        w = line.strip()
        counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as out:
    for w, n in sorted(counts.items()):
        out.write(f"{w}: {n}\n")
```
""",

"8.8 brief": r"""# 8.8 -- Capstone: a ranking report

## Concept

This capstone is a real little program: read a file of records, rank them, and
write a formatted report -- using split (4.4), unpacking (4.7), `int()` (1.11),
`sorted` with a key (5.4), f-strings (2.10), and files (this chapter) together.

`scores.txt` has one record per line, a name and a score separated by a space:

```
alice 40
bob 25
cara 40
```

Each line splits into its two fields:

```python
name, score = line.split()
score = int(score)
```

You want `ranking.txt` to list players from highest score to lowest (ties in
alphabetical order), then a final total line:

```
alice - 40
cara - 40
bob - 25
Total: 105
```

Note the exact format: `name - score` per player (spaces around the dash), and
a closing `Total: <sum>` line.

## Your task

Read `scores.txt`, and write `ranking.txt` with one `name - score` line per
player ordered by score (highest first, ties alphabetical), followed by a final
`Total: <sum of all scores>` line.

## Done when

- Players are listed `name - score`, highest score first, ties alphabetical.
- The last line is `Total: ` followed by the sum of every score.
- A single-player file works, and you used `with` for both files.
""",

"8.8 hints": r"""Read the lines, and for each one `name, score = line.split()`; convert the
score with `int()`. Collect the pairs into a list.

---

Sort with `key=lambda p: (-p[1], p[0])` for highest score first, ties
alphabetical. Write each `f"{name} - {score}\n"`, then a final
`f"Total: {sum_of_scores}\n"`.

---

with open("scores.txt") as f:
    lines = f.read().splitlines()
players = []
for line in lines:
    name, score = line.split()
    players.append((name, int(score)))
players.sort(key=lambda p: (-p[1], p[0]))
total = sum(score for name, score in players)
with open("ranking.txt", "w") as f:
    for name, score in players:
        f.write(f"{name} - {score}\n")
    f.write(f"Total: {total}\n")
""",

"8.8 reference": r"""The capstone reads **records**, parses each into usable fields, ranks them, and
writes a **formatted report** — the shape of real data work.

- **Parse**: split each line into fields and convert types (e.g.
  `name, score = line.split(","); score = int(score)`), collecting the records
  into a list.
- **Rank**: `sorted(records, key=..., reverse=True)` orders by the field that
  matters.
- **Format**: write aligned, human-readable lines, using f-string field widths
  (`f"{name:<12}{score:>5}"`) so columns line up.

```python
records = []
with open("scores.csv") as f:
    for line in f:
        name, score = line.strip().split(",")
        records.append((name, int(score)))
with open("ranked.txt", "w") as out:
    for name, score in sorted(records, key=lambda r: r[1], reverse=True):
        out.write(f"{name:<12}{score:>5}\n")
```
""",

"9.1 brief": r"""# 9.1 -- A first class

## Concept

A **class** is a blueprint for an object that bundles related data together. So
far a dog's name and age would be two loose variables; a class ties them into
one thing you can pass around.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- `class Dog:` names the blueprint.
- `__init__` is the **constructor** -- it runs when you build a new Dog, and its
  job is to set up the object's data.
- `self` is the object being built; `self.name = name` stores the value **on the
  object** so it's still there later.

You build one (an *instance*) by calling the class like a function, and you read
its data with a dot:

```python
d = Dog("Rex", 3)
print(d.name)   # Rex
print(d.age)    # 3
```

## Your task

Define a class `Dog` whose `__init__` takes a `name` and an `age` and stores
each on the object as `self.name` and `self.age`.

## Done when

- `Dog("Rex", 3)` makes an object whose `.name` is `"Rex"` and `.age` is `3`.
- It works for any name and age.
- You used a `class` with an `__init__` that stores both values on `self`.
""",

"9.1 hints": r"""Start with `class Dog:` and give it an `__init__(self, name, age)` method.

---

Inside `__init__`, copy each parameter onto the object with `self.`:
`self.name = name`. That's what makes the value stick.

---

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
""",

"9.1 reference": r"""A **class** defines a new type of object, bundling related data into one value.
**`__init__`** is the initialiser: Python calls it automatically when you create
an instance, to set up its starting data.

- `class Point:` opens the definition; calling `Point(3, 4)` makes an
  **instance** and runs `__init__`.
- **`self`** is the instance being built; `self.x = x` stores a value as an
  **attribute** on it, where every method can later reach it.
- `__init__`'s first parameter is always `self`; the rest are the arguments the
  caller passes.

```python
class Point:
    def __init__(self, x, y):
        self.x = x          # store data on the instance
        self.y = y

p = Point(3, 4)
p.x                         # 3
```
""",

"9.2 brief": r"""# 9.2 -- Methods: behaviour on the data

## Concept

Objects don't just hold data -- they have **methods**, functions that live on
the object and work with its own data through `self`.

```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

`area` is a method: it takes `self` (the object it's called on) and uses
`self.side`. You call it with a dot and parentheses -- no need to pass `self`,
Python fills it in:

```python
s = Square(5)
print(s.area())   # 25
```

The point of a method is that the behaviour travels *with* the data: any Square
already knows how to compute its own area.

## Your task

Define a class `Square` whose `__init__` stores a `side`, and add a method
`area()` that returns the square's area (`side * side`).

## Done when

- `Square(5).area()` returns `25`.
- It works for any side length, including `0`.
- `area` is a method on the class and computes from `self.side`.
""",

"9.2 hints": r"""Store the side in `__init__` like last time, then add a second method `area`.

---

A method takes `self` first: `def area(self):`. Inside, return
`self.side * self.side`.

---

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
""",

"9.2 reference": r"""A **method** is a function defined inside a class. It always takes **`self`**
first and computes from the object's own attributes, so behaviour lives with the
data it acts on.

- Call it with `instance.method()`; Python passes the instance as `self`
  automatically, so `p.dist()` calls `dist(p)`.
- Inside, reach the object's data through `self`: `self.x`, `self.y`.
- A method may take more parameters after `self` and `return` a value like any
  function.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

Point(3, 4).dist()      # 5.0
```
""",

"9.3 brief": r"""# 9.3 -- State that remembers

## Concept

An object's data lives **between** method calls -- a method can change `self`,
and the next call sees the change. That's what makes objects useful: they
*remember*.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count = self.count + 1
        return self.count
```

Each `tick()` bumps `self.count` and hands back the new value:

```python
c = Counter()
c.tick()   # 1
c.tick()   # 2
c.tick()   # 3
```

Crucially, the count lives **on the instance** (`self.count`), so two counters
keep separate tallies -- ticking one never touches the other.

## Your task

Define a class `Counter` that starts its `count` at `0`. Add a method `tick()`
that adds one to the count and **returns the new count**.

## Done when

- A fresh `Counter` ticked three times returns `1`, `2`, `3`.
- Two counters are independent -- ticking one doesn't change the other.
- The count is stored on `self`, not shared across all counters.
""",

"9.3 hints": r"""`__init__` sets the starting point: `self.count = 0`. Then `tick` changes it.

---

Inside `tick`, do `self.count = self.count + 1` (or `self.count += 1`), then
`return self.count`. Keep the count on `self` so each counter has its own.

---

class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1
        return self.count
""",

"9.3 reference": r"""An object holds **state** — data that persists between calls. A method can
**mutate** `self`, and the next method call sees the change, so the object
remembers what happened to it.

- `self.count += 1` updates an attribute in place; the new value lives on until
  changed again.
- This is the point of objects: they carry their data with them across calls,
  unlike a plain function whose locals vanish when it returns.
- Each instance has its **own** copy of the attributes, so two counters count
  independently.

```python
class Counter:
    def __init__(self):
        self.n = 0
    def tick(self):
        self.n += 1         # remembered for next time

c = Counter(); c.tick(); c.tick(); c.n   # 2
```
""",

"9.4 brief": r"""# 9.4 -- More data, more methods

## Concept

A class can hold several pieces of data and offer several methods over them.
Nothing new in the syntax -- just more of it:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

Both methods read the same stored data through `self`; each Rectangle answers
either question about itself:

```python
r = Rectangle(3, 4)
r.area()        # 12
r.perimeter()   # 14
```

## Your task

Define a class `Rectangle` whose `__init__` stores a `width` and a `height`,
with two methods: `area()` returns `width * height`, and `perimeter()` returns
`2 * (width + height)`.

## Done when

- `Rectangle(3, 4).area()` is `12` and `.perimeter()` is `14`.
- Both work for any width and height.
- Both are methods on the class, computing from `self`.
""",

"9.4 hints": r"""Store both values in `__init__`: `self.width = width` and
`self.height = height`.

---

Add two methods. `area` returns `self.width * self.height`; `perimeter` returns
`2 * (self.width + self.height)`.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
""",

"9.4 reference": r"""A class can hold **several attributes** and offer **several methods** that work
together over them — modelling something with more than one property.

- `__init__` stores each piece of data (`self.width`, `self.height`); each method
  reads whatever attributes it needs.
- Methods can build on the same data for different answers: `area` multiplies,
  `perimeter` adds — one object, many questions.
- Keeping the data and the operations in one class means callers ask the object
  rather than juggling loose variables.

```python
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):      return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

r = Rectangle(3, 4); r.area(), r.perimeter()   # (12, 14)
```
""",

"9.5 brief": r"""# 9.5 -- Printing an object: `__str__`

## Concept

Print an object as-is and you get something useless like
`<__main__.Point object at 0x10f3d2b80>`. To control how an object looks as
text, define the special method `__str__`, which returns the string Python
should show.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
```

`__str__` is a **dunder** (double-underscore) method -- Python calls it for you
whenever the object is turned into text, by `print()` or `str()`:

```python
p = Point(3, 4)
print(p)        # (3, 4)
str(p)          # "(3, 4)"
```

You never call `__str__` yourself; you just define it, and `str(p)` triggers it.

## Your task

Define a class `Point` storing `x` and `y`, with a `__str__` method so that
`str(Point(3, 4))` is exactly `"(3, 4)"` -- the two values in parentheses,
comma-and-space between them.

## Done when

- `str(Point(3, 4))` is `"(3, 4)"`.
- It works for any `x` and `y`, including negatives.
- The formatting comes from a `__str__` method on the class.
""",

"9.5 hints": r"""Store `x` and `y` in `__init__` as usual, then add a `__str__(self)` method.

---

`__str__` must **return** the text (not print it). Build it with an f-string:
`return f"({self.x}, {self.y})"`. Mind the comma and the space.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
""",

"9.5 reference": r"""**`__str__`** defines the human-readable text for an object. When you `print` an
instance or call `str()` on it, Python calls `__str__` and uses what it returns.

- Without it, printing an object shows an unhelpful default like
  `<Point object at 0x...>`; `__str__` replaces that with something meaningful.
- It must **return** a string (not print one), typically built with an f-string
  from the object's attributes.
- `__str__` is one of several **dunder** ("double-underscore") methods Python
  calls on your behalf, like `__init__`.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f"({self.x}, {self.y})"

print(Point(3, 4))      # (3, 4)
```
""",

"9.6 brief": r"""# 9.6 -- A sensible default

## Concept

A constructor is just a function, so it can take **default parameters** (6.4),
too. That lets a caller leave out what they don't care about and still get a
working object.

```python
class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def greet(self, name):
        return f"{self.greeting}, {name}!"
```

If you don't pass a greeting, you get `"Hello"`; if you do, it's used instead:

```python
Greeter().greet("Ada")        # "Hello, Ada!"
Greeter("Hi").greet("Bo")     # "Hi, Bo!"
```

The default lives in `__init__`'s signature (`greeting="Hello"`), so the object
is configured once at construction and every `greet` reuses it.

## Your task

Define a class `Greeter` whose `__init__` takes a `greeting` that **defaults to
`"Hello"`** and stores it. Add a method `greet(name)` that returns
`"{greeting}, {name}!"`.

## Done when

- `Greeter().greet("Ada")` is `"Hello, Ada!"` (default used).
- `Greeter("Hi").greet("Bo")` is `"Hi, Bo!"` (default overridden).
- The default is a default *parameter* of `__init__`, not an `if` inside it.
""",

"9.6 hints": r"""Give `__init__` a parameter with a default: `def __init__(self,
greeting="Hello"):`, then store it on `self`.

---

`greet` builds the message: `return f"{self.greeting}, {name}!"`. The default
belongs in the signature, so don't write an `if greeting is None` instead.

---

class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def greet(self, name):
        return f"{self.greeting}, {name}!"
""",

"9.6 reference": r"""`__init__` is an ordinary function, so its parameters can have **default
values** — letting an object be created with or without certain arguments.

- `def __init__(self, balance=0):` allows `Account()` (starts at 0) or
  `Account(100)` (starts at 100).
- The same rules apply: defaulted parameters follow non-defaulted ones, and a
  mutable default needs the `None` sentinel trick
  (`def __init__(self, items=None): self.items = items or []`).
- Defaults make the common case effortless while keeping the option open.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance

Account().balance        # 0
Account(100).balance     # 100
```
""",

"9.7 brief": r"""# 9.7 -- Objects working together

## Concept

A method can take **another object** as an argument and build a **new** object
as its result. This is how objects combine without losing their own identity.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

`add` reaches into `other` (another Vector) for its data, and **returns a brand
new `Vector`** -- it does not change `self` or `other`:

```python
a = Vector(1, 2)
b = Vector(3, 4)
c = a.add(b)      # Vector(4, 6)
a.x               # still 1 -- a is untouched
```

Building a `Vector(...)` *inside* `Vector`'s own method is normal: the class can
use itself.

## Your task

Define a class `Vector` storing `x` and `y`, with a method `add(other)` that
returns a **new** `Vector` whose coordinates are the two vectors' coordinates
added together. The originals must be left unchanged.

## Done when

- `Vector(1, 2).add(Vector(3, 4))` is a Vector with `.x == 4` and `.y == 6`.
- The two input vectors are unchanged afterwards.
- `add` returns a new `Vector` object (not a tuple), built inside the method.
""",

"9.7 hints": r"""Store `x` and `y` in `__init__`. The method takes the other vector:
`def add(self, other):`.

---

Read both vectors through the dot (`self.x`, `other.x`) and **return a new
Vector**: `return Vector(self.x + other.x, self.y + other.y)`. Don't assign back
onto `self`.

---

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
""",

"9.7 reference": r"""Objects **collaborate**: a method can take **another object** of the same class
as a parameter, read its attributes, and **return a new** object holding the
result — leaving both inputs unchanged.

- `def add(self, other):` reaches `self.x` and `other.x`, then
  `return Vector(self.x + other.x, ...)`. Returning a fresh instance keeps the
  operands immutable.
- This is how value-like objects compose (points, vectors, money). Defining the
  dunder `__add__` would even let `a + b` call it.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

Vector(1, 2).add(Vector(3, 4)).x    # 4
```
""",

"9.8 brief": r"""# 9.8 -- Capstone: a bank account

## Concept

Time to put the chapter together: a class with state, several methods, a
sensible default, and a rule it enforces.

A `BankAccount` keeps a `balance`. You can deposit (it grows) and withdraw (it
shrinks) -- but a withdrawal that would overdraw the account must be **refused**,
leaving the balance untouched.

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
```

- `balance` defaults to `0`, so `BankAccount()` is an empty account.
- `deposit` and `withdraw` change the stored balance (state that persists).
- `withdraw` **returns `True`** when it succeeds and **`False`** when it refuses
  -- and on refusal the balance does not change.

```python
acc = BankAccount(100)
acc.deposit(50)       # balance 150
acc.withdraw(70)      # True,  balance 80
acc.withdraw(999)     # False, balance still 80
```

## Your task

Define `BankAccount` exactly as above: a `balance` that defaults to `0`, a
`deposit(amount)` method, and a `withdraw(amount)` method that subtracts and
returns `True` only when there's enough -- otherwise it changes nothing and
returns `False`.

## Done when

- `BankAccount()` starts at `0`; `BankAccount(100)` starts at `100`.
- `deposit` and `withdraw` update `balance`, and withdrawing too much returns
  `False` and leaves `balance` unchanged.
- Withdrawing exactly the balance is allowed.
""",

"9.8 hints": r"""`__init__(self, balance=0)` stores the starting balance. `deposit` just adds to
`self.balance`.

---

`withdraw` needs a guard: `if amount <= self.balance:` subtract and
`return True`; otherwise change nothing and `return False`.

---

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
""",

"9.8 reference": r"""The capstone is a **stateful class** that puts the chapter together: a default in
`__init__`, methods that **mutate** state, a **guard** that raises on invalid
operations, and `__str__` for display.

- `__init__` sets the starting balance (with a default); `deposit` and `withdraw`
  change `self.balance` in place.
- A guard protects the invariant: `withdraw` checks funds and
  `raise ValueError(...)` rather than allowing an impossible state.
- `__str__` renders the object for printing. Together these make an object that
  is reliable to use and pleasant to read.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
    def __str__(self):
        return f"balance: {self.balance}"
```
""",

"10.1 brief": r"""# 10.1 -- yield: a function that pauses

## Concept

A normal function `return`s **once** and is done. A **generator** is a
function that uses `yield` instead: each `yield` hands back **one** value and
**pauses** the function right there. Ask for the next value and it **resumes**
from where it stopped.

```python
def two_words():
    yield "hello"
    yield "world"
```

Calling it does **not** run the body. It hands you a **generator** -- an object
you pull values from, one at a time, usually with a `for` loop:

```python
for w in two_words():
    print(w)        # hello, then world
```

The payoff: a generator produces a sequence **without building the whole list
in memory**. You will feel that in 10.3.

## Example

```python
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1
```

`list(count_up(3))` is `[1, 2, 3]` -- each loop pass yields one number, then
pauses until the next is asked for.

## Your task

Define a generator `count_down(n)` that **yields** the whole numbers from `n`
down to `1`, in that order. If `n` is `0` (or less), it yields nothing.

## Done when

- `list(count_down(5))` is `[5, 4, 3, 2, 1]`.
- `list(count_down(1))` is `[1]`; `list(count_down(0))` is `[]`.
- You use `yield` -- so calling `count_down` returns a generator, not a list.
""",

"10.1 hints": r"""A generator looks like a normal function, but it says `yield` where a normal
one would build a result. Each `yield` produces one number.

---

Count with a loop from `n` downwards and `yield` each value. A `while` loop:
start `i` at `n`, `yield i`, then `i = i - 1`, while `i >= 1`. (A
`for i in range(n, 0, -1):` works too.)

---

def count_down(n):
    i = n
    while i >= 1:
        yield i
        i = i - 1
""",

"10.1 reference": r"""A function containing **`yield`** is a **generator function**. Calling it doesn't
run the body — it returns a **generator object** that produces values one at a
time, **pausing** at each `yield` and resuming where it left off when asked for
the next.

- Each `yield value` hands one value to whoever is iterating, then freezes the
  function's state until the next value is requested.
- You consume a generator by iterating it (`for x in gen:`) or with `next(gen)`.
- This differs from `return`, which hands back **one** value and ends the
  function for good.

```python
def two():
    yield 1
    yield 2

for n in two():
    print(n)            # 1, then 2
```
""",

"10.2 brief": r"""# 10.2 -- yield inside a loop

## Concept

The real power of `yield` shows when it sits **inside a loop**: one `yield` line
runs once per pass, streaming a whole transformed sequence -- a value at a time,
never the whole list at once.

```python
def letters(word):
    for ch in word:
        yield ch.upper()
```

`list(letters("hi"))` is `["H", "I"]`. The loop walks the input; the `yield`
emits one transformed item each time round, pausing in between.

## Example

```python
def doubles(nums):
    for x in nums:
        yield x * 2
```

`list(doubles([1, 5, 9]))` is `[2, 10, 18]`.

## Your task

Define a generator `squares(n)` that **yields** the squares of the whole
numbers from `0` up to (but not including) `n`: `0, 1, 4, 9, ...`. If `n` is `0`
(or less), it yields nothing.

## Done when

- `list(squares(4))` is `[0, 1, 4, 9]`.
- `list(squares(1))` is `[0]`; `list(squares(0))` is `[]`.
- You use `yield` inside a loop -- not a returned list or comprehension.
""",

"10.2 hints": r"""Walk the numbers `0, 1, ..., n-1` with a loop, and `yield` each one squared.

---

`for i in range(n):` then `yield i * i`. The loop gives you each number; the
yield emits its square and pauses until the next is asked for.

---

def squares(n):
    for i in range(n):
        yield i * i
""",

"10.2 reference": r"""Placing a **`yield` inside a loop** streams a whole sequence: the generator emits
one transformed value per pass, pausing after each and resuming on the next
request.

- `for x in source: yield f(x)` yields `f(x)` for every item — the generator form
  of building a list with a comprehension, but produced lazily.
- Nothing is computed until something iterates the generator, and only as far as
  it's consumed.

```python
def squares(nums):
    for n in nums:
        yield n * n

list(squares([1, 2, 3]))    # [1, 4, 9]
```
""",

"10.3 brief": r"""# 10.3 -- generators are lazy

## Concept

This is the superpower. A generator only does work **when you ask for the next
value**. It never builds the whole sequence up front -- so a generator can be
**endless** and still cost almost nothing until you pull from it.

```python
def naturals():
    i = 0
    while True:        # never stops on its own...
        yield i
        i = i + 1
```

`while True` in a normal function would hang forever. In a generator it is
fine: each `yield` **pauses** the loop until the caller wants one more. You
take only as many as you need:

```python
from itertools import islice
list(islice(naturals(), 4))     # [0, 1, 2, 3] -- then it just stops asking
```

`islice(gen, k)` pulls the first `k` items from a generator and no more. The
generator produces exactly those four, then sits paused.

## Example

`naturals()` above yields `0, 1, 2, 3, ...` with no end. Pulling 3 items gives
`[0, 1, 2]`; pulling 10 gives `[0, 1, ..., 9]`. The same endless generator,
asked for different amounts.

## Your task

Define an **endless** generator `naturals()` that yields the whole numbers
starting at `0`: `0, 1, 2, 3, ...` forever. It must never stop on its own; the
checker only ever pulls a handful of values from it.

## Done when

- The first 5 values of `naturals()` are `[0, 1, 2, 3, 4]`.
- It is endless -- pulling more values just gives more numbers; it never runs
  out.
- You use `yield`, so calling `naturals()` returns a generator.
""",

"10.3 hints": r"""You need a loop that never ends, yielding a counter that goes up by one each
time. The `yield` is what stops it from hanging.

---

Start `i` at `0`. Then `while True:` -- `yield i`, then `i = i + 1`. The loop
"never ends", but each yield pauses it until the next value is wanted.

---

def naturals():
    i = 0
    while True:
        yield i
        i = i + 1
""",

"10.3 reference": r"""Generators are **lazy**: each value is computed only when requested, so a
generator can describe an **endless** sequence and still be useful — you just
take the values you need.

- An infinite `while True: yield n; n += 1` never finishes on its own, but a
  consumer can stop early (a `break`, or `next` called a few times).
- Laziness means a generator holds essentially **no memory** for the sequence — it
  keeps only its current state, not every value — unlike a list that materialises
  all of them.

```python
def naturals():
    n = 0
    while True:
        yield n             # endless, but only as far as asked
        n += 1

g = naturals(); next(g), next(g)   # (0, 1)
```
""",

"10.4 brief": r"""# 10.4 -- a generator remembers

## Concept

Because a generator **pauses** instead of finishing, its local variables stay
alive between `yield`s. A value you build up survives every pause -- the
generator picks up exactly where it left off, accumulator and all.

```python
def tally(words):
    seen = 0
    for w in words:
        seen = seen + 1
        yield seen          # 1, then 2, then 3, ... -- `seen` is remembered
```

`list(tally(["a", "b", "c"]))` is `[1, 2, 3]`. The `seen` counter is not reset
on each pass; it keeps its value across the yields.

## Example

```python
def running_max(nums):
    best = None
    for n in nums:
        if best is None or n > best:
            best = n
        yield best
```

`list(running_max([3, 1, 5]))` is `[3, 3, 5]` -- each item is the largest seen
**so far**.

## Your task

Define a generator `running_total(nums)` that yields the **running sum** of
`nums`: each value is the total of every number up to and including the current
one. An empty list yields nothing.

## Done when

- `list(running_total([3, 1, 2]))` is `[3, 4, 6]`.
- `list(running_total([5]))` is `[5]`; `list(running_total([]))` is `[]`.
- You use `yield`, and a variable that carries the total across the yields.
""",

"10.4 hints": r"""Keep a `total` variable outside the loop, add each number to it inside the
loop, and `yield` the total after each addition.

---

`total = 0` before the loop. Then `for n in nums:` -- `total = total + n`,
then `yield total`. The total is remembered across the yields, so it keeps
growing.

---

def running_total(nums):
    total = 0
    for n in nums:
        total = total + n
        yield total
""",

"10.4 reference": r"""A generator **remembers** its local variables across `yield`s: execution freezes
at the `yield` and every local keeps its value until the next request resumes the
function. This lets a generator **carry state** as it streams.

- A variable updated in the loop (a running total, a previous value) persists
  between yields without any object or global.
- This is what makes a generator a natural **running accumulator** — a running
  sum, for instance, that emits the total so far each step.

```python
def running_sum(nums):
    total = 0
    for n in nums:
        total += n          # total survives across yields
        yield total

list(running_sum([1, 2, 3]))    # [1, 3, 6]
```
""",

"10.5 brief": r"""# 10.5 -- filter while you yield

## Concept

A generator does not have to yield on every pass. Put the `yield` behind an
`if`, and you **filter** the stream as it flows -- skipping the items you don't
want, emitting only the ones you do.

```python
def shouts(words):
    for w in words:
        if w.isupper():
            yield w          # only the all-caps words come out
```

`list(shouts(["hi", "STOP", "go", "NOW"]))` is `["STOP", "NOW"]`. The loop
visits every word; the `yield` runs only when the `if` is true.

## Example

```python
def positives(nums):
    for n in nums:
        if n > 0:
            yield n
```

`list(positives([-1, 4, 0, 2]))` is `[4, 2]`.

## Your task

Define a generator `evens(nums)` that yields only the **even** numbers of
`nums`, keeping their original order. (A number is even when `n % 2 == 0`.) If
none are even, it yields nothing.

## Done when

- `list(evens([1, 2, 3, 4]))` is `[2, 4]`.
- `list(evens([1, 3, 5]))` is `[]`; `list(evens([]))` is `[]`.
- You use `yield` behind an `if` -- not a returned list or comprehension.
""",

"10.5 hints": r"""Loop over every number, but only `yield` the ones that pass an evenness test.

---

`for n in nums:` then `if n % 2 == 0:` and, indented under the if, `yield n`.
The odd numbers simply fall through without yielding.

---

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n
""",

"10.5 reference": r"""Putting **`yield` behind an `if`** filters a stream as it flows: the generator
emits only the items that pass the test and silently skips the rest — the lazy
counterpart of a comprehension's `if` clause.

- `for x in source: if test(x): yield x` produces a filtered stream without
  building any intermediate list.
- Because it's lazy, it composes cleanly: a filter generator can feed another
  generator, each handling one stage.

```python
def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n         # only the evens make it out

list(evens(range(10)))      # [0, 2, 4, 6, 8]
```
""",

"10.6 brief": r"""# 10.6 -- yield from: pass a whole stream along

## Concept

When you want a generator to re-emit **every** item of another iterable, you
could loop and yield each one:

```python
def both(a, b):
    for x in a:
        yield x
    for y in b:
        yield y
```

Python has a shorthand for exactly that inner loop: **`yield from`**.

```python
def both(a, b):
    yield from a        # yield every item of a, one by one
    yield from b        # then every item of b
```

`yield from iterable` is "yield each value this iterable produces". The two
versions above behave identically; `yield from` just says it in one line.

## Example

```python
def repeat_each(items):
    for x in items:
        yield from (x, x)      # yield x, then x again

list(repeat_each([1, 2]))      # [1, 1, 2, 2]
```

## Your task

Define a generator `chain(a, b)` that yields **all** the items of `a`, then
**all** the items of `b`, in order. Use `yield from`. Either list may be empty.

## Done when

- `list(chain([1, 2], [3, 4]))` is `[1, 2, 3, 4]`.
- `list(chain([], [9]))` is `[9]`; `list(chain([], []))` is `[]`.
- You use `yield from`, so calling `chain` returns a generator.
""",

"10.6 hints": r"""You want to re-emit every item of `a`, then every item of `b`. `yield from`
does exactly that for one iterable at a time.

---

Two lines: `yield from a` then `yield from b`. Each one streams that whole list
into the generator's output.

---

def chain(a, b):
    yield from a
    yield from b
""",

"10.6 reference": r"""**`yield from iterable`** re-emits **every** item the iterable produces, as if you
had written a loop of `yield`s. It delegates a whole sub-stream in one line.

- `yield from sub` is equivalent to `for x in sub: yield x`, but shorter and
  faster — and it works with lists, ranges, other generators, any iterable.
- It's the tool for **flattening** or **chaining**: a generator can `yield from`
  several sources in turn to splice their streams together.

```python
def chain(a, b):
    yield from a
    yield from b            # splice two streams into one

list(chain([1, 2], [3, 4]))     # [1, 2, 3, 4]
```
""",

"10.7 brief": r"""# 10.7 -- stop early

## Concept

A generator ends the moment its function ends -- and a plain `return` (with no
value) inside a generator means "stop now, no more items". So a generator can
decide to **finish early**, before the input runs out.

```python
def before_blank(words):
    for w in words:
        if w == "":
            return          # stop the generator here
        yield w
```

`list(before_blank(["a", "b", "", "c"]))` is `["a", "b"]` -- once the blank is
reached, `return` ends the generator and `"c"` is never produced.

## Example

```python
def while_positive(nums):
    for n in nums:
        if n <= 0:
            return
        yield n

list(while_positive([3, 1, -1, 5]))    # [3, 1]
```

## Your task

Define a generator `until_zero(nums)` that yields each number **until it reaches
a `0`**, then stops. The `0` itself, and anything after it, is **not** yielded.
If there is no `0`, it yields the whole list.

## Done when

- `list(until_zero([1, 2, 0, 3]))` is `[1, 2]`.
- `list(until_zero([0, 9]))` is `[]`; `list(until_zero([1, 2, 3]))` is
  `[1, 2, 3]`.
- You use `yield`, and stop early when you hit a `0`.
""",

"10.7 hints": r"""Loop over the numbers. As soon as you see a `0`, stop the whole generator;
otherwise yield the number.

---

`for n in nums:` -- first `if n == 0: return` (this ends the generator), then
`yield n` for everything before the zero.

---

def until_zero(nums):
    for n in nums:
        if n == 0:
            return
        yield n
""",

"10.7 reference": r"""A bare **`return`** inside a generator — or simply reaching the end of the
function — **stops** it: iteration ends and no further values come. `return` in a
generator carries **no value**; it only signals "done".

- This lets a generator **stop early** on a condition: `if x == sentinel: return`
  ends the stream at that point.
- To a `for` loop, a stopped generator is just an iterable that has run out — the
  loop ends naturally (internally, the generator raises `StopIteration`).

```python
def until_zero(nums):
    for n in nums:
        if n == 0:
            return          # stop the stream here
        yield n

list(until_zero([3, 1, 0, 9]))  # [3, 1]
```
""",

"10.8 brief": r"""# 10.8 -- Capstone: a streaming pipeline

## Concept

Nothing new -- this capstone is the chapter in miniature. The real reason
generators matter is that they **compose**: one generator's output is another
generator's input, so data flows through a **pipeline**, one item at a time,
without ever building the full list in between.

A pipeline stage is just a generator that loops over `stream` (any iterable --
a list, or *another generator*) and yields as it goes:

```python
def only_long(stream):
    for word in stream:
        if len(word) >= 4:
            yield word
```

You will build a source, a filter, and a relabel stage, then wire them
together.

## Example

```python
numbers(4)                              # yields 0, 1, 2, 3
keep_even(numbers(4))                   # yields 0, 2
labelled(keep_even(numbers(4)))         # yields "#0", "#2"
```

## Your task

Define **three** generators:

- `numbers(n)` -- yields `0, 1, ..., n-1` (the source). `n <= 0` yields nothing.
- `keep_even(stream)` -- yields only the even numbers from `stream` (any
  iterable).
- `labelled(stream)` -- yields the string `"#x"` for each `x` in `stream`
  (e.g. `7` becomes `"#7"`).

Each must use `yield`. `keep_even` and `labelled` must work on **any** stream,
including the output of another generator, so they compose.

## Done when

- `list(numbers(4))` is `[0, 1, 2, 3]`; `list(numbers(0))` is `[]`.
- `list(keep_even([1, 2, 3, 4]))` is `[2, 4]`.
- `list(labelled([0, 2]))` is `["#0", "#2"]`.
- `list(labelled(keep_even(numbers(6))))` is `["#0", "#2", "#4"]`.
- All three use `yield`, and the filter/relabel stages accept any iterable.
""",

"10.8 hints": r"""Each stage is its own little generator. `numbers` loops over `range(n)` and
yields; `keep_even` loops over `stream` and yields only the evens; `labelled`
loops over `stream` and yields a formatted string. None of them build a list.

---

`keep_even` and `labelled` take a `stream` and `for x in stream:` -- that loop
works whether `stream` is a list or another generator, which is what lets you
nest them. Use an f-string for the label: `yield f"#{x}"`.

---

def numbers(n):
    for i in range(n):
        yield i


def keep_even(stream):
    for x in stream:
        if x % 2 == 0:
            yield x


def labelled(stream):
    for x in stream:
        yield f"#{x}"
""",

"10.8 reference": r"""The capstone composes generators into a **streaming pipeline**: a **source**
generator feeds a **filter** generator, which feeds a **transform** generator.
Each stage is lazy, so values flow through one at a time and nothing is
materialised in full.

- Because each stage consumes the previous lazily, the pipeline processes huge or
  endless data with tiny memory — one item is in flight at a time.
- Stages stay small and independent: swap or add a stage without touching the
  others. This is the generator analogue of composing functions.

```python
def reader(nums):  yield from nums
def keep_pos(src): yield from (n for n in src if n > 0)
def doubled(src):  yield from (n * 2 for n in src)

list(doubled(keep_pos(reader([-1, 2, -3, 4]))))   # [4, 8]
```
""",

"11.1 brief": r"""# 11.1 -- import: bring in a module

## Concept

Python ships a large **standard library**: ready-made tools grouped into
**modules**. You don't get them for free in every file -- you **import** the
module you need, then reach its contents through its name.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
```

- `import math` runs once at the top of the file and binds the name `math` to
  the whole module.
- After that, `math.sqrt` is the square-root function and `math.pi` the
  constant -- `module.name` reaches anything the module provides.

The point of importing is that someone has already written and tested these, so
you call `math.sqrt` instead of re-deriving a square root yourself.

## Example

```python
import math

def diagonal(side):
    return math.sqrt(2) * side
```

## Your task

Define `hypotenuse(a, b)` that returns the length of the hypotenuse of a
right triangle with legs `a` and `b` -- the square root of `a*a + b*b` --
using **`math.sqrt`** from the imported `math` module.

## Done when

- `hypotenuse(3, 4)` returns `5.0`, `hypotenuse(5, 12)` returns `13.0`.
- `hypotenuse(0, 0)` returns `0.0`.
- The square root comes from `math.sqrt`, via `import math`.
""",

"11.1 hints": r"""The very first line of the file makes the module available: `import math`. After
that you can use anything it provides as `math.something`.

---

`math.sqrt(x)` returns the square root of `x`. You want the square root of
`a*a + b*b`. Put the `import math` at the top, then write the function.

---

import math


def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)
""",

"11.1 reference": r"""An **`import`** statement loads a **module** — a file of ready-made code from the
standard library — and binds it to a name. `import math` makes the module object
available as `math`, and its contents are reached through it: `math.sqrt`,
`math.pi`, `math.floor`.

- The statement runs **once**, conventionally at the **top** of the file; the
  name then refers to the whole module for the rest of the program.
- **`module.name`** (attribute access) looks a function or constant up *on* the
  module, which keeps each module's names in their own namespace — `math.pi` and
  your own `pi` never collide.
- Importing a name that doesn't exist raises `ModuleNotFoundError`; the module's
  code runs the first time it is imported and is cached thereafter.
- The standard library ships with Python ("batteries included"), so these
  modules need no installation — just the import.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
math.floor(2.7)  # 2
```
""",

"11.2 brief": r"""# 11.2 -- from import: pull out one name

## Concept

`import math` brings in the *whole* module and you reach into it with
`math.something`. Often you want just one tool, used by its plain name. The
**`from ... import ...`** form does that:

```python
from math import gcd

gcd(12, 18)      # 6  -- called directly, no math. prefix
```

- `from math import gcd` binds the single name `gcd` into your file.
- You then call it as `gcd(...)`, not `math.gcd(...)`.
- You can pull several at once: `from math import gcd, sqrt, pi`.

`gcd(a, b)` is the **greatest common divisor** -- the largest integer that
divides both. It's exactly what you need to reduce a fraction to lowest terms:
divide the top and bottom by their gcd.

## Example

```python
from math import gcd

def both_divisible_by(a, b):
    return gcd(a, b)
```

## Your task

Using **`from math import gcd`**, define `simplify(num, den)` that returns the
fraction `num/den` reduced to lowest terms, as a tuple `(top, bottom)`: divide
both `num` and `den` by their `gcd`.

## Done when

- `simplify(6, 8)` returns `(3, 4)`, `simplify(10, 5)` returns `(2, 1)`.
- `simplify(7, 7)` returns `(1, 1)`.
- The gcd comes from `math`, imported with `from math import gcd`.
""",

"11.2 hints": r"""Start the file with `from math import gcd`. Now `gcd` is a function you can call
directly, no `math.` in front of it.

---

Find `g = gcd(num, den)`, then return the tuple `(num // g, den // g)`. Use `//`
(integer division) so the result stays whole numbers.

---

from math import gcd


def simplify(num, den):
    g = gcd(num, den)
    return (num // g, den // g)
""",

"11.2 reference": r"""The **`from module import name`** form binds a specific name from a module
*directly* into your file, so it's called without the module prefix. `from math
import gcd` makes `gcd` a plain name; you write `gcd(12, 18)`, not
`math.gcd(...)`.

- Several names at once: `from math import gcd, sqrt, pi`.
- It imports only what you name — `math.floor` is **not** available unless you
  also import `floor`. (`import math` brings everything but keeps the prefix; the
  two forms trade convenience against namespace clarity.)
- The whole module still runs and is cached; you've just chosen which of its
  names land in your namespace. Because the name arrives bare, it can **shadow**
  one of your own — `from math import e` would hide a variable called `e`.

```python
from math import gcd, sqrt

gcd(12, 18)    # 6
sqrt(16)       # 4.0
```
""",

"11.3 brief": r"""# 11.3 -- import as: rename on the way in

## Concept

Sometimes a module's name is long, or clashes with one of yours. **`import ... as
...`** brings the module in under a name **you** choose:

```python
import statistics as stats

stats.mean([1, 2, 3, 4])    # 2.5
```

- `import statistics as stats` binds the module to `stats`; `stats.mean` is
  exactly `statistics.mean`.
- The alias is just a local nickname -- the module is unchanged, and only your
  file sees the new name.
- This is why you'll see conventional aliases everywhere (`import numpy as np`);
  here we shorten `statistics`.

The **`statistics`** module does the common averages for you. `stats.mean(nums)`
is the arithmetic mean -- the sum divided by the count -- without you writing
`sum(nums) / len(nums)`.

## Example

```python
import statistics as stats

def midpoint(nums):
    return stats.median(nums)
```

## Your task

Using **`import statistics as stats`**, define `average(nums)` that returns the
mean of the list `nums`, computed with `stats.mean`.

## Done when

- `average([2, 4, 6])` returns `4`, `average([1, 2])` returns `1.5`.
- `average([5])` returns `5`.
- The mean comes from `statistics.mean`, imported as `stats`.
""",

"11.3 hints": r"""Begin with `import statistics as stats`. From then on, `stats` is your name for
the module.

---

`stats.mean(nums)` returns the average of the list. Your whole function can be
one line that returns it.

---

import statistics as stats


def average(nums):
    return stats.mean(nums)
""",

"11.3 reference": r"""**`import module as alias`** imports a module but binds it under a name of your
choosing. `import statistics as stats` makes the module available as `stats`;
`stats.mean` *is* `statistics.mean` — the alias changes only the local name, not
the module.

- Use it to **shorten** a long module name or to **avoid a clash** with one of
  your own names. The convention-driven aliases you'll meet (`import numpy as
  np`) are exactly this.
- The same `as` works on a single name from a from-import: `from statistics
  import mean as avg`.
- Only your file sees the alias; other modules keep their own names for it.

```python
import statistics as stats

stats.mean([1, 2, 3, 4])     # 2.5
stats.median([1, 5, 2])      # 2
```
""",

"11.4 brief": r"""# 11.4 -- random: reproducible chance

## Concept

The **`random`** module produces pseudo-random values: `random.randint(1, 6)`
rolls a die, `random.shuffle(lst)` reorders a list in place. They're *pseudo*-
random -- computed from an internal state -- which means you can make them
**repeatable** by fixing that state with a **seed**:

```python
import random

random.seed(42)
random.shuffle(deck)     # always the same order for seed 42
```

- `random.seed(n)` sets the starting point. After the same seed, the same calls
  produce the same results, every run, every machine.
- `random.shuffle(lst)` shuffles **in place** (it returns `None`), so shuffle a
  copy if you need to keep the original.

Seeding is how a game replays a level, or a test checks "random" code.

## Example

```python
import random

def pick(options, seed):
    random.seed(seed)
    return random.choice(options)
```

## Your task

Define `shuffled(items, seed)` that returns a **new** list with the items of
`items` shuffled, made repeatable by seeding with `seed` **before** shuffling.
Don't change the original `items`.

## Done when

- `shuffled(items, seed)` gives the same result every time for the same
  `items` and `seed`.
- The original list passed in is left unchanged (shuffle a copy).
- `shuffled([], 1)` returns `[]`.
""",

"11.4 hints": r"""You need three steps: copy the list, seed the generator, shuffle the copy.
`out = list(items)` makes the copy so the original is safe.

---

`random.seed(seed)` fixes the starting point; `random.shuffle(out)` reorders
`out` in place (it returns None, so don't `return random.shuffle(...)`). Return
`out` afterwards.

---

import random


def shuffled(items, seed):
    out = list(items)
    random.seed(seed)
    random.shuffle(out)
    return out
""",

"11.4 reference": r"""The **`random`** module generates pseudo-random values from an internal state:
`random.randint(a, b)` (an integer in `[a, b]`), `random.choice(seq)` (a random
item), `random.shuffle(lst)` (reorder a list **in place**), `random.random()` (a
float in `[0, 1)`).

- The numbers are deterministic functions of the state, so **`random.seed(n)`**
  makes them **repeatable**: after the same seed, the same calls yield the same
  results on every run and machine. Seed once, before the draws you want to
  reproduce.
- `random.shuffle` mutates its argument and returns `None` — shuffle a **copy**
  (`out = list(items)`) to keep the original, and never `return
  random.shuffle(...)`.
- The default (unseeded) generator is seeded from the OS, so without a seed each
  run differs. `random` is **not** for cryptography — use the `secrets` module
  for tokens and passwords.

```python
import random

random.seed(42)
random.randint(1, 6)     # same value every run for seed 42
deck = [1, 2, 3, 4]
random.shuffle(deck)     # deck reordered in place
```
""",

"11.5 brief": r"""# 11.5 -- Counter: tally in one step

## Concept

Back in chapter 5 you tallied by hand: `counts[k] = counts.get(k, 0) + 1`. The
**`collections`** module ships that pattern, written and tested, as **`Counter`**:

```python
from collections import Counter

Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
```

- `Counter(items)` walks any iterable and returns a count of each distinct item.
- A `Counter` **is** a dict (it's a subclass), so `counts[x]` and
  `for k, v in counts.items()` work exactly as you'd expect -- and it compares
  equal to the plain dict with the same counts.
- It even handles the missing key: `counts["zzz"]` is `0`, not a `KeyError`.

This is the standard library's promise: the loop you'd write is already a tool.

## Example

```python
from collections import Counter

def letter_counts(word):
    return Counter(word)
```

## Your task

Using **`Counter`** from `collections`, define `tally(items)` that returns a
count of how many times each item appears in the list `items`.

## Done when

- `tally(["a", "b", "a"])` equals `{"a": 2, "b": 1}`.
- `tally([])` equals `{}`.
- The counting is done by `Counter`, not a hand-written loop.
""",

"11.5 hints": r"""`from collections import Counter` at the top. `Counter` does the whole tally when
you hand it the list.

---

`Counter(items)` already returns the counts, and a Counter compares equal to the
plain dict of the same counts -- so you can return it directly.

---

from collections import Counter


def tally(items):
    return Counter(items)
""",

"11.5 reference": r"""**`Counter`** (from the **`collections`** module) is a `dict` subclass that
tallies an iterable in one call: `Counter(items)` returns a mapping of each
distinct item to how many times it appears — the `counts.get(k, 0) + 1` loop,
already written.

- Being a dict, it supports everything a dict does (`c[key]`, `c.items()`,
  `key in c`) and compares **equal** to a plain dict with the same counts.
- A **missing** key reads as `0` rather than raising `KeyError`, which suits
  counting.
- **`c.most_common(n)`** returns the `n` highest-count `(item, count)` pairs,
  already sorted — the report step for free. Counters also add and subtract
  (`c1 + c2`) to combine tallies.

```python
from collections import Counter

c = Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
c["a"]                    # 3
c["z"]                    # 0  -- no KeyError
c.most_common(1)          # [('a', 3)]
```
""",

"11.6 brief": r"""# 11.6 -- defaultdict: a default for missing keys

## Concept

To group items in a plain dict you must first check whether the key exists:

```python
if length not in groups:
    groups[length] = []
groups[length].append(word)
```

**`defaultdict`** removes that ceremony. You give it a **factory** -- a function
that makes the default value -- and it calls the factory automatically the first
time you touch a missing key:

```python
from collections import defaultdict

groups = defaultdict(list)     # missing key -> a fresh []
groups[5].append("hello")      # no setup needed
```

- `defaultdict(list)` makes an empty list for any new key, so `.append` just
  works.
- `defaultdict(int)` makes `0` for any new key -- a tally without `.get`.
- It's a real dict otherwise; convert with `dict(groups)` if you want a plain one.

## Example

```python
from collections import defaultdict

def by_first_letter(words):
    groups = defaultdict(list)
    for w in words:
        groups[w[0]].append(w)
    return dict(groups)
```

## Your task

Using **`defaultdict`** from `collections`, define `group_by_length(words)` that
returns a dict mapping each word **length** to the list of words of that length,
in their original order.

## Done when

- `group_by_length(["hi", "ok", "bye"])` equals `{2: ["hi", "ok"], 3: ["bye"]}`.
- `group_by_length([])` equals `{}`.
- Grouping uses a `defaultdict(list)`, not a manual "if key in dict" check.
""",

"11.6 hints": r"""`from collections import defaultdict`, then `groups = defaultdict(list)`. The
`list` is the factory: every new key starts as an empty list.

---

Loop the words; for each, `groups[len(w)].append(w)`. The key is the length,
the value is the growing list. Return `dict(groups)` at the end.

---

from collections import defaultdict


def group_by_length(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)
""",

"11.6 reference": r"""**`defaultdict`** (from **`collections`**) is a `dict` that supplies a default for
a missing key automatically. You pass it a **factory** — a zero-argument callable
that builds the default — and the first time you read or touch an absent key, it
calls the factory, stores the result, and uses it.

- `defaultdict(list)` makes a fresh `[]` for each new key, so `d[k].append(x)`
  works with no "if key not in d" setup — the grouping idiom.
- `defaultdict(int)` makes `0` for each new key, so `d[k] += 1` tallies.
- Only **lookup** of a missing key triggers the factory; it's otherwise an
  ordinary dict. `dict(d)` converts to a plain dict, and a *genuinely* missing
  key still reads as the default rather than raising.

```python
from collections import defaultdict

groups = defaultdict(list)
groups[5].append("hello")    # key 5 auto-starts as []
groups                       # defaultdict(<class 'list'>, {5: ['hello']})
```
""",

"11.7 brief": r"""# 11.7 -- json: data as text

## Concept

To save data to a file or send it over a network, you need it as **text**.
**JSON** is the near-universal text format for structured data, and the **`json`**
module converts both ways:

```python
import json

json.dumps({"name": "Ada", "score": 90})   # '{"name": "Ada", "score": 90}'
json.loads('{"ok": true}')                  # {'ok': True}
```

- `json.dumps(obj)` -- "dump string" -- turns a Python dict/list/number/str into
  a JSON **string**.
- `json.loads(text)` -- "load string" -- parses a JSON string back into Python
  values.
- The two are inverses: `json.loads(json.dumps(x))` gives `x` back.

Note JSON's spelling differs slightly from Python's (`true`/`false`/`null`), which
is exactly why you let the module handle it instead of formatting by hand.

## Example

```python
import json

def parse(text):
    return json.loads(text)
```

## Your task

Using **`json.dumps`**, define `to_json(record)` that returns the JSON string
for the dictionary `record`.

## Done when

- `to_json({"a": 1, "b": 2})` returns `'{"a": 1, "b": 2}'`.
- `to_json({})` returns `'{}'`.
- The string is produced by `json.dumps`, not built by hand.
""",

"11.7 hints": r"""`import json` at the top. The function you want is `json.dumps`, which takes a
Python object and returns its JSON text.

---

`json.dumps(record)` does the whole job. The function body is one line that
returns it.

---

import json


def to_json(record):
    return json.dumps(record)
""",

"11.7 reference": r"""**JSON** (JavaScript Object Notation) is the standard **text** format for
structured data, and the **`json`** module converts Python values to and from it.

- **`json.dumps(obj)`** ("dump string") serializes a Python `dict`, `list`,
  `str`, number, `bool`, or `None` into a JSON string. Keys become strings, and
  Python's `True`/`False`/`None` are written as JSON's `true`/`false`/`null`.
- **`json.loads(text)`** ("load string") parses a JSON string back into Python
  values. The two are inverses: `json.loads(json.dumps(x)) == x`.
- `dumps` takes options — `indent=2` pretty-prints, `sort_keys=True` orders the
  keys. The file-oriented `json.dump(obj, f)` / `json.load(f)` write and read a
  file object directly.
- Only JSON-compatible types serialize; a `set` or a custom object raises
  `TypeError` unless you tell `dumps` how to convert it.

```python
import json

json.dumps({"name": "Ada", "ok": True})   # '{"name": "Ada", "ok": true}'
json.loads('[1, 2, 3]')                    # [1, 2, 3]
```
""",

"11.8 brief": r"""# 11.8 -- Capstone: a stats summary from JSON

## Concept

This chapter's real lesson is that everyday work is **composing library tools**:
let one module read the data, another crunch it, and return the result. Here you
combine two of the modules you just met.

The input is a **JSON string** holding a list of numbers, e.g. `"[4, 8, 15, 16]"`.
You'll:

1. parse it with **`json.loads`** into a Python list,
2. summarize it with **`statistics`** and the built-ins `max` / `min`,
3. return a plain dict of the results.

```python
import json
import statistics

data = json.loads("[4, 8, 15, 16]")     # [4, 8, 15, 16]
statistics.mean(data)                    # 10.75
```

## Your task

Define `summary(numbers_json)` that takes a JSON string of a list of numbers and
returns a dict with these keys:

- `"count"` -- how many numbers (`len`),
- `"mean"` -- their mean (`statistics.mean`),
- `"max"` -- the largest (`max`),
- `"min"` -- the smallest (`min`).

Parse the input with `json.loads`. Assume at least one number.

## Done when

- `summary("[2, 4, 6]")` equals
  `{"count": 3, "mean": 4, "max": 6, "min": 2}`.
- `summary("[5]")` equals `{"count": 1, "mean": 5, "max": 5, "min": 5}`.
- The input is parsed with `json.loads`, not by hand.
""",

"11.8 hints": r"""Two imports at the top: `import json` and `import statistics`. First turn the
text into a list with `json.loads(numbers_json)`.

---

Once you have the list `nums`, build the dict: `len(nums)` for count,
`statistics.mean(nums)` for mean, and the built-in `max(nums)` / `min(nums)`.

---

import json
import statistics


def summary(numbers_json):
    nums = json.loads(numbers_json)
    return {
        "count": len(nums),
        "mean": statistics.mean(nums),
        "max": max(nums),
        "min": min(nums),
    }
""",

"11.8 reference": r"""The capstone is the chapter's real point: **composing standard-library modules**
into a small pipeline rather than writing each step from scratch.

- **Read** with `json` — `json.loads(text)` turns the JSON input into Python
  values (here, a list of numbers).
- **Summarize** with `statistics` and the built-ins — `statistics.mean(nums)` for
  the average, `max(nums)` / `min(nums)` for the extremes, `len(nums)` for the
  count.
- **Return** a plain `dict`, so the caller gets ordinary Python values to use.

Each stage is a module someone else wrote and tested; your job is to wire them
together. That is what most real programs are — glue between well-made libraries.

```python
import json
import statistics

def summary(numbers_json):
    nums = json.loads(numbers_json)
    return {"count": len(nums), "mean": statistics.mean(nums),
            "max": max(nums), "min": min(nums)}

summary("[2, 4, 6]")   # {'count': 3, 'mean': 4, 'max': 6, 'min': 2}
```
""",

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

"14.1 brief": r"""# 14.1 -- lambda: a function in an expression

## Concept

A **`lambda`** is a tiny function written inline, with no name and no `def`:

```python
double = lambda x: x * 2
double(5)      # 10
```

- `lambda args: expression` -- the value of the expression is returned
  automatically (no `return`, and only one expression allowed).
- A lambda is a **value**, so you can store it, **return** it from another
  function, or pass it as an argument (which is where it really earns its keep --
  the rest of this chapter).

Because a lambda is defined inside another function, it can **close over** that
function's variables. `lambda x: x * n` remembers the `n` from where it was made.

(For anything longer than one expression, use a normal `def` -- lambdas are for
small inline functions.)

## Example

```python
def adder(n):
    return lambda x: x + n     # remembers n
```

## Your task

Define `multiplier(n)` that **returns a lambda** which multiplies its argument by
`n`. So `multiplier(3)` returns a function, and calling that function with `4`
gives `12`.

## Done when

- `multiplier(3)(4)` is `12`; `multiplier(10)(5)` is `50`.
- `multiplier(0)(7)` is `0`.
- The returned function is a `lambda`, not a nested `def`.
""",

"14.1 hints": r"""A lambda is `lambda args: expression`. You want one that takes an `x` and gives
back `x * n`.

---

`multiplier` returns that lambda. The lambda closes over `n`, so each call to
`multiplier` makes a function tied to its own `n`.

---

def multiplier(n):
    return lambda x: x * n
""",

"14.1 reference": r"""A **`lambda`** is an anonymous function written as a single expression:
`lambda args: expression`. The expression's value is returned automatically —
there is no `return`, and the body must be **one** expression.

- A lambda is a first-class **value**: assign it, return it, or pass it as an
  argument. `f = lambda x: x * 2` is much like `def f(x): return x * 2`, just
  inline and nameless.
- Defined inside another function, a lambda **closes over** that scope's
  variables — `lambda x: x * n` captures `n` from where it was created, so each
  `multiplier(n)` yields a function bound to its own `n`.
- Lambdas are for *small* inline functions, especially as the `key=` to `sorted`
  or the function for `map`/`filter` (the rest of this chapter). For anything
  multi-statement, use a named `def`.

```python
double = lambda x: x * 2
double(5)                  # 10

def multiplier(n):
    return lambda x: x * n
multiplier(3)(4)           # 12
```
""",

"14.2 brief": r"""# 14.2 -- map: apply to every item

## Concept

**`map(func, iterable)`** runs `func` on **every** item and yields the results.
It's the "apply to each" pattern as a higher-order function -- a function that
takes another function:

```python
list(map(str.upper, ["a", "b"]))     # ['A', 'B']
list(map(lambda x: x * x, [1, 2, 3])) # [1, 4, 9]
```

- `map` returns a **lazy iterator**, so wrap it in `list(...)` to get a list.
- The function can be a `lambda`, a `def`, or a built-in like `str.upper` or
  `int`.

(A list comprehension `[f(x) for x in items]` does the same thing and often reads
more naturally; this puzzle is about learning `map` itself, the tool you'll meet
in plenty of code.)

## Example

```python
def lengths(words):
    return list(map(len, words))
```

## Your task

Using **`map`**, define `squares(nums)` that returns a list of each number in
`nums` squared.

## Done when

- `squares([1, 2, 3])` returns `[1, 4, 9]`.
- `squares([])` returns `[]`.
- The mapping is done with `map`, not a comprehension or manual loop.
""",

"14.2 hints": r"""`map(func, nums)` applies `func` to each number. Your `func` squares its input:
`lambda x: x * x`.

---

`map` is lazy, so wrap it: `list(map(lambda x: x * x, nums))`.

---

def squares(nums):
    return list(map(lambda x: x * x, nums))
""",

"14.2 reference": r"""**`map(func, iterable)`** applies `func` to every item and yields the results —
the "transform each item" pattern as a higher-order function (one that takes
another function as an argument).

- It returns a **lazy iterator**, computing each result on demand; wrap it in
  `list(...)` (or `tuple`, or feed a `for`) to consume it.
- `func` can be a `lambda`, a named `def`, or any callable — a built-in like
  `len`, `str.upper`, or `int` is common.
- Given several iterables, `map(func, a, b)` calls `func(a_i, b_i)` in lockstep,
  stopping at the shortest.
- A list comprehension `[func(x) for x in items]` expresses the same thing and is
  often clearer; `map` is the functional-style equivalent you'll see widely.

```python
list(map(len, ["hi", "there"]))        # [2, 5]
list(map(lambda x: x * x, [1, 2, 3]))  # [1, 4, 9]
list(map(int, ["1", "2", "3"]))        # [1, 2, 3]
```
""",

"14.3 brief": r"""# 14.3 -- filter: keep what passes

## Concept

Where `map` transforms every item, **`filter`** keeps only **some** of them.
You give it a **predicate** -- a function that returns true or false -- and it
keeps each item the predicate says yes to:

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))     # [2, 4]
```

- `filter(pred, iterable)` yields each item for which `pred(item)` is truthy,
  dropping the rest, in order.
- Like `map`, it returns a **lazy iterator**, so wrap it in `list(...)`.

(The comprehension `[x for x in items if pred(x)]` does the same; this puzzle is
about `filter` itself.)

## Example

```python
def nonempty(strings):
    return list(filter(lambda s: s != "", strings))
```

## Your task

Using **`filter`**, define `evens(nums)` that returns a list of only the even
numbers in `nums`.

## Done when

- `evens([1, 2, 3, 4])` returns `[2, 4]`.
- `evens([1, 3, 5])` returns `[]`.
- The selection is done with `filter`, not a comprehension or manual loop.
""",

"14.3 hints": r"""`filter(pred, nums)` keeps each number where `pred` is true. Your predicate tests
even: `lambda x: x % 2 == 0`.

---

Wrap it in `list(...)`: `list(filter(lambda x: x % 2 == 0, nums))`.

---

def evens(nums):
    return list(filter(lambda x: x % 2 == 0, nums))
""",

"14.3 reference": r"""**`filter(pred, iterable)`** keeps the items for which the **predicate** `pred`
(a function returning true or false) is truthy, dropping the rest — the "keep if"
counterpart to `map`'s "transform each".

- It returns a **lazy iterator** in original order; wrap it in `list(...)` to
  collect.
- `pred` is any callable returning a truthy/falsy value — a `lambda`, a `def`, or
  a built-in. Passing **`None`** as the predicate (`filter(None, items)`) keeps
  the items that are themselves truthy, dropping `0`, `""`, `None`, etc.
- The comprehension `[x for x in items if pred(x)]` is the equivalent and often
  reads better; `filter` is the functional form.

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))   # [2, 4]
list(filter(None, [0, 1, "", "a", None]))        # [1, 'a']
list(filter(str.isalpha, "a1b2"))                # ['a', 'b']
```
""",

"14.4 brief": r"""# 14.4 -- sorted(key=lambda): sort by a derived value

## Concept

`sorted` (chapter 5) orders items by their natural order. Its **`key=`** argument
changes *what* it sorts on: a function mapping each item to the value to compare.
An inline **lambda** is the usual way to write that:

```python
words = ["pear", "fig", "apple"]
sorted(words, key=len)                  # ['fig', 'pear', 'apple']
sorted(words, key=lambda w: w[-1])      # by last letter
```

- `key` is called once per item; `sorted` then orders items by those key values.
- The lambda lets you sort by anything **derived** from an item -- its length, a
  field, a computed score -- without changing the items themselves.
- `sorted` is **stable**: items with equal keys keep their original order.

## Example

```python
def by_size(nums):
    return sorted(nums, key=lambda n: abs(n))   # by distance from zero
```

## Your task

Using **`sorted`** with a **`key=lambda`**, define `by_last(words)` that returns
the words sorted by their **last character**.

## Done when

- `by_last(["pear", "fig", "kiwi"])` returns `["fig", "kiwi", "pear"]`
  (last letters g, i, r are in order).
- `by_last([])` returns `[]`.
- The order comes from `sorted(..., key=lambda ...)`, not a manual sort.
""",

"14.4 hints": r"""`sorted(words, key=...)` sorts by whatever the key function returns. You want to
sort by the last character of each word.

---

The last character of `w` is `w[-1]`, so the key is `lambda w: w[-1]`:
`sorted(words, key=lambda w: w[-1])`.

---

def by_last(words):
    return sorted(words, key=lambda w: w[-1])
""",

"14.4 reference": r"""`sorted`'s **`key=`** argument is a function mapping each item to the value to
sort on, so you can order by something **derived** from the items rather than the
items themselves. An inline **`lambda`** is the idiomatic way to write that key.

- `key` is called **once per item**; `sorted` orders the items by the resulting
  key values, but returns the original items. `sorted(words, key=len)` orders by
  length, `sorted(words, key=lambda w: w[-1])` by last letter.
- `sorted` is **stable**: items with equal keys keep their input order.
- Pair `key=` with **`reverse=True`** to sort descending. The same `key=` works on
  `list.sort`, `min`, and `max`.

```python
sorted(["pear", "fig", "apple"], key=len)            # ['fig', 'pear', 'apple']
sorted([-3, 1, -2], key=lambda n: abs(n))            # [1, -2, -3]
sorted(records, key=lambda r: r[1], reverse=True)    # by 2nd field, high first
```
""",

"14.5 brief": r"""# 14.5 -- any: is at least one true?

## Concept

**`any(iterable)`** returns `True` if **at least one** item is truthy, `False`
otherwise. Fed a generator of tests, it answers "does *any* item pass?":

```python
any(n < 0 for n in [1, 2, -3])     # True
any(n < 0 for n in [1, 2, 3])      # False
```

- It replaces the loop-with-a-flag (`found = False; for ...: if ...: found =
  True`) with one expression.
- It **short-circuits**: it stops and returns `True` at the first truthy item.
- `any([])` is `False` (nothing passed).

The pattern is `any(<test> for <item> in <iterable>)` -- a generator expression
of booleans handed to `any`.

## Example

```python
def has_blank(strings):
    return any(s == "" for s in strings)
```

## Your task

Using **`any`**, define `has_negative(nums)` that returns `True` if `nums`
contains at least one negative number.

## Done when

- `has_negative([1, 2, -3])` is `True`; `has_negative([1, 2, 3])` is `False`.
- `has_negative([])` is `False`.
- The answer comes from `any(...)`, not a hand-written loop with a flag.
""",

"14.5 hints": r"""`any(...)` takes a sequence of true/false values and returns True if any is true.
Build that sequence with a generator expression.

---

`any(n < 0 for n in nums)` -- for each number, the test `n < 0` is True or False,
and `any` reports whether at least one was True.

---

def has_negative(nums):
    return any(n < 0 for n in nums)
""",

"14.5 reference": r"""**`any(iterable)`** returns `True` as soon as **one** item is truthy, else
`False`. Handed a generator of tests, it answers "does any item pass?" in a single
expression, replacing a loop that sets a flag.

- It **short-circuits**: evaluation stops at the first truthy item, so it's
  efficient and works on infinite/lazy iterables.
- `any([])` is `False` — there is nothing to be true.
- The idiom is `any(<test> for <item> in <iterable>)`: a generator expression of
  booleans. (Its partner `all` is 14.6.)

```python
any(n < 0 for n in [1, 2, -3])    # True
any(c.isdigit() for c in "abc")   # False
any([])                           # False
```
""",

"14.6 brief": r"""# 14.6 -- all: are they every one true?

## Concept

**`all(iterable)`** is `any`'s partner: it returns `True` only if **every** item
is truthy. It answers "do they *all* pass?":

```python
all(n > 0 for n in [1, 2, 3])      # True
all(n > 0 for n in [1, -2, 3])     # False
```

- It **short-circuits** the other way: it stops and returns `False` at the first
  item that fails.
- `all([])` is `True` -- vacuously, since no item failed. (A common surprise:
  "all of nothing" is true.)

Same shape as `any`: `all(<test> for <item> in <iterable>)`.

## Example

```python
def all_words(strings):
    return all(s.isalpha() for s in strings)
```

## Your task

Using **`all`**, define `all_positive(nums)` that returns `True` if **every**
number in `nums` is greater than zero.

## Done when

- `all_positive([1, 2, 3])` is `True`; `all_positive([1, -2, 3])` is `False`.
- `all_positive([])` is `True` (nothing fails).
- The answer comes from `all(...)`, not a hand-written loop with a flag.
""",

"14.6 hints": r"""`all(...)` returns True only if every value in the sequence is true. Build the
sequence of tests with a generator expression.

---

`all(n > 0 for n in nums)` -- each `n > 0` is True or False, and `all` is True
only if none were False.

---

def all_positive(nums):
    return all(n > 0 for n in nums)
""",

"14.6 reference": r"""**`all(iterable)`** returns `True` only if **every** item is truthy — the partner
to `any`. It answers "do they all pass?" in one expression.

- It **short-circuits** on the first falsy item, returning `False` immediately.
- `all([])` is `True` — *vacuously*, since no item failed. This "all of nothing
  is true" rule is a common surprise; guard for the empty case if it matters.
- Same shape as `any`: `all(<test> for <item> in <iterable>)`. Together they
  express the universal ("for all") and existential ("there exists") questions
  over a sequence.

```python
all(n > 0 for n in [1, 2, 3])     # True
all(n > 0 for n in [1, -2, 3])    # False
all([])                           # True  -- vacuously
```
""",

"14.7 brief": r"""# 14.7 -- reduce: fold a sequence to one value

## Concept

**`reduce`** (from `functools`) **folds** a whole sequence into a single value by
applying a two-argument function cumulatively, left to right:

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])     # 10  ((((1+2)+3)+4))
reduce(lambda a, b: a * b, [1, 2, 3, 4])     # 24
```

- `reduce(func, items)` computes `func(func(func(i0, i1), i2), i3)...` -- each
  step combines the running result with the next item.
- A third argument is a **start** value: `reduce(func, items, start)` begins the
  fold from `start`, which also defines the answer for an **empty** sequence.
- It's the accumulator loop (chapter 3) as a higher-order function. (`sum` is the
  special case for `+`; `reduce` lets you fold with *any* combiner.)

## Example

```python
from functools import reduce

def total(nums):
    return reduce(lambda a, b: a + b, nums, 0)
```

## Your task

Using **`reduce`** from `functools`, define `product(nums)` that returns the
product of all the numbers (with a start of `1`, so the empty list gives `1`).

## Done when

- `product([1, 2, 3, 4])` returns `24`; `product([5])` returns `5`.
- `product([])` returns `1`.
- The fold uses `reduce`, not a manual accumulator loop.
""",

"14.7 hints": r"""`from functools import reduce`. It takes a two-argument combiner, the items, and
a start value.

---

The combiner multiplies the running result by the next number:
`reduce(lambda a, b: a * b, nums, 1)`. The start `1` makes the empty list give 1.

---

from functools import reduce


def product(nums):
    return reduce(lambda a, b: a * b, nums, 1)
""",

"14.7 reference": r"""**`functools.reduce(func, iterable[, start])`** **folds** a sequence into a single
value by applying a two-argument `func` cumulatively, left to right:
`func(func(func(i0, i1), i2), i3)...`. Each step combines the running result with
the next item.

- A **start** value (`reduce(func, items, start)`) seeds the fold and defines the
  result for an **empty** sequence; without it, reducing an empty iterable raises
  `TypeError`.
- It generalises the accumulator loop to *any* combiner: `+` gives a sum, `*` a
  product, `max` the largest. The dedicated `sum` is the `+` special case, and
  `math.prod` the `*` one — but `reduce` folds with whatever function you supply.
- `reduce` lives in `functools` (it's not a built-in), so it must be imported.

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])      # 10
reduce(lambda a, b: a * b, [1, 2, 3, 4], 1)   # 24
reduce(lambda a, b: a if a > b else b, [3, 9, 2])   # 9  (max)
```
""",

"14.8 brief": r"""# 14.8 -- Capstone: a ranked shortlist

## Concept

The chapter's tools chain into a **pipeline**. Given a list of `(name, score)`
records, build a shortlist:

1. **`filter`** to the records that meet a threshold,
2. **`sorted`** with a `key=lambda` (and `reverse=True`) to rank them high to low,
3. **`map`** out just the names.

```python
records = [("Ada", 90), ("Linus", 70), ("Grace", 95)]
qualified = filter(lambda r: r[1] >= 80, records)
ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
list(map(lambda r: r[0], ranked))     # ['Grace', 'Ada']
```

Each record is a tuple, so `r[0]` is the name and `r[1]` the score.

## Your task

Define `passing(records, threshold)` that takes a list of `(name, score)` tuples
and returns the **names** of those with `score >= threshold`, ordered by score
**highest first**, built with `filter`, `sorted(key=lambda ...)`, and `map`.

## Done when

- `passing([("Ada", 90), ("Linus", 70), ("Grace", 95)], 80)` returns
  `["Grace", "Ada"]`.
- `passing([], 50)` returns `[]`; a threshold above every score returns `[]`.
- The result is built by filtering, sorting by a lambda key, and mapping -- a
  pipeline of the chapter's tools.
""",

"14.8 hints": r"""Three steps. First `filter(lambda r: r[1] >= threshold, records)` keeps the
records that qualify (r[1] is the score).

---

Then `sorted(qualified, key=lambda r: r[1], reverse=True)` ranks them high to
low, and `map(lambda r: r[0], ...)` pulls out the names. Wrap the map in `list`.

---

def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
""",

"14.8 reference": r"""The capstone chains the chapter's higher-order functions into a **data
pipeline** — the shape of much real processing:

1. **`filter(lambda r: r[1] >= threshold, records)`** narrows to the records that
   qualify;
2. **`sorted(..., key=lambda r: r[1], reverse=True)`** ranks them by score, high
   to low (stable, so equal scores keep their order);
3. **`map(lambda r: r[0], ...)`** projects out just the field you want — the name.

Each stage takes a function and an iterable and yields another iterable, so they
compose directly: the filter feeds the sort, the sort feeds the map. The same
pipeline could be written with comprehensions; expressing it as
`filter`/`sorted`/`map` is the functional style, and seeing a task *as* a pipeline
of transformations is the skill the chapter builds toward.

```python
def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
```
""",

"15.1 brief": r"""# 15.1 -- Inheritance: build on a base class

## Concept

Chapter 9 built single classes. **Inheritance** lets one class build on another:
a **subclass** automatically gets the **base class's** methods, then adds or
changes its own.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return self.name + " the animal"

class Dog(Animal):           # Dog IS an Animal
    def speak(self):
        return "Woof"
```

- `class Dog(Animal):` makes `Dog` a subclass of `Animal`. A `Dog` instance can
  call `describe()` -- inherited from `Animal` -- *and* `speak()`, its own.
- The relationship is "**is-a**": a `Dog` **is an** `Animal`, so
  `isinstance(dog, Animal)` is `True`.
- Shared behaviour lives once in the base; subclasses don't repeat it.

## Your task

Define a base class `Animal` with an `__init__(self, name)` and a
`describe(self)` returning `"<name> the animal"`. Then define `Dog(Animal)` that
**inherits** from it and adds `speak(self)` returning `"Woof"`.

## Done when

- `Dog("Rex").describe()` returns `"Rex the animal"` (inherited).
- `Dog("Rex").speak()` returns `"Woof"`.
- A `Dog` **is an** `Animal`: it inherits rather than copying `describe`.
""",

"15.1 hints": r"""Write `Animal` first, with `__init__` storing `self.name` and `describe`
returning the sentence. Then `class Dog(Animal):` -- the `(Animal)` is what makes
Dog inherit.

---

Inside `Dog` you only write `speak`; `describe` comes for free from `Animal`.
Don't redefine `describe` in `Dog`.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return self.name + " the animal"


class Dog(Animal):
    def speak(self):
        return "Woof"
""",

"15.1 reference": r"""**Inheritance** lets a class build on another. Writing `class Child(Parent):`
makes `Child` a **subclass**: it automatically has all of `Parent`'s methods, and
can add new ones or replace existing ones.

- The relationship is **"is-a"**: a `Dog(Animal)` *is an* `Animal`, so
  `isinstance(dog, Animal)` is `True` and a `Dog` works anywhere an `Animal` is
  expected.
- Shared behaviour lives **once** in the base class; subclasses inherit it rather
  than copying it, so a fix in the parent reaches every child.
- Python finds a method by walking the **MRO** (method resolution order): the
  instance's class first, then its bases. `object` is the implicit base of every
  class.

```python
class Animal:
    def __init__(self, name): self.name = name
    def describe(self): return self.name + " the animal"

class Dog(Animal):
    def speak(self): return "Woof"

d = Dog("Rex")
d.describe()              # 'Rex the animal'  -- inherited
isinstance(d, Animal)    # True
```
""",

"15.2 brief": r"""# 15.2 -- super(): extend the parent

## Concept

A subclass often needs everything the parent's `__init__` does **plus** a bit
more. **`super()`** gives you the parent, so you call its method and then add to
it -- rather than copying the parent's code:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # run Animal's __init__ (sets self.name)
        self.breed = breed         # then add Dog's own attribute
```

- `super().__init__(name)` calls the **parent's** `__init__` on this instance, so
  `self.name` gets set by `Animal`.
- After that, the child adds what's special to it (`self.breed`).
- This keeps the parent's set-up in one place; if `Animal.__init__` changes, `Dog`
  picks it up automatically.

## Your task

Define `Animal` with `__init__(self, name)` storing `self.name`. Then define
`Dog(Animal)` whose `__init__(self, name, breed)` calls **`super().__init__(name)`**
and then stores `self.breed`.

## Done when

- `Dog("Rex", "Lab").name` is `"Rex"` (set via `super().__init__`).
- `Dog("Rex", "Lab").breed` is `"Lab"`.
- A `Dog` is an `Animal`, and the name is set by the parent, not re-assigned by
  hand.
""",

"15.2 hints": r"""`Dog` takes two arguments. The first, `name`, belongs to `Animal` -- hand it up
with `super().__init__(name)`.

---

After the `super().__init__(name)` line, set `self.breed = breed` for Dog's own
part.

---

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
""",

"15.2 reference": r"""**`super()`** returns a proxy to the **parent class**, so a subclass can call the
parent's method and build on it instead of duplicating its code. The usual case
is `__init__`:

- `super().__init__(args)` runs the parent's initialiser on this instance,
  setting up whatever the parent owns; the child then adds its own attributes.
- It keeps the parent's logic in **one place** — change `Animal.__init__` and
  every subclass that calls `super().__init__` inherits the change.
- `super()` works for any method, not just `__init__`: an overriding method can
  call `super().method()` to reuse the parent's version and extend it.
- With no `super().__init__`, the parent's initialiser does **not** run, so the
  attributes it would set are missing.

```python
class Animal:
    def __init__(self, name): self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # Animal sets self.name
        self.breed = breed         # Dog adds self.breed

Dog("Rex", "Lab").name             # 'Rex'
```
""",

"15.3 brief": r"""# 15.3 -- Overriding: a child's own version

## Concept

A subclass can **override** a parent method -- define its own version of a method
the parent already has. For the subclass's instances, the new version wins:

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."          # generic

class Cat(Animal):
    def speak(self):
        return "Meow"         # Cat's own
```

- `Cat("Felix").speak()` returns `"Meow"`; a plain `Animal(...).speak()` still
  returns `"..."`.
- This is **polymorphism**: the *same* call, `x.speak()`, does the right thing for
  whatever type `x` is.
- The subclass still inherits everything it doesn't override (here, `__init__` and
  `self.name`).

## Your task

Define `Animal` with `__init__(self, name)` and `speak(self)` returning `"..."`.
Then define `Cat(Animal)` that **overrides** `speak` to return `"Meow"`.

## Done when

- `Cat("Felix").speak()` returns `"Meow"`.
- `Animal("thing").speak()` returns `"..."` (unchanged).
- `Cat("Felix").name` is `"Felix"` (inherited `__init__`), and a Cat is an Animal.
""",

"15.3 hints": r"""Give `Animal` both `__init__` and `speak` (returning "..."). Then `Cat(Animal)`
defines its own `speak`.

---

Cat's `speak` simply returns "Meow". Don't redefine `__init__` in Cat -- it's
inherited.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Cat(Animal):
    def speak(self):
        return "Meow"
""",

"15.3 reference": r"""**Overriding** is defining, in a subclass, a method the parent already has. For
the subclass's instances, Python finds the subclass's version first (it's earlier
in the MRO), so the child's behaviour replaces the parent's.

- This is **polymorphism**: one call site, `x.speak()`, runs the right code for
  whatever type `x` actually is — `Cat` says "Meow", a generic `Animal` says
  "...". Calling code needn't know the exact type.
- The subclass still **inherits** everything it does *not* override (here
  `__init__`).
- An override can reuse the parent's version with `super().method()` — extend
  rather than fully replace.

```python
class Animal:
    def speak(self): return "..."
class Cat(Animal):
    def speak(self): return "Meow"

for a in [Animal(), Cat()]:
    print(a.speak())     # '...' then 'Meow' -- same call, different result
```
""",

"15.4 brief": r"""# 15.4 -- @property: a computed attribute

## Concept

Sometimes a value is **derived** from others -- a rectangle's area from its width
and height. You could store it, but then it goes stale when width changes. A
**`@property`** computes it on every access, while still being read like a plain
attribute:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12   -- no parentheses, but the method runs
r.width = 5
r.area        # 20   -- recomputed from the new width
```

- `@property` above a method makes `obj.area` (no `()`) call that method and
  return its result.
- Because it runs each time, the value is always current -- unlike a value stored
  once in `__init__`.

## Your task

Define `Rectangle` with `__init__(self, width, height)` and an **`area`**
**property** that returns `width * height`.

## Done when

- `Rectangle(3, 4).area` is `12` (accessed with no parentheses).
- After `r = Rectangle(3, 4); r.width = 5`, `r.area` is `20` -- recomputed, not
  stored.
""",

"15.4 hints": r"""Write `area` as a normal method that returns `self.width * self.height`, then put
`@property` on the line directly above `def area`.

---

With `@property`, callers write `r.area` (no parentheses) and the method runs each
time, so it always reflects the current width and height.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
""",

"15.4 reference": r"""**`@property`** is a decorator that turns a method into a **computed, read-only
attribute**. `obj.area` (no parentheses) runs the method and returns its result,
so a derived value is recomputed on every access and never goes stale.

- It hides the fact that work happens: callers use `obj.area`, not `obj.area()`,
  exactly as for a stored attribute — but the value always reflects the current
  state.
- A bare `@property` is read-only; assigning to it raises `AttributeError`. Add a
  matching `@area.setter` to allow assignment with validation.
- Prefer a property over a value stored in `__init__` whenever the value *depends*
  on other attributes that can change.

```python
class Rectangle:
    def __init__(self, w, h): self.width, self.height = w, h
    @property
    def area(self): return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12
r.width = 5
r.area        # 20  -- recomputed
```
""",

"15.5 brief": r"""# 15.5 -- @classmethod: an alternative constructor

## Concept

A normal method takes `self` (an instance). A **`@classmethod`** takes **`cls`**
(the class itself), so it can build and return a **new instance** -- a handy way
to offer an alternative, named constructor:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])

p = Point.from_tuple((3, 4))     # called on the class, not an instance
p.x, p.y                          # (3, 4)
```

- `@classmethod` makes `cls` the first parameter -- the class the method is called
  on (`Point` here).
- `cls(...)` is the same as `Point(...)`, but using `cls` means subclasses get an
  instance of *their* type for free.
- You call it on the **class**: `Point.from_tuple(...)`.

## Your task

Define `Point` with `__init__(self, x, y)`, and a **classmethod** `from_tuple(cls,
pair)` that builds a `Point` from a `(x, y)` tuple.

## Done when

- `Point.from_tuple((3, 4)).x` is `3` and `.y` is `4`.
- `from_tuple` is a `@classmethod` taking `cls`, and builds the point with
  `cls(...)`.
""",

"15.5 hints": r"""Write `__init__` as usual. Then add a method decorated with `@classmethod` whose
first parameter is `cls`, not `self`.

---

Inside `from_tuple`, unpack the pair and build the object with `cls`:
`return cls(pair[0], pair[1])`.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])
""",

"15.5 reference": r"""A **`@classmethod`** is bound to the **class**, not an instance: its first
parameter is **`cls`** (the class itself) instead of `self`. Because it has the
class, it can build instances — the classic use is an **alternative constructor**.

- Call it on the class: `Point.from_tuple((3, 4))`. Python passes `Point` as
  `cls`.
- Building with `cls(...)` rather than the literal class name means a **subclass**
  that calls the inherited classmethod gets an instance of *itself*.
- Contrast with **`@staticmethod`**, which takes neither `self` nor `cls` — just a
  plain function namespaced under the class, used when the method needs no access
  to the instance or class.

```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    @classmethod
    def from_tuple(cls, pair): return cls(pair[0], pair[1])

Point.from_tuple((3, 4)).x     # 3
```
""",

"15.6 brief": r"""# 15.6 -- __eq__: value equality

## Concept

By default, `==` on objects asks "are these the **same object**?" -- so two
separately-built objects with identical data are *not* equal. The **`__eq__`**
dunder method changes that to **value equality**:

```python
class Money:
    def __init__(self, cents):
        self.cents = cents
    def __eq__(self, other):
        return self.cents == other.cents

Money(500) == Money(500)     # True   -- same value
Money(500) == Money(750)     # False
```

- Python calls `a.__eq__(b)` for `a == b`. You return whether they should count as
  equal -- usually by comparing the attributes that define the value.
- `!=` is handled for you (it's the negation of `__eq__`).
- (Defining `__eq__` is also what lets your objects be compared in tests, lists,
  and `in` checks by value.)

## Your task

Define `Money` with `__init__(self, cents)` and an **`__eq__`** so two `Money`
objects are equal exactly when their `cents` match.

## Done when

- `Money(500) == Money(500)` is `True`.
- `Money(500) == Money(750)` is `False`.
- Equality compares `cents`, not object identity.
""",

"15.6 hints": r"""Add a method `__eq__(self, other)` to Money. Python calls it for `==`.

---

Return the comparison of the values: `return self.cents == other.cents`.

---

class Money:
    def __init__(self, cents):
        self.cents = cents

    def __eq__(self, other):
        return self.cents == other.cents
""",

"15.6 reference": r"""By default, `==` between objects tests **identity** — whether they are the very
same object — so two independently built objects with identical data compare
unequal. Defining **`__eq__(self, other)`** redefines `==` as **value equality**.

- Python calls `a.__eq__(b)` to evaluate `a == b`; return whether they should
  count as equal, normally by comparing the defining attributes. `!=` follows
  automatically as its negation.
- Value equality is what makes objects work intuitively in `==` tests, in `list`
  membership (`in`), and when comparing results.
- If you define `__eq__`, the class becomes **unhashable** (its `__hash__` is set
  to `None`), so it can't go in a `set` or `dict` key until you also define
  `__hash__` — often `return hash(self.cents)`.

```python
class Money:
    def __init__(self, cents): self.cents = cents
    def __eq__(self, other): return self.cents == other.cents

Money(500) == Money(500)     # True
Money(500) == Money(750)     # False
```
""",

"15.7 brief": r"""# 15.7 -- __lt__: make objects sortable

## Concept

`sorted`, `min`, and `max` all order things using the **`<`** operator. By
default Python doesn't know how to compare two of your objects -- sorting them
raises `TypeError`. Define **`__lt__`** ("less than") and they become sortable:

```python
class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees
    def __lt__(self, other):
        return self.degrees < other.degrees

temps = [Temperature(30), Temperature(10), Temperature(20)]
sorted(temps)        # ordered 10, 20, 30 -- by degrees
```

- Python calls `a.__lt__(b)` for `a < b`. Return whether `a` should come **before**
  `b` -- usually by comparing the attribute you want to sort on.
- `sorted` only needs `<`, so `__lt__` alone makes a list of your objects
  sortable.

## Your task

Define `Temperature` with `__init__(self, degrees)` and an **`__lt__`** so
temperatures compare by `degrees`.

## Done when

- `Temperature(10) < Temperature(20)` is `True`.
- `sorted([Temperature(30), Temperature(10), Temperature(20)])` is ordered
  `10, 20, 30` by degrees.
- Comparison uses `degrees`.
""",

"15.7 hints": r"""Add `__lt__(self, other)` to Temperature. Python calls it for `<`, and `sorted`
uses `<`.

---

Return the comparison of the values: `return self.degrees < other.degrees`. That
single method is enough to make a list sortable.

---

class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees

    def __lt__(self, other):
        return self.degrees < other.degrees
""",

"15.7 reference": r"""**`__lt__(self, other)`** defines the **`<`** operator for your objects, and `<` is
exactly what **`sorted`**, **`min`**, and **`max`** use to order things. Without
it, comparing two of your objects raises `TypeError`; with it, a list of them
sorts directly.

- Python calls `a.__lt__(b)` for `a < b`; return whether `a` should come **before**
  `b`, usually by comparing the attribute you sort on.
- `sorted` needs only `<`, so `__lt__` alone makes objects sortable. The full set
  of ordering dunders is `__lt__`, `__le__`, `__gt__`, `__ge__`.
- `functools.total_ordering` is a class decorator that fills in the other three
  from `__lt__` and `__eq__`, if you want all comparisons.

```python
class Temperature:
    def __init__(self, degrees): self.degrees = degrees
    def __lt__(self, other): return self.degrees < other.degrees

sorted([Temperature(30), Temperature(10), Temperature(20)])   # 10, 20, 30
min([Temperature(30), Temperature(10)]).degrees               # 10
```
""",

"15.8 brief": r"""# 15.8 -- Capstone: a shape hierarchy

## Concept

Pull the chapter together into one small hierarchy. A base `Shape` holds a name
and can describe itself; a `Rectangle` inherits from it, adds size, computes its
area as a property, and compares to other rectangles by area.

```python
class Shape:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return "%s with area %d" % (self.name, self.area)   # uses the property

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height
    def __eq__(self, other):
        return self.area == other.area
    def __lt__(self, other):
        return self.area < other.area
```

Notice `Shape.describe` uses `self.area`, which only `Rectangle` defines -- the
base method works through the subclass's property (polymorphism).

## Your task

Build exactly the two classes above:

- `Shape.__init__(self, name)` and `describe(self)` -> `"<name> with area
  <area>"`.
- `Rectangle(Shape)`: `__init__(self, width, height)` sets the name to
  `"rectangle"` via `super()`, stores width/height; an `area` **property**; and
  `__eq__` / `__lt__` comparing by `area`.

## Done when

- `Rectangle(3, 4).area` is `12`; `.name` is `"rectangle"`; `.describe()` is
  `"rectangle with area 12"`; it is a `Shape`.
- `Rectangle(2, 6) == Rectangle(3, 4)` is `True` (equal areas).
- `sorted([Rectangle(3, 4), Rectangle(1, 1), Rectangle(2, 5)])` is ordered by
  area (1, 10, 12).
""",

"15.8 hints": r"""Start with `Shape`: `__init__(self, name)` and `describe` returning
`"%s with area %d" % (self.name, self.area)`. It refers to `self.area`, which the
subclass will provide.

---

`Rectangle(Shape)`: in `__init__` call `super().__init__("rectangle")`, store
width/height; add `@property area` returning `width * height`; add `__eq__` and
`__lt__` that compare `self.area` to `other.area`.

---

class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return "%s with area %d" % (self.name, self.area)


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area
""",

"15.8 reference": r"""The capstone blends the chapter into one hierarchy, the way real classes are
built:

- **Inheritance** — `Rectangle(Shape)` *is a* `Shape`, so it gets `describe` for
  free and `isinstance(r, Shape)` is true.
- **`super()`** — `Rectangle.__init__` calls `super().__init__("rectangle")` to let
  the base set `self.name`, then adds its own width and height.
- **`@property`** — `area` is computed from width and height on each access, so it
  stays correct when a side changes.
- **Polymorphism** — `Shape.describe` reads `self.area`, which only `Rectangle`
  defines; the base method works through the subclass's property.
- **Dunders** — `__eq__` and `__lt__` (both by area) make rectangles compare and
  sort like built-in values, so `==` and `sorted` just work.

Together these turn a plain object into one that behaves like a first-class
value: it has an identity in a hierarchy, derived data, and meaningful equality
and ordering — the payoff of the whole chapter.

```python
r = Rectangle(3, 4)
r.describe()                              # 'rectangle with area 12'
Rectangle(2, 6) == Rectangle(3, 4)        # True  -- equal areas
sorted([Rectangle(3, 4), Rectangle(1, 1)])   # by area: 1, then 12
```
""",

"16.1 brief": r"""# 16.1 -- Item: a thing with a price

## Project: Shopping Cart

This chapter is a **project**. Across four steps you'll build a small shopping
cart, then assemble it with little hand-holding. The lessons are behind you now
-- here you put them to work.

## Step 1

Every shop needs **items**. Build an `Item` class.

- `__init__(self, name, price)` stores the name and price.
- `label(self)` returns the item as a string `"name: $price"`, with the price to
  **two decimal places** -- e.g. `"Apple: $1.50"`.

## Done when

- `Item("Apple", 1.5).name` is `"Apple"` and `.price` is `1.5`.
- `Item("Apple", 1.5).label()` is `"Apple: $1.50"`.
- `Item("Bread", 2).label()` is `"Bread: $2.00"`.
""",

"16.1 hints": r"""Store `name` and `price` in `__init__`, then write `label` to return the
formatted string.

---

An f-string with a format spec handles the two decimals:
`f"{self.name}: ${self.price:.2f}"`.
""",

"16.2 brief": r"""# 16.2 -- Cart: hold items and total them

## Step 2

Now the **cart** itself. Build a `Cart` class that collects items by name and
price and adds up the bill.

- `__init__(self)` starts an empty cart.
- `add(self, name, price)` adds one item to the cart.
- `total(self)` returns the sum of all the prices (0 for an empty cart).

## Done when

- A new `Cart()` has `total()` of `0`.
- After `add("Apple", 1.5)` and `add("Bread", 2.0)`, `total()` is `3.5`.
- `add` can be called any number of times before `total`.
""",

"16.2 hints": r"""Keep a list on the cart (`self.items = []` in `__init__`); `add` appends to it.

---

`total` sums the prices -- `sum(price for name, price in self.items)` if you store
`(name, price)` pairs.
""",

"16.3 brief": r"""# 16.3 -- Debug: the discount is wrong

## Step 3 -- fix the bug

This time the code is **already written** -- and it has a bug. A `Cart` with a
`discounted_total(percent)` method is meant to take `percent` **per cent** off the
total. But customers are reporting the discount is wildly too large: a 10% coupon
on a \$50 cart is charging \$40 instead of \$45.

Open the workspace, read `discounted_total`, work out what it's actually doing,
and fix it. Leave the rest of the class alone.

## Done when

- `discounted_total(0)` equals the full `total()` (no discount).
- A 10% discount on a \$50 cart gives `45.0`, not `40.0`.
- For any total `t` and percent `p`, `discounted_total(p)` is `t * (1 - p/100)`.
""",

"16.3 hints": r"""A percentage discount scales the total -- it doesn't subtract a flat amount.
Keeping `p`% of `100%` means multiplying by `(1 - p/100)`.
""",

"16.4 brief": r"""# 16.4 -- Capstone: print the receipt

## Step 4 -- the finish, on your own

No walkthrough this time. Put the pieces together.

Write a function `receipt(items)` where `items` is a list of `(name, price)`
pairs. It returns a multi-line string: **one line per item** in `"name: $price"`
form (two decimals), then a final **`"TOTAL: $<total>"`** line.

For `receipt([("Apple", 1.5), ("Bread", 2.0)])`:

```
Apple: $1.50
Bread: $2.00
TOTAL: $3.50
```

## Done when

- Each item is its own line, formatted `"name: $price"` to two decimals.
- The last line is `"TOTAL: $<sum of prices>"`, also to two decimals.
- An empty list returns just `"TOTAL: $0.00"`.
""",
}
