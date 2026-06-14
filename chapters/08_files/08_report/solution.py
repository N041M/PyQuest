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
