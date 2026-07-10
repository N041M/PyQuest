Uma **função** embala um trabalho debaixo de um nome para que possa ser executado a pedido,
tantas vezes quantas forem necessárias. **`def`** introduz uma: um cabeçalho `def nome():` e um
corpo indentado.

- **Chamá-la** — `nome()` — corre o corpo. Definir uma função não a executa;
  a chamada é que executa.
- **`return valor`** devolve um resultado a quem chamou e termina a função
  de imediato. A expressão da chamada `nome()` *passa a ser* esse valor.
- Uma função sem `return` (ou com um `return` isolado) devolve `None`.

```python
def greet():
    return "hello"

greet()        # 'hello'  -- the call evaluates to the returned value
```
