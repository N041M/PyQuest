O conteúdo de um ficheiro é sempre **texto**, por isso uma linha como `"42\n"`
é uma *cadeia de caracteres*. Para fazer contas tens de converter primeiro
cada linha num número.

- `int(line)` interpreta um inteiro; tolera espaços em branco à volta
  (incluindo a quebra de linha final), por isso `int("42\n")` é `42`. Usa
  `float(line)` para decimais.
- Uma linha em branco ou não numérica gera `ValueError` — salta as linhas em
  branco (`if not line.strip(): continue`) ou envolve a conversão num `try`.
- Acumula à medida que avanças: mantém um total corrente e soma cada valor
  interpretado.

```python
total = 0
with open("nums.txt") as f:
    for line in f:
        total += int(line)    # text -> number, then add
```
