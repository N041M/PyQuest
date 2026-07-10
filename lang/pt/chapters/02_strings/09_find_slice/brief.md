# 2.9 -- Encontrar uma posição

## Conceito

`s.find(sub)` devolve o **índice** onde `sub` aparece pela primeira vez -- um número que podes
depois usar para fatiar. (Se `sub` não for encontrado, devolve `-1`.)

```python
s = "name=Sam"
i = s.find("=")    # 4
print(i)           # 4
print(s[i+1:])     # Sam   (everything after the "=")
```

Portanto, `find` localiza um marcador, e uma fatia extrai a parte que queres em relação a ele.
Aqui `s[i+1:]` significa "de uma posição depois do `=` até ao fim".

## Exemplo

```python
s = "color=blue"
i = s.find("=")
print(s[i+1:])     # blue
```

## A tua tarefa

Cada entrada é uma linha com a forma `key=value` (com um único `=`). Imprime apenas o
**valor** -- tudo o que vem depois do `=`.

Para a entrada `color=blue` a saída é:

```
blue
```

## Está feito quando

- Para `color=blue` imprime `blue`.
- Para `x=1` imprime `1`; para `a=` imprime uma linha vazia; para `k=a=b` imprime
  `a=b` (só o primeiro `=` a divide). O verificador testa estes casos.
