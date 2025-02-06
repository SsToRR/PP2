import math
import random
"""
def convert_to_gram(ounces):
    return ounces * 28.3495231

ounces = int(input())
print(convert_to_gram(ounces))
"""
"""
def far_to_cel(temp):
    return (5/9) * (temp - 32)

temperature = int(input())
print(far_to_cel(temperature))
"""
"""
heads = int(input("How many heads are there?: "))
legs = int(input("How many legs are there?: "))

def solve(numheads, numlegs):
    rabbit = (numlegs - 2*numheads) / 2
    chicken = numheads - rabbit
    return (int(rabbit), int(chicken))

print(solve(heads, legs))
"""
"""
numbers_array = list(map(int, input().split()))

def filter_prime(nums):
    result = []
    for i in nums:
        if i == 1 or i == 0:
            continue
        ok = 1
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                ok = 0
                break
        if ok == 1:
            result.append(i)
    return result

print(filter_prime(numbers_array))
"""
"""
def next_permutation(s, ans, results):
    if len(s) == 0:
        results.append(ans)
        return
    for i in range(len(s)):
        ch = s[i]
        L_substr = s[0 : i]
        R_substr = s[i + 1 : ]
        sum = L_substr + R_substr
        next_permutation(sum, ans + ch, results)

s = input()
results = []
next_permutation(s, "", results)
print(results) 
"""
"""
def reverse(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
"""
"""
nums = list(map(int, input().split()))

def has_33(array):
    for i in range (0, len(array) - 1):
        if(array[i] == array[i+1] and array[i] == 3):
            return True
    return False

print(has_33(nums))
"""
"""
nums = list(map(int, input().split()))

def has_007(array):
    for i in range (0, len(array) - 2):
        if(array[i] == 0 and array[i + 1] == 0 and array[i + 2] == 7):
            return True
    return False

print(has_007(nums))
"""
"""
r = int(input())

def volume(radius):
    return float((4/3) * math.pi * radius**3)

print(volume(r))
"""
"""
nums = list(map(int, input().split()))

def unique_elements(array):
    result = []
    mp = {}
    for i in range(0, len(array) - 1):
        if array[i] in mp: 
            continue
        else:
            mp[array[i]] = 1
            result.append(array[i])
    return result

print(unique_elements(nums))
"""
"""
s = input()

def is_palindrome(str):
    t = str[::-1]
    if(str == t):
        return True
    else:
        return False

print(is_palindrome(s))
"""
"""
histograms = list(map(int, input().split()))

def histogram(array):
    for i in range(0, len(array)):
        t = ""
        for j in range(array[i] + 1):
            t += '*'
        print(t)

histogram(histograms)
"""
"""
def guess_game():
    name = input("Hello bro! What is your name?")
    rand_num = random.randrange(1, 20)
    print("Well", name, "I am thinking of a number between 1 and 20")
    x = -1
    cnt = 0
    while(x != rand_num):
        cnt += 1
        x = int(input("Take a guess!"))
        if x < rand_num:
            print("Too low!")
        elif x > rand_num:
            print("Too high!")
        else:
            print("Good job", name, f"You guessed my number in {cnt} guesses!")

guess_game()
"""

