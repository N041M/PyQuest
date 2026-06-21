# 16.2 -- Cart: hold items and total them

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
