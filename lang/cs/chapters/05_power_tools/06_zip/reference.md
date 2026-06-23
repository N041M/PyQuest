**`zip(a, b)`** prochází několik iterovatelných objektů **v zákrytu** a vydává
jednu n-tici odpovídajících položek na průchod — *i*-tou z každého. Spáruje
paralelní posloupnosti bez indexování.

- `for x, y in zip(xs, ys):` naváže `x` a `y` na odpovídající položky při každém
  průchodu.
- Zastaví se u **nejkratšího** vstupu, takže položky navíc v delším se ignorují.
- Lze zipovat libovolný počet iterovatelných objektů; `dict(zip(keys, values))`
  sestaví slovník ze dvou paralelních seznamů.

```python
names, scores = ["Ada", "Linus"], [90, 85]
for n, s in zip(names, scores):
    print(n, s)           # Ada 90 / Linus 85
```
