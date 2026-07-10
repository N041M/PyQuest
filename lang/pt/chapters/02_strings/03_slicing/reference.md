Uma **fatia** `s[start:stop]` devolve uma nova cadeia contendo os caracteres desde a
posição `start` até **mas sem incluir** `stop` — um intervalo *semiaberto*. O
comprimento do resultado é `stop - start` (quando ambos estão dentro do intervalo).

- `s[2:5]` dá os caracteres nos índices 2, 3, 4 — três caracteres.
- Qualquer um dos limites pode ser omitido: `s[:3]` começa no início, `s[3:]` vai até
  ao fim, e `s[:]` copia a cadeia inteira.
- O fatiamento nunca gera erro para limites fora do intervalo — em vez disso, ajusta-os.
  `s[:100]` numa cadeia curta devolve simplesmente tudo o que ela tem.

```python
s = "Python"
s[0:3]    # 'Pyt'
s[:2]     # 'Py'
s[2:]     # 'thon'
```
