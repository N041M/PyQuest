# 3.1 -- Booleanos e comparação

## Conceito

Um **booleano** é um valor que é `True` ou `False` -- uma resposta sim/não.
É o seu próprio tipo (`bool`), escrito com letra maiúscula.

Obténs booleanos ao **comparar** valores:

| operador | significado |
|---|---|
| `==` | igual a |
| `!=` | diferente de |
| `<`  | menor que |
| `>`  | maior que |
| `<=` | menor ou igual a |
| `>=` | maior ou igual a |

```python
print(3 < 5)      # True
print(3 == 5)     # False
print(7 >= 7)     # True
```

Repara que `==` (comparar) tem **dois** sinais de igual. Um único `=` *atribui* uma
variável; `==` *pergunta "isto é igual?"*.

## Exemplo

```python
a = 4
b = 9
print(a > b)      # False
```

## A tua tarefa

Lê dois números inteiros (cada um na sua própria linha). Imprime se o **primeiro é
maior do que o segundo** -- isto é, imprime o resultado de `first > second`
(que será `True` ou `False`).

Para a entrada `8` seguida de `3`, a saída é:

```
True
```

## Está feito quando

- Para `8` seguido de `3` imprime `True`; para `2` seguido de `5` imprime `False`.
- Quando os dois números são iguais imprime `False` (igual não é "maior").
