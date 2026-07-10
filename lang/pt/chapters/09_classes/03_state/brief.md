# 9.3 -- Estado que se lembra

## Conceito

Os dados de um objeto vivem **entre** chamadas de métodos -- um método pode
alterar `self`, e a chamada seguinte vê a alteração. É isso que torna os
objetos úteis: eles *lembram-se*.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count = self.count + 1
        return self.count
```

Cada `tick()` aumenta `self.count` e devolve o novo valor:

```python
c = Counter()
c.tick()   # 1
c.tick()   # 2
c.tick()   # 3
```

Crucialmente, a contagem vive **na instância** (`self.count`), por isso dois
contadores mantêm totais separados -- fazer tick num nunca toca no outro.

## A tua tarefa

Define uma classe `Counter` que começa o seu `count` em `0`. Acrescenta um
método `tick()` que soma um à contagem e **devolve a nova contagem**.

## Está feito quando

- Um `Counter` novo, chamado três vezes, devolve `1`, `2`, `3`.
- Dois contadores são independentes -- fazer tick num não altera o outro.
- A contagem está guardada em `self`, não partilhada entre todos os
  contadores.
