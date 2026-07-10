Uma instrução **`import`** carrega um **módulo** — um ficheiro de código pronto da
biblioteca padrão — e associa-o a um nome. `import math` torna o objeto do módulo
disponível como `math`, e o seu conteúdo é acedido através dele: `math.sqrt`,
`math.pi`, `math.floor`.

- A instrução executa-se **uma vez**, convencionalmente no **topo** do ficheiro; o
  nome passa então a referir-se a todo o módulo durante o resto do programa.
- **`module.name`** (acesso a atributo) procura uma função ou constante *no*
  módulo, o que mantém os nomes de cada módulo no seu próprio espaço de nomes —
  `math.pi` e o teu próprio `pi` nunca colidem.
- Importar um nome que não existe gera `ModuleNotFoundError`; o código do
  módulo executa-se na primeira vez que é importado e fica depois em cache.
- A biblioteca padrão vem com o Python ("pilhas incluídas"), por isso estes
  módulos não precisam de instalação — apenas do import.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
math.floor(2.7)  # 2
```
