Três operações fundamentais com cadeias de caracteres:

- **`len(s)`** devolve o número de caracteres em `s` como um `int`; `len("")`
  é `0`.
- **`+` concatena**: `"ab" + "cd"` é `"abcd"`. Ambos os operandos têm de ser cadeias
  — `"n" + 5` gera `TypeError`; converte primeiro com `str(5)`.
- **`*` repete**: `s * n` (ou `n * s`) junta `n` cópias. `"ab" * 3` é
  `"ababab"`; `n <= 0` dá a cadeia vazia `""`.

As três produzem cadeias **novas** e deixam as originais inalteradas (as cadeias de
caracteres são imutáveis).

```python
s = "ab"
len(s)    # 2
s + "c"   # 'abc'
s * 3     # 'ababab'
```
