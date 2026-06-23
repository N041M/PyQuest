Cyklus se **zarážkou** (sentinel) opakovaně čte hodnoty a zastaví se, když uvidí
speciální „stop“ hodnotu, ne po pevném počtu. Vzorem je `while`, jehož podmínka
porovnává nejnovější vstup se zarážkou.

- Přečti jednou před cyklem (nebo čti na začátku každého průchodu), pak porovnej
  se zarážkou, abys rozhodl, zda pokračovat.
- Samotná zarážka se **nezpracovává** — kontrola proběhne před prací, takže stop
  hodnota cyklus ukončí, místo aby se započítala.

```python
line = input()
while line != "quit":     # "quit" is the sentinel
    print("you said:", line)
    line = input()        # read the next, then re-check
```
