# 5.9 -- Počítání pomocí slovníku

## Koncept

*„Kolikrát se každá věc objeví?“* je jedna z nejužitečnějších otázek v
programování. Odpovědí je **sčítací vzor** (tally): slovník, kde každý klíč je věc,
kterou jsi viděl, a jeho hodnota je, kolikrát jsi ji viděl.

Celý trik je jeden řádek, postavený na `.get()` z 4.10:

```python
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
```

Čti ten řádek pomalu: *„počet pro `w` se stane tím, čím byl -- nebo 0, je-li `w`
nové -- plus jedna.“* `.get(w, 0)` je to, co rozběhne první spatření: ještě tam
není žádný záznam, takže se počítá od 0.

Po cyklu `counts.get(thing, 0)` odpoví na „kolik?“ pro cokoli -- včetně věcí nikdy
neviděných, které jsou `0`, ne pád.

## Příklad

```python
words = ["tea", "milk", "tea"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts.get("tea", 0))     # 2
print(counts.get("cocoa", 0))   # 0
```

## Tvůj úkol

Přečti jeden řádek slov (odděl je pomocí `.split()`, jako v 4.4), pak přečti
**dotazové slovo** na druhém řádku. Vypiš, kolikrát se dotaz na řádku vyskytuje.

Pro vstup `tea milk tea`, pak `tea`:

```
2
```

## Hotovo, když

- `tea milk tea` s dotazem `tea` vypíše `2`; dotaz `milk` vypíše `1`.
- Dotaz, který se nikdy neobjeví, vypíše `0` (žádný pád).
- Sestavil jsi sčítací slovník (ne jednorázové projití).
