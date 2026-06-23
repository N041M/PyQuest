`print` zapíše textovou reprezentaci každého argumentu na standardní výstup
(terminál), v pořadí, a pak zapíše `end` (ve výchozím nastavení znak nového
řádku). Je to hlavní způsob, jak program ukáže uživateli výsledek.

- Každá hodnota se nejprve převede na text pomocí `str()`, takže `print(42)` i
  `print("42")` zobrazí `42`.
- Při více argumentech se `sep` (výchozí jedna mezera) vkládá *mezi* sousední
  hodnoty — nikdy před první ani za poslední.
- `end` se přidá jednou, na úplný konec. Protože jeho výchozí hodnota je `"\n"`,
  každé volání `print` ukončí aktuální řádek a další výstup začne znovu.
- `print` vrací `None`; volá se kvůli svému vedlejšímu účinku, ne kvůli návratové
  hodnotě.

```python
print("Hello, World!")        # Hello, World!
print("a", "b", "c")          # a b c
```
