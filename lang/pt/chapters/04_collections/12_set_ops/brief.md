# 4.12 -- Combinar conjuntos

## Conceito

Os conjuntos podem ser combinados como na matemática:

- **interseção** `a & b` -- itens em **ambos**
- **união** `a | b` -- itens em **qualquer um**
- **diferença** `a - b` -- itens em `a` mas não em `b`

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)    # {2, 3}
print(a | b)    # {1, 2, 3, 4}
print(a - b)    # {1}
```

Estas respondem a perguntas como "que itens dois grupos partilham?" sem escrever
um ciclo. (`a.intersection(b)` e `a.union(b)` fazem o mesmo que `&` e `|`.)

## Exemplo

```python
x = {"a", "b"}
y = {"b", "c"}
print(len(x & y))   # 1   (just "b")
```

## A tua tarefa

Lê um primeiro grupo: uma contagem `n`, depois `n` palavras. Depois um segundo
grupo: uma contagem `m`, depois `m` palavras. Imprime **quantas palavras distintas
aparecem em ambos** os grupos.

Para o primeiro grupo `a`, `b` e o segundo grupo `b`, `c`:

```
1
```

(Apenas `b` está em ambos.)

## Está feito quando

- `{a, b}` e `{b, c}` imprimem `1`.
- Grupos vazios dão `0`; duplicados dentro de um grupo contam uma só vez.
