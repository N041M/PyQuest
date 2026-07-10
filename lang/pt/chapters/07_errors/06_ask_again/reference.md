O **ciclo de repetição** continua a perguntar até obter um valor válido.
Combina um `while True` com `try` / `except`: se tiver sucesso, faz `break`
para sair; se falhar, volta ao ciclo para perguntar outra vez.

- O `try` tenta a conversão/operação; um caminho bem-sucedido termina com
  `break`, saindo do ciclo.
- O `except` trata da entrada inválida (muitas vezes só imprimindo uma dica
  e continuando), para que o `while True` faça mais uma passagem.
- Um `while True` sem outra saída depende desse `break` — o caso válido é a
  única forma de sair.

```python
while True:
    try:
        n = int(input("number: "))
        break                 # valid -> leave the loop
    except ValueError:
        print("not a number, try again")
```
