Funkce obsahující **`yield`** je **generátorová funkce**. Její zavolání tělo
nespustí — vrátí **objekt generátoru**, který vytváří hodnoty po jedné, **pozastaví
se** u každého `yield` a obnoví se tam, kde přestal, když je požádán o další.

- Každý `yield hodnota` podá jednu hodnotu tomu, kdo iteruje, pak zmrazí stav
  funkce do dalšího požadavku.
- Generátor konzumuješ jeho procházením (`for x in gen:`) nebo pomocí `next(gen)`.
- Liší se to od `return`, který vrátí **jednu** hodnotu a funkci natrvalo ukončí.

```python
def two():
    yield 1
    yield 2

for n in two():
    print(n)            # 1, then 2
```
