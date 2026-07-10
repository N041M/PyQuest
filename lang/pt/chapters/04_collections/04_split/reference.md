**`s.split()`** divide uma cadeia de caracteres numa **lista de partes**. Sem
argumentos, divide em sequências de **espaço em branco** e descarta os espaços no
início/fim — a forma habitual de obter as palavras de uma linha.

- `s.split(sep)` divide exatamente pelo separador `sep`, mantendo partes vazias
  entre separadores adjacentes (`"a,,b".split(",")` é `["a", "", "b"]`).
- `s.split(sep, maxsplit)` divide no máximo `maxsplit` vezes — útil para separar um
  prefixo, por exemplo `"key=a=b".split("=", 1)` é `["key", "a=b"]`.
- É o inverso de `join` (a seguir).

```python
"the quick fox".split()        # ['the', 'quick', 'fox']
"2024-01-15".split("-")        # ['2024', '01', '15']
```
