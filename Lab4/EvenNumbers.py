n = int(input())

def even_numbers(n):
    even_nums = []
    for i in range(0, n + 1):
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums

nums = even_numbers(n)

print(*nums, sep=', ')