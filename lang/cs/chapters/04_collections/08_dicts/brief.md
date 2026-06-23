# 4.8 -- Slovníky

## Koncept

**Slovník** (`dict`) mapuje **klíče** na **hodnoty** -- vyhledávací tabulka. Zapíšeš
ho složenými závorkami a páry `klíč: hodnota`:

```python
ages = {"sam": 20, "ada": 36}
print(ages["sam"])     # 20      look up by key
ages["lee"] = 41       # add a new key
ages["sam"] = 21       # update an existing key
```

Věci vyhledáváš podle **klíče** (ne podle pozice), což dělá slovníky rychlými a
šikovnými pro „dané X, jaké je jeho Y?“. Začni z prázdna pomocí `{}` a naplň ho:

```python
d = {}
d["x"] = 1
```

## Příklad

```python
prices = {}
prices["apple"] = 3
print(prices["apple"])   # 3
```

## Tvůj úkol

Přečti počet `n`, pak `n` dvojic **slova** a **čísla** (slovo na jednom řádku,
číslo na dalším) do slovníku (slovo je klíč, číslo hodnota). Pak přečti ještě jedno
**dotazové slovo** a vypiš číslo uložené pro něj.

Pro vstup `2`, `apple`, `3`, `banana`, `5`, pak dotaz `banana`:

```
5
```

## Hotovo, když

- Sestavení `{apple: 3, banana: 5}` a dotaz `banana` vypíše `5`.
- Pozdější dvojice se stejným klíčem ho aktualizuje (test se spoléhá na poslední
  hodnotu pro každý opakovaný klíč).
