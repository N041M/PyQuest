Uma cadeia de caracteres é uma sequência ordenada de caracteres, e `s[index]` lê o que está numa
determinada posição. As posições são **baseadas em zero**: o primeiro caractere é `s[0]`, o
segundo `s[1]`, e assim por diante.

- O resultado é, em si, uma cadeia de um único caractere (o Python não tem um tipo
  de caractere separado).
- Um índice igual ou superior ao comprimento gera `IndexError`; para uma cadeia de
  comprimento *n*, as posições válidas vão de `0` a `n - 1`.
- As cadeias de caracteres são **imutáveis** — indexar lê um caractere, mas `s[0] = "x"` é um
  erro. Para alterar o texto, constrói-se uma nova cadeia.

```python
word = "Python"
word[0]    # 'P'
word[3]    # 'h'
```
