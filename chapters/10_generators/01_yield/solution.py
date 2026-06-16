def count_down(n):
    i = n
    while i >= 1:
        yield i
        i = i - 1
