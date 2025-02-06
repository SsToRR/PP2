from math import sqrt
"""
class string():
    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string, "Printing the string")

s1 = string()
s1.getString()
s1.printString()
"""

"""
class Shape:
    def __init__(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2
    
shape = Shape()
print(shape.area)

square = Square(10)
print(square.area())
"""
"""
class Shape:
    def __init__(self):
        pass

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

rectangle = Rectangle(1000, 1000)
print(rectangle.area())
"""
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, pos_x, pos_y):
        print(sqrt((self.x - pos_x)**2 + (self.y - pos_y)**2))

p = Point(3, 4)
p.show()
p.move(1, 10)
p.dist(1, 10)
"""
"""
class Account:
    pass

class owner:
    def __init__(self, name):
        self.name = name

class Balance:
    def __init__(self, total = 0):
        self.total = total

    def withdraw(self, amount):
        if self.total - amount < 0:
            print("No bro, you can't do that")
        else:
            self.total -= amount
            print(f"Balance after withdrawal: {self.total}")

    def deposit(self, amount):
        self.total += amount
        print(f"Balance after deposit: {self.total}")

    def balance(self):
        print(f"Your current balance: {self.total}")

Owner = owner("Miras")
Bal = Balance()
Bal.balance()
Bal.deposit(1000)
Bal.withdraw(900)
Bal.withdraw(120)
"""
"""
class Filter: 
    def __init__(self, num):
        self.num = num

    def is_prime(self, n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime(self):
        return list(filter(lambda x: self.is_prime(x), self.num))

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p_filter = Filter(num)
p_nums = p_filter.prime()
print(p_nums)
"""