**Výchozí hodnota** v hlavičce dělá parametr volitelným: vynechá-li volající ten
argument, použije se výchozí hodnota.

- `def greet(name, greeting="hi"):` lze volat `greet("Ada")` (použije `"hi"`) nebo
  `greet("Ada", "hello")` (přepíše ji).
- Parametry **s** výchozí hodnotou musí jít **za** těmi bez ní.
- U měnitelných typů používej *novou* výchozí hodnotu při každém volání — napiš
  `def f(items=None):` a pak `if items is None: items = []`, nikdy
  `def f(items=[]):` (jeden sdílený seznam přetrvá mezi voláními).

```python
def power(base, exp=2):
    return base ** exp

power(5)       # 25  -- exp defaults to 2
power(5, 3)    # 125
```
