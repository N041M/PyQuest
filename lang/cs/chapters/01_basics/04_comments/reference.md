`#` zahajuje **komentář**: od `#` do konce daného řádku Python text ignoruje.
Komentáře vysvětlují, *proč* kód něco dělá; na samotný běh nemají vliv.

- Komentář může být na vlastním řádku nebo následovat za kódem na stejném řádku
  (`x = 1  # nastavení`).
- `#` uvnitř řetězcového literálu je jen znak, ne komentář (`"#1"` je text `#1`).
- Python **nemá syntaxi pro blokové komentáře**: okomentuj každý řádek pomocí `#`,
  nebo — pro jednorázový blok — použij řetězcový literál, který se vyhodnotí a
  zahodí.

„Zakomentování“ řádku (dání `#` před něj) je nejrychlejší způsob, jak ho vypnout
bez smazání.

```python
# this whole line is ignored
print("hi")   # and this trailing note is too
```
