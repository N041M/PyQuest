Uma função que contém **`yield`** é uma **função geradora**. Chamá-la não
executa o corpo — devolve um **objeto gerador** que produz valores um de
cada vez, **pausando** em cada `yield` e retomando de onde parou quando é
pedido o seguinte.

- Cada `yield valor` entrega um valor a quem está a iterar, depois congela o
  estado da função até que o próximo valor seja pedido.
- Consomes um gerador iterando-o (`for x in gen:`) ou com `next(gen)`.
- Isto difere de `return`, que devolve **um** valor e termina a função
  definitivamente.

```python
def two():
    yield 1
    yield 2

for n in two():
    print(n)            # 1, then 2
```
