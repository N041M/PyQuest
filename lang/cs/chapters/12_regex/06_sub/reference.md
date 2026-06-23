**`re.sub(pattern, repl, text)`** je nahrazování řízené vzorem: vrátí **nový**
řetězec s **každou** nepřekrývající se shodou `pattern` nahrazenou `repl`. Kde
`str.replace` vymění pevný podřetězec, `re.sub` vymění cokoli, co vzor popisuje.

- Protože kvantifikovaný vzor odpovídá **úseku**, každý úsek se smrskne na jedno
  nahrazení: `re.sub(r"\d+", "#", "a12b3")` je `"a#b#"`, ne `"a##b#"`.
- Žádná shoda nechá text beze změny. Volitelné `count=` omezí, kolik nahrazení se
  provede.
- `repl` může odkazovat na zachycené skupiny pomocí `\1`, `\2`, … (např.
  `re.sub(r"(\w+)@(\w+)", r"\2.\1", s)`), nebo být **funkcí**, která dostane každou
  shodu a vrátí její nahrazení, pro logiku příliš složitou na šablonu.

```python
import re

re.sub(r"\s+", " ", "too   many    spaces")   # 'too many spaces'
re.sub(r"\d+", "#", "call 555-1234")           # 'call #-#'
re.sub(r"(\d+)", r"[\1]", "x12")               # 'x[12]'
```
