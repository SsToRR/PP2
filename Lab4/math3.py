import math

n = int(input("Number of sides: "))
s = float(input("Length of a side: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(round(area, 3))
