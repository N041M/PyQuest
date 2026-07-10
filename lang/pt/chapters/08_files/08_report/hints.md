Lê as linhas, e para cada uma `name, score = line.split()`; converte a
pontuação com `int()`. Reúne os pares numa lista.

---

Ordena com `key=lambda p: (-p[1], p[0])` para a pontuação mais alta primeiro,
empates por ordem alfabética. Escreve cada `f"{name} - {score}\n"`, e depois
um `f"Total: {sum_of_scores}\n"` final.

---

with open("scores.txt") as f:
    lines = f.read().splitlines()
players = []
for line in lines:
    name, score = line.split()
    players.append((name, int(score)))
players.sort(key=lambda p: (-p[1], p[0]))
total = sum(score for name, score in players)
with open("ranking.txt", "w") as f:
    for name, score in players:
        f.write(f"{name} - {score}\n")
    f.write(f"Total: {total}\n")
