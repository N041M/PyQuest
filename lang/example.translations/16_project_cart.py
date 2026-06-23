# PyQuest translations -- language 'example' -- chapter 16_project_cart -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply example

TRANSLATIONS = {

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
