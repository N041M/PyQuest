# 8.4 -- Zápis souboru

## Koncept

Čtení je polovina příběhu; programy také **vytvářejí** soubory. Otevři v režimu
`"w"` (pro *write*, zápis) a zavolej `.write()`:

```python
with open("out.txt", "w") as f:
    f.write("hello\n")
```

Dvě věci, které je dobré vědět:

- `"w"` vytvoří úplně nový soubor (nebo existující **vyprázdní**) a pak zapisuje.
- `.write()` položí **přesně** ten text, který mu dáš -- žádné automatické zalomení
  řádku, jaké přidává `print()`. Chceš-li zalomení řádků, zahrň `"\n"` sám.

Častý tvar je **přečti jeden soubor, zapiš jiný**:

```python
with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
```

## Příklad

Pokud `in.txt` obsahuje `quiet please`, pak `out.txt` má nakonec držet
`QUIET PLEASE`.

## Tvůj úkol

Přečti `in.txt` a zapiš jeho obsah **velkými písmeny** (`.upper()` z 2.7) do nového
souboru jménem `out.txt`.

## Hotovo, když

- `out.txt` obsahuje přesně text z `in.txt`, velkými písmeny.
- Prázdný `in.txt` vyprodukuje prázdný `out.txt` -- žádný pád.
- Použil jsi `with` a otevřel `out.txt` v režimu `"w"`.
