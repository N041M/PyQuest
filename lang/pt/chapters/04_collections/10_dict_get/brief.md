# 4.10 -- Chaves inexistentes e .get()

## Conceito

Procurar uma chave que não está no dicionário com `d[key]` **falha** (gera um
`KeyError`):

```python
ages = {"sam": 20}
print(ages["lee"])    # KeyError!
```

`.get()` é a forma segura. Devolve `None` para uma chave inexistente em vez de
falhar -- ou um **valor por omissão** que forneças:

```python
print(ages.get("lee"))        # None
print(ages.get("lee", 0))     # 0      (your default)
print(ages.get("sam", 0))     # 20     (key exists, so its value)
```

Portanto, `d.get(key, default)` significa "o valor se a chave existir, caso
contrário `default`".

## Exemplo

```python
d = {"a": 1}
print(d.get("a", 0))    # 1
print(d.get("z", 0))    # 0
```

## A tua tarefa

Lê uma contagem `n`, depois `n` pares de uma palavra e um número para um
dicionário. Depois lê uma **palavra de consulta** e imprime o seu número -- mas se
a palavra não estiver no dicionário, imprime `0` em vez disso (não falhes).

Para a entrada `2`, `a`, `1`, `b`, `2`, seguida da consulta `c`:

```
0
```

(`c` não é uma chave, por isso é impresso o valor por omissão `0`.)

## Está feito quando

- Uma chave existente imprime o seu valor; uma chave inexistente imprime `0`.
- Nunca falha com uma chave inexistente (usa `.get`).
