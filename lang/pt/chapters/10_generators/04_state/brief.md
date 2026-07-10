# 10.4 -- um gerador tem memória

## Conceito

Porque um gerador **pausa** em vez de terminar, as suas variáveis locais
mantêm-se vivas entre `yield`s. Um valor que vais construindo sobrevive a
cada pausa -- o gerador retoma exatamente onde parou, acumulador e tudo.

```python
def tally(words):
    seen = 0
    for w in words:
        seen = seen + 1
        yield seen          # 1, then 2, then 3, ... -- `seen` is remembered
```

`list(tally(["a", "b", "c"]))` é `[1, 2, 3]`. O contador `seen` não é
reposto a cada passagem; mantém o seu valor ao longo dos yields.

## Exemplo

```python
def running_max(nums):
    best = None
    for n in nums:
        if best is None or n > best:
            best = n
        yield best
```

`list(running_max([3, 1, 5]))` é `[3, 3, 5]` -- cada item é o maior visto
**até agora**.

## A tua tarefa

Define um gerador `running_total(nums)` que produz a **soma acumulada** de
`nums`: cada valor é o total de todos os números até e incluindo o atual.
Uma lista vazia não produz nada.

## Está feito quando

- `list(running_total([3, 1, 2]))` é `[3, 4, 6]`.
- `list(running_total([5]))` é `[5]`; `list(running_total([]))` é `[]`.
- Usas `yield`, e uma variável que transporta o total ao longo dos yields.
