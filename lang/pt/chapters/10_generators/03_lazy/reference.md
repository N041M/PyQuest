Os geradores são **preguiçosos**: cada valor só é calculado quando pedido,
por isso um gerador pode descrever uma sequência **infinita** e ainda assim
ser útil — retiras apenas os valores de que precisas.

- Um `while True: yield n; n += 1` infinito nunca termina sozinho, mas quem
  consome pode parar mais cedo (um `break`, ou `next` chamado algumas
  vezes).
- A preguiça significa que um gerador guarda essencialmente **nenhuma
  memória** para a sequência — guarda apenas o seu estado atual, não cada
  valor — ao contrário de uma lista que os materializa todos.

```python
def naturals():
    n = 0
    while True:
        yield n             # endless, but only as far as asked
        n += 1

g = naturals(); next(g), next(g)   # (0, 1)
```
