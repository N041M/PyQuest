**Funkce** zabalí kus práce pod jméno, takže ji lze spustit na vyžádání,
kolikrát je potřeba. **`def`** ji uvádí: hlavička `def jméno():` a odsazené tělo.

- **Volání** — `jméno()` — spustí tělo. Definice funkce ji nespustí; udělá to
  volání.
- **`return hodnota`** předá výsledek zpět volajícímu a funkci okamžitě ukončí.
  Volání `jméno()` se pak *stane* touto hodnotou.
- Funkce bez `return` (nebo s holým `return`) vrátí `None`.

```python
def greet():
    return "hello"

greet()        # 'hello'  -- the call evaluates to the returned value
```
