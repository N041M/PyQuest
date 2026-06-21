# 16.4 -- Capstone: print the receipt

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
