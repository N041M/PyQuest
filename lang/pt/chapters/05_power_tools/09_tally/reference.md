O padrão de **contagem** conta quantas vezes aparece cada coisa distinta, usando um
dicionário cujas chaves são as coisas e cujos valores são contagens correntes.

- Para cada item, `counts[k] = counts.get(k, 0) + 1` lê a contagem atual
  (`0` na primeira vez que a chave é vista, através do valor por omissão do `.get`) e escreve mais um.
- Começa a partir de um dicionário vazio `{}`; as chaves aparecem à medida que são encontradas pela primeira vez.
- O `collections.Counter` da biblioteca padrão faz isto num só passo, mas o
  idioma `.get(k, 0) + 1` mostra exatamente o que está a acontecer.

```python
counts = {}
for w in ["a", "b", "a"]:
    counts[w] = counts.get(w, 0) + 1   # {'a': 2, 'b': 1}
```
