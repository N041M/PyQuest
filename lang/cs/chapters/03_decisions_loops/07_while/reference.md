Cyklus **`while`** opakuje svůj blok, **dokud** jeho podmínka zůstává pravdivá.
Podmínka se kontroluje **před** každým průchodem; jakmile se stane nepravdivou,
cyklus skončí a program pokračuje níže.

- Něco uvnitř cyklu musí nakonec podmínku zneplatnit (např. posun počítadla),
  jinak se točí navždy — nekonečný cyklus.
- Je-li podmínka nepravdivá hned při první kontrole, tělo se spustí nulakrát.
- Použij `while`, když dopředu neznáš počet průchodů (točíš se, dokud něco
  nenastane); použij `for`, když počítáš známý rozsah.

```python
n = 3
while n > 0:
    print(n)
    n = n - 1        # moves toward ending the loop -> 3, 2, 1
```
