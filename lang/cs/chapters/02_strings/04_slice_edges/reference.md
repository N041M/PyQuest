Meze řezu mohou být **záporné**, počítané od konce, a oba styly se volně
kombinují. `s[1:-1]` zahodí první a poslední znak — začni na indexu 1, skonči
těsně před posledním.

- Řez, jehož start je roven stopu nebo za ním, je **prázdný**, ne chyba: `s[3:3]`
  i `s[5:2]` dají `""`.
- Meze mimo rozsah se oříznou, takže řez je shovívavý tam, kde obyčejné
  indexování vyvolá chybu: `s[1:99]` je v pořádku.
- Protože stop je vyloučen, `s[:-1]` odstraní přesně poslední znak a `s[1:]`
  odstraní první.

```python
s = "Python"
s[1:-1]   # 'ytho'  -- both ends trimmed
s[2:2]    # ''      -- empty, not an error
```
