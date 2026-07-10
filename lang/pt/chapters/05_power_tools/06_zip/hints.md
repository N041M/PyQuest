Lê primeiro TODOS os nomes para uma lista, depois todas as pontuações para outra --
só depois os emparelhas.

---

`for name, score in zip(names, scores):` dá um par por passagem; imprime os
dois com um espaço entre eles (`print(name, score)` simples já faz isso).

---

n = int(input())
names = []
for _ in range(n):
    names.append(input())
scores = []
for _ in range(n):
    scores.append(input())
for name, score in zip(names, scores):
    print(name, score)
