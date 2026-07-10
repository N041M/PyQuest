# 2.8 -- Substituir e contar

## Conceito

Mais dois métodos de cadeias de caracteres:

- `s.replace(old, new)` devolve uma cópia de `s` com **todas** as ocorrências de `old`
  trocadas por `new`:
  ```python
  "banana".replace("a", "o")   # "bonono"
  ```
- `s.count(sub)` devolve **quantas vezes** `sub` aparece (um número):
  ```python
  "banana".count("a")          # 3
  ```

Se `old` não estiver presente, `replace` devolve a cadeia sem alterações; se `sub` não
estiver presente, `count` devolve `0`.

## Exemplo

```python
s = "foo bar"
print(s.replace("o", "0"))   # f00 bar
print(s.count("o"))          # 2
```

## A tua tarefa

Lê uma linha e imprime duas linhas:

1. a linha com todas as letras `o` substituídas por um zero `0`
2. quantos `o`s havia na linha **original**

Para a entrada `foobar` a saída é:

```
f00bar
2
```

## Está feito quando

- Para `foobar` as linhas são `f00bar` e `2`.
- Para uma linha sem nenhum `o` imprime a linha sem alterações e `0`. O verificador testa
  isso.
