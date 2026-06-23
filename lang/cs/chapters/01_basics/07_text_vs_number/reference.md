Každá hodnota má **typ**. Dva základní se objevují hned:

- **řetězec** (`str`) je text psaný v uvozovkách: `"42"`, `"hello"`;
- **celé číslo** (`int`) je číslo psané jako holé číslice: `42`.

Celý rozdíl jsou uvozovky. `type("42")` je `str`; `type(42)` je `int`.

Typ rozhoduje, co operátor znamená. `+` mezi dvěma **řetězci** je *zřetězí*
(spojí); `+` mezi dvěma **čísly** je *sečte*:

```python
"2" + "2"   # "22"  -- text joined
 2  +  2    #  4    -- numbers added
```

Míchání obou pomocí `+` je chyba (`TypeError`), protože Python nebude hádat, jestli
jsi chtěl sčítat, nebo spojovat. Nejprve explicitně převeď: `int("2") + 2` je `4`
a `"$" + str(2)` je `"$2"`.
