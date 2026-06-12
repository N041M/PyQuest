parts = input().split()
try:
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("unknown op")
except ValueError:
    print("bad number")
except ZeroDivisionError:
    print("cannot divide")
