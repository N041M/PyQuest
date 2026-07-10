**`yield from iterável`** reemite **todos** os itens que o iterável produz,
como se tivesses escrito um ciclo de `yield`s. Delega um subfluxo inteiro
numa linha.

- `yield from sub` é equivalente a `for x in sub: yield x`, mas mais curto e
  mais rápido — e funciona com listas, intervalos, outros geradores,
  qualquer iterável.
- É a ferramenta para **achatar** ou **encadear**: um gerador pode fazer
  `yield from` de várias fontes sucessivamente para unir os seus fluxos.

```python
def chain(a, b):
    yield from a
    yield from b            # splice two streams into one

list(chain([1, 2], [3, 4]))     # [1, 2, 3, 4]
```
