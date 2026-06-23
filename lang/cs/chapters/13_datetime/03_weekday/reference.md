**`date.weekday()`** vrátí den v týdnu jako celé číslo, **pondělí = 0** až
**neděle = 6**. Protože `date` kóduje skutečný kalendář — přestupné roky, různé délky
měsíců — spočítá to správně pro libovolné datum, což je přesně ten druh práce, který
deleguješ na knihovnu, místo abys ho odvozoval ručně.

- `.isoweekday()` je totéž, ale **pondělí = 1 .. neděle = 7** (ISO konvence).
- Časté použití je `weekday() >= 5` k testu na víkend.
- Doprovodné `.strftime("%A")` naformátuje **jméno** dne v týdnu, ale to závisí na
  lokalizaci; číselné `.weekday()` je stabilní všude.

```python
from datetime import date

date(2026, 6, 20).weekday()      # 5  (Saturday)
date(2026, 6, 22).weekday()      # 0  (Monday)
date(2026, 6, 20).weekday() >= 5 # True -- it's the weekend
```
