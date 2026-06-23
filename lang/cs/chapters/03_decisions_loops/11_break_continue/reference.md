Dva příkazy mění tok cyklu zevnitř:

- **`break`** cyklus **okamžitě** ukončí, přeskočí všechny zbývající průchody a
  skočí na kód za cyklem. Použij ho, abys zastavil, jakmile najdeš, co potřebuješ.
- **`continue`** přeskočí **zbytek aktuálního průchodu** a skočí rovnou na další
  iteraci cyklu (znovu zkontroluje podmínku / vezme další položku).

Oba ovlivňují pouze **nejvnitřnější** cyklus, který je obklopuje.

```python
for n in range(10):
    if n == 5:
        break             # stop the whole loop at 5
    if n % 2 == 0:
        continue          # skip evens, go to the next n
    print(n)              # 1, 3
```
