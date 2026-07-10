Um bloco `if` pode conter, ele próprio, outro `if` — **aninhamento**. O teste interior
só é executado **quando** a condição exterior é verdadeira, pelo que o aninhamento
exprime "isto, e depois, dentro disso, aquilo".

- Cada nível acrescenta um passo de indentação; o bloco interior é indentado sob o
  `if` interior.
- O aninhamento e o `and` podem exprimir a mesma coisa — `if a: if b:` é como
  `if a and b:` — mas o aninhamento é a ferramenta certa quando o caso exterior precisa
  do seu próprio tratamento (por exemplo, um `else`) separado do interior.
- Mantém o aninhamento pouco profundo; pirâmides profundas são difíceis de ler, e uma
  cadeia de `elif` ou um `return` antecipado costumam ler-se melhor.

```python
if logged_in:
    if is_admin:
        show_admin_panel()   # only when logged_in AND is_admin
    else:
        show_user_panel()    # logged_in but not admin
```
