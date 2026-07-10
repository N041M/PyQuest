`input` lê **uma linha** da entrada padrão — tudo o que o utilizador escreve até
premir Enter — remove a quebra de linha final, e devolve-a como uma **cadeia de caracteres**.

- O valor devolvido é *sempre* um `str`, mesmo que o utilizador tenha escrito dígitos:
  `input()` sobre `42` devolve `"42"`, não `42`. Para fazer aritmética, converte-o
  (vê `int()`).
- O argumento opcional `prompt` é escrito no ecrã primeiro, sem uma
  quebra de linha final, para que o utilizador escreva na mesma linha.
- Se o fluxo de entrada terminar sem haver linha para ler (fim de ficheiro), `input` levanta
  `EOFError`.

```python
name = input("Your name? ")   # prompts, then reads a line
print("Hi, " + name)
```
