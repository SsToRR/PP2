import time

number = int(input("Enter a number: "))
milliseconds = int(input("Enter milliseconds: "))
time.sleep(milliseconds / 1000)

print("Square root of", number,  "after", milliseconds, "milliseconds is", pow(number, 0.5))