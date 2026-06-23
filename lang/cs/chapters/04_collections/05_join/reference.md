**`sep.join(parts)`** slepí iterovatelný objekt **řetězců** do jednoho řetězce a
mezi sousední položky vloží `sep`. Oddělovač je řetězec, na kterém metodu voláš,
což zpočátku zní zvláštně, ale umožňuje, aby oddělovač byl libovolný řetězec.

- Každá položka už musí být řetězec; čísla vyvolají `TypeError`. Nejprve převeď,
  např. `", ".join(str(n) for n in nums)`.
- `"".join(parts)` zřetězí bez oddělovače — efektivní způsob, jak sestavit řetězec
  z mnoha kousků (mnohem lepší než opakované `+`).
- Je to inverze k `split`.

```python
"-".join(["2024", "01", "15"])   # '2024-01-15'
" ".join(["the", "fox"])          # 'the fox'
```
