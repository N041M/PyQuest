Přiřazení pomocí `=` sváže **jméno** s hodnotou. Poté jméno na tuto hodnotu
*odkazuje* a použití jména kdekoli se vyhodnotí jako ona. Při čtení kódu `=`
znamená „stává se“, ne „rovná se“ (rovnost je `==`).

- Jména se nedeklarují a nemají pevný typ — první přiřazení jméno vytvoří a to pak
  ukazuje na libovolný objekt, který přiřadíš.
- Jméno musí začínat písmenem nebo podtržítkem a obsahovat písmena, číslice nebo
  podtržítka; rozlišuje velikost písmen (`total` a `Total` jsou různá).
- Nejprve se plně vyhodnotí pravá strana, pak se výsledek sváže se jménem nalevo.

```python
greeting = "Hello"
print(greeting)        # Hello  -- the name stands in for the value
```
