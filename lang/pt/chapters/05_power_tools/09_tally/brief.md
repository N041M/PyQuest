# 5.9 -- Contar com um dicionário

## Conceito

*"Quantas vezes aparece cada coisa?"* é uma das perguntas mais úteis na programação.
A resposta é o **padrão de contagem**: um dicionário onde cada chave é uma
coisa que já viste e o seu valor é quantas vezes já a viste.

O truque todo é uma linha, construída sobre o `.get()` de 4.10:

```python
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
```

Lê a linha devagar: *"a contagem de `w` passa a ser o que era -- ou 0 se
`w` for novo -- mais um."* `.get(w, 0)` é o que faz a primeira aparição funcionar:
ainda não há entrada, por isso conta a partir de 0.

Depois do ciclo, `counts.get(coisa, 0)` responde "quantas vezes?" para qualquer coisa --
incluindo coisas nunca vistas, que dão `0`, e não um erro.

## Exemplo

```python
words = ["tea", "milk", "tea"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts.get("tea", 0))     # 2
print(counts.get("cocoa", 0))   # 0
```

## A tua tarefa

Lê uma linha de palavras (separa-as com `.split()`, como em 4.4), depois lê uma
**palavra de consulta** numa segunda linha. Imprime quantas vezes a consulta aparece na
linha.

Para a entrada `tea milk tea`, depois `tea`:

```
2
```

## Está feito quando

- `tea milk tea` com a consulta `tea` imprime `2`; a consulta `milk` imprime `1`.
- Uma consulta que nunca aparece imprime `0` (sem erro).
- Construíste uma contagem com dicionário (não uma verificação pontual).
