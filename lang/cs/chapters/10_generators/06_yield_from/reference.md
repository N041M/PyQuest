**`yield from iterable`** znovu vydá **každou** položku, kterou iterovatelný objekt
vyprodukuje, jako bys napsal cyklus `yield`ů. Deleguje celý dílčí stream jedním
řádkem.

- `yield from sub` je ekvivalentní `for x in sub: yield x`, ale kratší a rychlejší
  — a funguje se seznamy, rozsahy, jinými generátory, libovolným iterovatelným
  objektem.
- Je to nástroj na **zploštění** nebo **zřetězení**: generátor může `yield from`
  několik zdrojů po sobě, aby spletl jejich streamy dohromady.

```python
def chain(a, b):
    yield from a
    yield from b            # splice two streams into one

list(chain([1, 2], [3, 4]))     # [1, 2, 3, 4]
```
