# 2.6 -- Comprimento, juntar, repetir

## Conceito

Três ferramentas do dia a dia para cadeias de caracteres:

- `len(s)` dá o **número de caracteres** em `s` (um número):
  ```python
  len("cat")    # 3
  ```
- `+` junta duas cadeias (já viste isto no capítulo 1):
  ```python
  "cat" + "!"   # "cat!"
  ```
- `*` com um número **repete** uma cadeia:
  ```python
  "ab" * 3      # "ababab"
  "-" * 5       # "-----"
  ```

`len` devolve um número, por isso podes fazer contas com ele. `+` e `*` constroem
novas cadeias.

## Exemplo

```python
s = "hi"
print(len(s))    # 2
print(s + "!")   # hi!
print(s * 3)     # hihihi
```

## A tua tarefa

Lê uma palavra e imprime três linhas:

1. o número de caracteres na palavra
2. a palavra com um ponto de exclamação adicionado no fim
3. a palavra repetida três vezes

Para a entrada `hi` a saída é:

```
2
hi!
hihihi
```

## Está feito quando

- Para `hi` as três linhas são `2`, `hi!`, `hihihi`.
- Também funciona para uma entrada vazia: `0`, `!`, e uma linha vazia. O
  verificador testa isso.
