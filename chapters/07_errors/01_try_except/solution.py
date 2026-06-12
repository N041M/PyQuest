line = input()
try:
    n = int(line)
    print(n * 2)
except ValueError:
    print("not a number")
