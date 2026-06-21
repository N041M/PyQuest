# 16.1 -- Item: a thing with a price

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
