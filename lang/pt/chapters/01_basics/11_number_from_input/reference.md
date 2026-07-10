`int` converte um valor num **inteiro**. O seu uso mais comum é transformar a
**cadeia de caracteres** que `input()` devolve num número com que podes calcular.

- `int("42")` é `42`. Espaços em branco à volta são ignorados (`int(" 42 ")` funciona);
  um sinal inicial é permitido (`int("-5")`).
- Texto que não seja um número inteiro levanta `ValueError` — `int("3.5")` e
  `int("ten")` falham ambos. Para decimais, usa `float("3.5")`.
- Chamado sobre um `float`, `int` trunca *em direção a zero* (`int(3.9)` é `3`,
  `int(-3.9)` é `-3`).

Como `input()` produz sempre texto, ler um número é um idioma de dois passos:

```python
n = int(input("How many? "))   # read text, then parse it to an int
print(n * 2)
```
