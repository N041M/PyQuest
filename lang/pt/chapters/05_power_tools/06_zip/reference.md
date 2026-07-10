**`zip(a, b)`** percorre vários iteráveis **em sincronia**, produzindo um tuplo de
itens correspondentes por passagem — o *i*-ésimo de cada um. Empareira sequências paralelas
sem usar índices.

- `for x, y in zip(xs, ys):` liga `x` e `y` aos itens correspondentes em cada passagem.
- Para no iterável **mais curto**, por isso os itens extra num mais comprido são ignorados.
- Qualquer número de iteráveis pode ser combinado com `zip`; `dict(zip(keys, values))` constrói um dicionário
  a partir de duas listas paralelas.

```python
names, scores = ["Ada", "Linus"], [90, 85]
for n, s in zip(names, scores):
    print(n, s)           # Ada 90 / Linus 85
```
