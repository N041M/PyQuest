n = int(input())
nums = [int(input()) for _ in range(n)]
doubled = [x * 2 for x in nums]
for d in doubled:
    print(d)
