Ve výchozím stavu `==` mezi objekty testuje **identitu** — zda jsou ten úplně
stejný objekt — takže dva nezávisle postavené objekty se stejnými daty se porovnají
jako nerovné. Definice **`__eq__(self, other)`** předefinuje `==` na **rovnost podle
hodnoty**.

- Python volá `a.__eq__(b)` k vyhodnocení `a == b`; vrať, zda se mají počítat jako
  rovné, obvykle porovnáním definujících atributů. `!=` následuje automaticky jako
  jeho negace.
- Rovnost podle hodnoty je to, co dělá objekty intuitivními v testech `==`, v
  příslušnosti k `list` (`in`) a při porovnávání výsledků.
- Pokud definuješ `__eq__`, třída se stane **nehashovatelnou** (její `__hash__` se
  nastaví na `None`), takže nemůže do `set` ani jako klíč `dict`, dokud nedefinuješ
  i `__hash__` — často `return hash(self.cents)`.

```python
class Money:
    def __init__(self, cents): self.cents = cents
    def __eq__(self, other): return self.cents == other.cents

Money(500) == Money(500)     # True
Money(500) == Money(750)     # False
```
