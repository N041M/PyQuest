# 16.3 -- Debug: the discount is wrong

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
