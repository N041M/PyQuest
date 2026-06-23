Vzor **akumulátoru** buduje výsledek napříč cyklem. Proměnnou inicializuješ
**před** cyklem, pak ji aktualizuješ při **každém** průchodu; po cyklu drží
zkombinovaný výsledek.

- U součtu začni total na `0` a přičítej každou hodnotu (`total = total + x`, nebo
  `total += x`). Začátek na `0` je neutrální prvek pro `+`, takže prázdný cyklus ho
  nechá `0`.
- Stejný tvar počítá (začni na 0, `+= 1` za shodu), staví řetězec (začni `""`,
  `+=`) nebo sbírá seznam (začni `[]`, `.append`).
- Akumulátor musí žít **mimo** cyklus — deklarovat ho uvnitř by ho resetovalo při
  každém průchodu.

```python
total = 0
for n in [3, 1, 4]:
    total += n            # 3, then 4, then 8
print(total)             # 8
```
