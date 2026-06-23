# PyQuest translations -- language 'example' -- chapter 03_decisions_loops -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply example

TRANSLATIONS = {

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
}
