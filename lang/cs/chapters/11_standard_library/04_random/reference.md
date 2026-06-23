Modul **`random`** generuje pseudonáhodné hodnoty z vnitřního stavu:
`random.randint(a, b)` (celé číslo v `[a, b]`), `random.choice(seq)` (náhodná
položka), `random.shuffle(lst)` (přeuspořádá seznam **na místě**), `random.random()`
(float v `[0, 1)`).

- Čísla jsou deterministické funkce stavu, takže **`random.seed(n)`** je dělá
  **opakovatelnými**: po stejném semínku stejná volání dají stejné výsledky při
  každém spuštění a na každém stroji. Semínkuj jednou, před losy, které chceš
  reprodukovat.
- `random.shuffle` mutuje svůj argument a vrací `None` — zamíchej **kopii**
  (`out = list(items)`), abys zachoval originál, a nikdy nepiš
  `return random.shuffle(...)`.
- Výchozí (nesemínkovaný) generátor je semínkován z OS, takže bez semínka se každé
  spuštění liší. `random` **není** pro kryptografii — pro tokeny a hesla použij
  modul `secrets`.

```python
import random

random.seed(42)
random.randint(1, 6)     # same value every run for seed 42
deck = [1, 2, 3, 4]
random.shuffle(deck)     # deck reordered in place
```
