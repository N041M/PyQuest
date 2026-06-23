**Filtrovací** průchod přečte jeden soubor, ponechá jen řádky, které přijme `if`,
a zapíše je do jiného — souborová podoba vzoru komprehenze-s-`if`.

- Otevři zdroj pro čtení a cíl pro zápis, projdi zdroj a `f_out.write(line)` jen
  tehdy, když řádek projde tvým testem.
- Řádky ze vstupu si ponechají zalomení, takže jejich zpětný zápis reprodukuje
  zalomení řádků, aniž by nějaké přidal.
- Číst a zapisovat **tutéž** cestu najednou je nebezpečné; zapisuj do nového
  souboru (nebo posbírej výsledky a pak zapiš).

```python
with open("all.txt") as src, open("kept.txt", "w") as out:
    for line in src:
        if "ERROR" in line:
            out.write(line)       # keep only matching lines
```
