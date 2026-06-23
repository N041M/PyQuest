`return` se může objevit **kdekoli** ve funkci a jeho dosažení volání ihned ukončí
— pozdější řádky se neprovedou. **Časný return** toho využívá k ošetření případu a
okamžitému odchodu.

- Zplošťuje kód: ošetři speciální nebo neplatný případ na začátku stráží
  (`if bad: return ...`), pak napiš hlavní cestu bez jejího vnoření do `else`.
- Vítězí první dosažený `return`; nic za ním se v tom volání neprovede.

```python
def reciprocal(n):
    if n == 0:
        return None     # bail out early on the bad case
    return 1 / n        # main path, not indented under an else
```
