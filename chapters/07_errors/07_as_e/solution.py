line = input()
try:
    print(int(line))
except ValueError as e:
    print(e)
