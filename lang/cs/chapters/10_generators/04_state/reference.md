Generátor si **pamatuje** své lokální proměnné napříč `yield`y: běh zmrzne u
`yield` a každá lokální proměnná si drží svou hodnotu do dalšího požadavku, který
funkci obnoví. Díky tomu může generátor **nést stav**, jak proudí.

- Proměnná aktualizovaná v cyklu (průběžný součet, předchozí hodnota) přetrvává
  mezi yieldy bez jakéhokoli objektu nebo globální proměnné.
- To je to, co dělá generátor přirozeným **průběžným akumulátorem** — třeba
  průběžným součtem, který v každém kroku vydá dosavadní součet.

```python
def running_sum(nums):
    total = 0
    for n in nums:
        total += n          # total survives across yields
        yield total

list(running_sum([1, 2, 3]))    # [1, 3, 6]
```
