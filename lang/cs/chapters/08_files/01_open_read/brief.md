# 8.1 -- Otevření souboru

## Koncept

Dosud každá hodnota pocházela z literálu, který jsi napsal, nebo z `input()`.
Skutečné programy také čtou **soubory** -- text, který už leží na disku.

`open(name)` ti podá *objekt souboru*. Čistý způsob, jak ho použít, je blok `with`:

```python
with open("note.txt") as f:
    text = f.read()
```

- `with open(...) as f:` soubor otevře a naváže ho na `f`;
- `f.read()` vrátí **celý obsah** souboru jako jeden řetězec;
- když blok skončí, Python **soubor za tebe zavře** -- i když kód uvnitř vyvolal
  chybu. To automatické zavření je celý důvod, proč dát `with` přednost před holým
  `open()`.

Soubor se hledá relativně k tomu, kde program běží, takže `"note.txt"` znamená
„soubor jménem note.txt vedle mě“.

## Příklad

Pokud `note.txt` obsahuje:

```
buy milk
call sam
```

pak `text` je řetězec `"buy milk\ncall sam\n"` -- včetně zalomení řádků.

## Tvůj úkol

Vedle tvého programu leží soubor jménem `note.txt`. Přečti jeho celý obsah a vypiš
ho.

## Hotovo, když

- Program vypíše přesně to, co `note.txt` obsahuje.
- Funguje, ať soubor drží cokoli -- jeden řádek, mnoho řádků, nebo nic.
- Soubor jsi otevřel příkazem `with`.
