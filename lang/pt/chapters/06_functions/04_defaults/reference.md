Um **valor por omissão** no cabeçalho torna um parâmetro opcional: se quem chama omite
esse argumento, o valor por omissão é usado.

- `def greet(name, greeting="hi"):` pode ser chamada como `greet("Ada")` (usa `"hi"`) ou
  `greet("Ada", "hello")` (substitui-o).
- Os parâmetros **com** valores por omissão têm de vir **depois** dos que não têm.
- Usa um valor por omissão *novo* em cada chamada para tipos mutáveis — escreve `def f(items=None):`
  depois `if items is None: items = []`, nunca `def f(items=[]):` (uma única lista partilhada
  persiste entre chamadas).

```python
def power(base, exp=2):
    return base ** exp

power(5)       # 25  -- exp defaults to 2
power(5, 3)    # 125
```
