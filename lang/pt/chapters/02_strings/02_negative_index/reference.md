Um índice **negativo** conta a partir do fim da cadeia: `s[-1]` é o último
caractere, `s[-2]` o penúltimo, e assim por diante. Poupa-te a escrever
`s[len(s) - 1]`.

- `s[-1]` e `s[len(s) - 1]` designam o mesmo caractere; a forma negativa apenas
  não precisa do comprimento.
- O intervalo negativo válido vai de `-1` até `-len(s)`; ir mais além (por exemplo,
  `s[-99]` numa cadeia curta) gera `IndexError`.
- `s[0]` é o primeiro caractere; não existe `-0` (isso é apenas `0`).

```python
word = "Python"
word[-1]   # 'n'
word[-2]   # 'o'
```
