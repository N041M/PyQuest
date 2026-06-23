**Booleovské operátory** kombinují podmínky:

- **`and`** je pravdivé jen když jsou **obě** strany pravdivé.
- **`or`** je pravdivé když je pravdivá **alespoň jedna** strana.
- **`not`** obrátí jednu hodnotu.

Vyhodnocují se **zkráceně** (short-circuit): `and` se zastaví u prvního
nepravdivého operandu, `or` u prvního pravdivého, takže pravá strana se
nevyhodnotí, když už levá rozhodla. Priorita je `not` > `and` > `or`; závorky
udělají záměr jasným.

```python
0 < x and x < 100      # True only inside the range
done or out_of_time    # True if either holds
not finished           # flips the flag
```
