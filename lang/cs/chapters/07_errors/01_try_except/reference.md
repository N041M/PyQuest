Příkaz **`try` / `except`** spustí rizikový kód a chybu zachytí, pokud selže,
místo aby nechal program spadnout. Blok `try` drží kód, který může **vyvolat
chybu**; blok `except` se spustí jen tehdy, když k tomu dojde.

- Pokud blok `try` uspěje, `except` se zcela přeskočí.
- Pokud nějaký příkaz v `try` vyvolá chybu, **zbytek `try` se opustí** a řízení
  skočí na odpovídající `except`; program pak pokračuje níže.
- Nezachycená chyba rozvine celý program s tracebackem — `except` je způsob, jak
  zasáhnout.

```python
try:
    n = int(text)        # may raise ValueError
except ValueError:
    n = 0                # recover instead of crashing
```
