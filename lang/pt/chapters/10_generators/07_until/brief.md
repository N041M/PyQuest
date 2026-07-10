# 10.7 -- parar mais cedo

## Conceito

Um gerador termina no momento em que a sua função termina -- e um `return`
simples (sem valor) dentro de um gerador significa "para agora, sem mais
itens". Portanto um gerador pode decidir **terminar mais cedo**, antes de a
entrada se esgotar.

```python
def before_blank(words):
    for w in words:
        if w == "":
            return          # stop the generator here
        yield w
```

`list(before_blank(["a", "b", "", "c"]))` é `["a", "b"]` -- assim que se
chega ao vazio, o `return` termina o gerador e `"c"` nunca é produzido.

## Exemplo

```python
def while_positive(nums):
    for n in nums:
        if n <= 0:
            return
        yield n

list(while_positive([3, 1, -1, 5]))    # [3, 1]
```

## A tua tarefa

Define um gerador `until_zero(nums)` que produz cada número **até chegar a
um `0`**, depois para. O próprio `0`, e tudo depois dele, **não** é
produzido. Se não houver nenhum `0`, produz a lista toda.

## Está feito quando

- `list(until_zero([1, 2, 0, 3]))` é `[1, 2]`.
- `list(until_zero([0, 9]))` é `[]`; `list(until_zero([1, 2, 3]))` é
  `[1, 2, 3]`.
- Usas `yield`, e paras mais cedo quando encontras um `0`.
