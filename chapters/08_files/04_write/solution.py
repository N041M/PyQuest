with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
