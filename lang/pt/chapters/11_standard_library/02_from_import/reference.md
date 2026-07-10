A forma **`from module import name`** associa um nome específico de um módulo
*diretamente* ao teu ficheiro, por isso é chamado sem o prefixo do módulo. `from math
import gcd` torna `gcd` um nome simples; escreves `gcd(12, 18)`, não
`math.gcd(...)`.

- Vários nomes de uma vez: `from math import gcd, sqrt, pi`.
- Só importa o que nomeares — `math.floor` **não** está disponível a menos que
  também importes `floor`. (`import math` traz tudo mas mantém o prefixo; as
  duas formas trocam conveniência por clareza no espaço de nomes.)
- O módulo inteiro continua a executar-se e a ficar em cache; só escolheste
  quais dos seus nomes aterram no teu espaço de nomes. Como o nome chega nu,
  pode **ofuscar** um teu — `from math import e` esconderia uma variável
  chamada `e`.

```python
from math import gcd, sqrt

gcd(12, 18)    # 6
sqrt(16)       # 4.0
```
