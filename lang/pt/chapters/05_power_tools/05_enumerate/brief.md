# 5.5 -- enumerate()

## Conceito

Às vezes um ciclo precisa tanto do **item** como da sua **posição**. Podias controlar
um contador à mão, mas o Python tem uma função nativa exatamente para isto:

```python
words = ["tea", "milk"]
for i, w in enumerate(words):
    print(i, w)
# 0 tea
# 1 milk
```

Em cada passagem, o `enumerate` entrega-te um par `(posição, item)`, que desempacotas
em duas variáveis (4.7) -- o mesmo truque de `for k, v in d.items()`.

Contar a partir de `0` raramente é o que queres *mostrar* a uma pessoa. O segundo
argumento define o número inicial:

```python
for i, w in enumerate(words, 1):
    print(i, w)
# 1 tea
# 2 milk
```

## Exemplo

```python
for i, ch in enumerate("hi", 1):
    print(f"{i}. {ch}")
# 1. h
# 2. i
```

## A tua tarefa

Lê uma contagem `n`, depois `n` palavras. Imprime-as como uma lista numerada a começar em 1,
no formato `1. palavra` (um ponto e um espaço depois do número).

Para a entrada `3`, depois `tea`, `milk`, `sugar`:

```
1. tea
2. milk
3. sugar
```

## Está feito quando

- Três palavras imprimem-se como `1. ...`, `2. ...`, `3. ...`.
- Uma contagem de `0` não imprime nada.
- Usaste `enumerate()` -- sem contador guardado à mão.
