Program běží shora dolů, takže po sobě jdoucí příkazy `print` vytvoří po sobě
jdoucí řádky — každé volání vypíše své argumenty a pak nový řádek.

Předání **více hodnot jednomu `print`**, oddělených čárkami, je něco jiného než
více volání `print`: hodnoty se objeví na *jednom* řádku, spojené pomocí `sep` (ve
výchozím stavu mezerou). Jde o oddělení čárkami ve volání, ne o zřetězení řetězců
— hodnoty si ponechávají vlastní typy a převádějí se nezávisle.

```python
print("one")
print("two")          # two lines

print("x", "y", 3)    # one line:  x y 3
```
