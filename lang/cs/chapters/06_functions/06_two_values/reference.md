Funkce vrací **jeden** objekt, ale tím objektem může být **n-tice**, takže
`return a, b` předá několik hodnot najednou (Python je zabalí do n-tice). Volající
je **rozbalí** odpovídajícími jmény.

- `return lo, hi` vrátí n-tici `(lo, hi)`; `low, high = bounds(xs)` ji rozbalí do
  dvou jmen.
- Při rozbalování se počty musí shodovat. Chceš-li, zachyť celou n-tici jedním
  jménem: `result = bounds(xs)` a pak `result[0]`, `result[1]`.

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4
```
