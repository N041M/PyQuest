`input` přečte **jeden řádek** ze standardního vstupu — vše, co uživatel napíše,
než stiskne Enter — odstraní koncový znak nového řádku a vrátí to jako **řetězec**.

- Návratová hodnota je *vždy* `str`, i když uživatel napsal číslice: `input()` při
  `42` vrátí `"42"`, ne `42`. Pro počítání to převeď (viz `int()`).
- Volitelný argument `prompt` se nejprve vypíše na obrazovku, bez koncového nového
  řádku, takže uživatel píše na stejný řádek.
- Pokud vstupní proud skončí a není co číst (konec souboru), `input` vyvolá
  `EOFError`.

```python
name = input("Your name? ")   # prompts, then reads a line
print("Hi, " + name)
```
