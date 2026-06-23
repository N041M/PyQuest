**Knihovna** zde znamená sadu souvisejících funkcí, které jsi napsal, každá
pojmenovaná podle svého úkolu, jež dohromady tvoří znovupoužitelnou sadu nástrojů —
odměnu kapitoly.

- Stav malé funkce, z nichž každá dělá jednu věc a `return` svůj výsledek; pak je
  funkce vyšší úrovně volají. Volající kód se čte jako sled záměrů.
- Držet logiku uvnitř pojmenovaných funkcí (místo kopírování inline) znamená, že
  oprava nebo vylepšení dopadne na jedno místo a každý volající z toho těží.

```python
def clean(s):    return s.strip().lower()
def words(s):    return clean(s).split()
def wordcount(s): return len(words(s))

wordcount("  The quick fox ")   # 3  -- each function builds on the last
```
