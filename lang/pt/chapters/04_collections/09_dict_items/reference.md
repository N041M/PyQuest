**`d.items()`** produz cada par `(key, value)`, por isso um ciclo `for` com duas
variáveis percorre todo o dicionário, desempacotando cada par à medida que avança.

- `for k, v in d.items():` associa `k` à chave e `v` ao seu valor em cada passagem.
- `d.keys()` e `d.values()` iteram apenas as chaves ou apenas os valores; percorrer
  o dicionário diretamente (`for k in d`) itera as **chaves**.
- A ordem de iteração é a **ordem de inserção** (a ordem em que as chaves foram
  adicionadas pela primeira vez).

```python
prices = {"pen": 2, "ink": 5}
for item, cost in prices.items():
    print(item, cost)        # pen 2 / ink 5
```
