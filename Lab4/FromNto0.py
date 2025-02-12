n = int(input())

def nums(n):
    for i in range(n, 0, -1):
        yield i

print(*nums(n))