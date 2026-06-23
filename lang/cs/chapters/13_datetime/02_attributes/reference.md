**`date.fromisoformat(text)`** rozparsuje standardní řetězec `YYYY-MM-DD` na objekt
`date` — inverze k `.isoformat()`. Výsledek je skutečné datum, takže můžeš číst jeho
atributy, porovnat ho nebo s ním počítat.

- Očekává přesný ISO tvar; chybně utvořený nebo nemožný řetězec vyvolá `ValueError`,
  což jako vedlejší účinek validuje vstup.
- `.year`, `.month`, `.day` přečtou složky zpět jako celá čísla.
- Parsování na datum (místo abys řetězec sám řezal) je smyslem: hodnota je
  zkontrolovaná a ihned připravená pro kalendářní práci. Pro neISO rozvržení parsuje
  `datetime.strptime` podle explicitního formátu (13.7).

```python
from datetime import date

d = date.fromisoformat("2026-06-20")
(d.year, d.month, d.day)     # (2026, 6, 20)
d < date.fromisoformat("2026-12-31")   # True
```
