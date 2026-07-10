# 4.9 -- Percorrer um dicionário num ciclo

## Conceito

Para visitar tudo num dicionário, percorre `.items()` num ciclo, que dá cada
**chave e valor** em conjunto:

```python
ages = {"sam": 20, "ada": 36}
for name, age in ages.items():
    print(name, age)      # sam 20, then ada 36
```

A parte `for name, age in ...` está a desempacotar cada par em duas variáveis. Os
dicionários lembram-se da ordem em que as chaves foram inseridas, por isso
obténs-las de volta por essa ordem.

Existem também `.keys()` (apenas as chaves) e `.values()` (apenas os valores), mas
`.items()` é o habitual quando precisas de ambos.

## Exemplo

```python
d = {"x": 1, "y": 2}
for k, v in d.items():
    print(f"{k}={v}")     # x=1, then y=2
```

## A tua tarefa

Lê uma contagem `n`, depois `n` pares de uma **palavra** e um **número** para um
dicionário. Depois imprime uma linha `key=value` para cada par, pela ordem em que
foram adicionados.

Para a entrada `2`, `a`, `1`, `b`, `2`:

```
a=1
b=2
```

## Está feito quando

- `a=1`, `b=2` são impressos pela ordem de inserção.
- Uma contagem de `0` não imprime nada.
