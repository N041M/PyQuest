**Množina** je neuspořádaná kolekce **jedinečných** položek: `{1, 2, 3}`. Modeluje
„skupinu odlišných věcí“ a rychle testuje příslušnost.

- Sestavení množiny z posloupnosti **zahodí duplicity**: `set([1, 1, 2])` je
  `{1, 2}`. Prázdná množina je `set()` — `{}` je prázdný *slovník*.
- **`x in s`** testuje příslušnost a je mnohem rychlejší než procházení seznamu,
  protože množiny jsou založené na hashování.
- Množiny jsou neuspořádané (žádné indexování, žádné řezy) a drží jen neměnné
  položky. Přidávej pomocí `.add(x)`, odebírej pomocí `.discard(x)`.

```python
seen = set()
seen.add("a"); seen.add("a")   # {'a'} -- duplicate ignored
"a" in seen                    # True
set([3, 1, 3, 2])              # {1, 2, 3}
```
