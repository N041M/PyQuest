Uma cláusula **`else`** dá ao `if` um segundo ramo: o seu bloco é executado exatamente quando
a condição do `if` é **falsa**. Juntos formam uma escolha de dois caminhos — executa-se sempre
um ramo ou o outro, nunca os dois.

- O `else` não tem condição; é o caso genérico para "o `if` foi falso".
- Tem de estar emparelhado com um `if` à mesma indentação, e o seu bloco é indentado
  da mesma forma.

```python
if n % 2 == 0:
    print("even")
else:
    print("odd")        # runs only when n % 2 == 0 is False
```
