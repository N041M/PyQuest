Přidání **`if`** do komprehenze ponechá jen položky, které projdou testem.
`[x for x in items if test]` posbírá každé `x`, pro které je `test` pravdivý, a
zbytek **přeskočí**.

- Klauzule `if` filtruje; úvodní výraz stále transformuje, takže se obojí
  kombinuje: `[n * n for n in nums if n % 2 == 0]` umocní jen sudá.
- Nahrazuje vzor cyklus-s-`if`-a-`append`.
- Neplést si s **podmíněným výrazem** v pozici hodnoty
  (`[a if cond else b for x in items]`), který vybírá u každé položky, místo aby
  filtroval.

```python
[n for n in range(10) if n % 2 == 0]   # [0, 2, 4, 6, 8]
[w for w in words if len(w) > 3]       # only long words
```
