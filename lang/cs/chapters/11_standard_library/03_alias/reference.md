**`import modul as alias`** naimportuje modul, ale naváže ho pod jménem dle tvé
volby. `import statistics as stats` zpřístupní modul jako `stats`; `stats.mean` *je*
`statistics.mean` — alias mění jen lokální jméno, ne modul.

- Použij ho ke **zkrácení** dlouhého jména modulu nebo k **vyhnutí se srážce** s
  jedním z tvých vlastních jmen. Konvencí dané aliasy, které potkáš (`import numpy
  as np`), jsou přesně tohle.
- Stejné `as` funguje na jediném jméně z from-importu: `from statistics import mean
  as avg`.
- Alias vidí jen tvůj soubor; ostatní moduly si pro něj drží vlastní jména.

```python
import statistics as stats

stats.mean([1, 2, 3, 4])     # 2.5
stats.median([1, 5, 2])      # 2
```
