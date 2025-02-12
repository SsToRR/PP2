l = int(input("Left bound: "))
r = int(input("Right bound: "))

def squares(l, r):
    for i in range(l, r + 1):
        yield i ** 2

print(*squares(l, r), sep=', ')