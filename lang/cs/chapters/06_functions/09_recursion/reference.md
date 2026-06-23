**Rekurzivní** funkce volá **sebe sama**, aby vyřešila menší verzi téhož
problému. Dvě části jsou nezbytné:

- **základní případ**, který vrací přímo **bez** rekurze — to rekurzi zastaví;
- **rekurzivní případ**, který funkci zavolá na menším vstupu a staví na výsledku,
  přičemž se pokaždé posouvá k základnímu případu.

Vynech nebo nikdy nedosáhni základního případu a volání se vnořují, dokud Python
nevyvolá `RecursionError`. Mnoho rekurzí má jednodušší tvar cyklem; rekurze zazáří,
když je problém sám sobě podobný.

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)   # smaller subproblem

factorial(4)   # 24
```
