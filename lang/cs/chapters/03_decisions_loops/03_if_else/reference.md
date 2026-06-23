Klauzule **`else`** dá `if` druhou větev: její blok se spustí přesně tehdy, když
je podmínka `if` **nepravdivá**. Společně tvoří dvojcestnou volbu — vždy se spustí
jedna, nebo druhá větev, nikdy obě.

- `else` nebere žádnou podmínku; je to záchytný případ pro „`if` byl nepravdivý“.
- Musí se párovat s `if` na stejném odsazení a jeho blok je odsazený stejně.

```python
if n % 2 == 0:
    print("even")
else:
    print("odd")        # runs only when n % 2 == 0 is False
```
