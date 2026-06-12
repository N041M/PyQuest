while True:
    try:
        n = int(input())
        break
    except ValueError:
        pass
print(n * 2)
