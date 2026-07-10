O argumento **`key=`** de `sorted` é uma função que faz corresponder cada
item ao valor pelo qual ordenar, permitindo-te ordenar por algo **derivado** dos
itens em vez dos próprios itens. Uma **`lambda`** em linha é a forma idiomática
de escrever essa chave.

- `key` é chamada **uma vez por item**; `sorted` ordena os itens pelos
  valores-chave resultantes, mas devolve os itens originais. `sorted(words,
  key=len)` ordena por comprimento, `sorted(words, key=lambda w: w[-1])` pela
  última letra.
- `sorted` é **estável**: itens com chaves iguais mantêm a ordem de entrada.
- Combina `key=` com **`reverse=True`** para ordenar de forma decrescente. O
  mesmo `key=` funciona em `list.sort`, `min`, e `max`.

```python
sorted(["pear", "fig", "apple"], key=len)            # ['fig', 'pear', 'apple']
sorted([-3, 1, -2], key=lambda n: abs(n))            # [1, -2, -3]
sorted(records, key=lambda r: r[1], reverse=True)    # by 2nd field, high first
```
