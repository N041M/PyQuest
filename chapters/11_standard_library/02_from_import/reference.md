The **`from module import name`** form binds a specific name from a module
*directly* into your file, so it's called without the module prefix. `from math
import gcd` makes `gcd` a plain name; you write `gcd(12, 18)`, not
`math.gcd(...)`.

- Several names at once: `from math import gcd, sqrt, pi`.
- It imports only what you name — `math.floor` is **not** available unless you
  also import `floor`. (`import math` brings everything but keeps the prefix; the
  two forms trade convenience against namespace clarity.)
- The whole module still runs and is cached; you've just chosen which of its
  names land in your namespace. Because the name arrives bare, it can **shadow**
  one of your own — `from math import e` would hide a variable called `e`.

```python
from math import gcd, sqrt

gcd(12, 18)    # 6
sqrt(16)       # 4.0
```
