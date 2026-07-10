# 5.3 -- min() e max()

## Conceito

Encontrar o item mais pequeno ou maior é outro ciclo que podias escrever à mão
("guarda o melhor até agora, compara cada item") -- e outro ciclo que o Python traz como
função nativa:

```python
nums = [3, 7, 1]
print(min(nums))    # 1
print(max(nums))    # 7
```

`min()` e `max()` recebem uma lista (na verdade, qualquer coleção não vazia) e devolvem
o seu item mais pequeno / maior. Também funcionam com cadeias de caracteres -- "mais pequeno" então
significa mais cedo na ordem alfabética:

```python
min("cab")     # "a"
```

Um cuidado: numa lista **vazia** rebentam (não há mais pequeno de
nada), por isso este puzzle garante pelo menos um número.

## Exemplo

```python
nums = [4, -2, 9]
print(min(nums))    # -2
print(max(nums))    # 9
```

## A tua tarefa

Lê uma contagem `n` (sempre pelo menos 1), depois `n` números inteiros. Imprime duas linhas:
o mais pequeno, depois o maior.

Para a entrada `3`, depois `4`, `-2`, `9`:

```
-2
9
```

## Está feito quando

- `4, -2, 9` imprime `-2` depois `9`.
- Um único número imprime-se a si próprio duas vezes (é ao mesmo tempo o mínimo e o máximo).
- Usaste `min()` e `max()`.
