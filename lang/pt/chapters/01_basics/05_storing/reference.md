A atribuição com `=` liga um **nome** a um valor. Depois disso o nome *refere-se a*
esse valor, e usar o nome em qualquer lado é equivalente a avaliá-lo. Ao ler código, `=` é
"passa a ser", não "é igual a" (a igualdade é `==`).

- Os nomes não são declarados e não têm um tipo fixo — a primeira atribuição cria
  o nome, e este passa simplesmente a apontar para o que quer que atribuas.
- Um nome tem de começar com uma letra ou sublinhado e conter letras, dígitos ou
  sublinhados; é sensível a maiúsculas/minúsculas (`total` e `Total` são diferentes).
- O lado direito é totalmente avaliado primeiro, e só depois o resultado é ligado ao
  nome do lado esquerdo.

```python
greeting = "Hello"
print(greeting)        # Hello  -- the name stands in for the value
```
