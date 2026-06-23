# 12.6 -- re.sub: najdi a nahraď podle vzoru

## Koncept

`str.replace` vymění pevný podřetězec. **`re.sub`** vymění vše, co odpovídá **vzoru**:

```python
import re

re.sub(r"\d+", "#", "call 555-1234 now")     # 'call #-# now'
```

- `re.sub(pattern, replacement, text)` vrátí **nový** řetězec s **každou** shodou
  `pattern` nahrazenou `replacement`.
- Protože `\d+` odpovídá celému úseku číslic, každý úsek se smrskne na jediné `#` --
  jedno nahrazení na shodu, ne na znak.
- Žádná shoda nechá text beze změny. Nahrazení může také odkazovat na zachycené
  skupiny (`\1`), ale prostý řetězec je běžný případ.

## Příklad

```python
import re

def squash_spaces(text):
    return re.sub(r"\s+", " ", text)
```

## Tvůj úkol

Pomocí **`re.sub`** definuj `redact(text)`, která nahradí každý úsek číslic v `text`
jediným `"#"`.

## Hotovo, když

- `redact("call 555-1234")` vrátí `"call #-#"`.
- `redact("no digits")` vrátí `"no digits"`.
- Každý *úsek* číslic se stane jedním `#` (použij `\d+`), přes `re.sub` -- ne cyklus
  přes znaky.
