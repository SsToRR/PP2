n = int(input())

def generate_squares(n):
    squares = []
    for i in range(n + 1):
        squares.append(i**2)
    return squares

#youtube.com/watch?v=Qfm6nfz1QNQ

print(generate_squares(n))