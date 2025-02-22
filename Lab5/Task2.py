import re

s = input('Input your string: ')

check = re.compile('ab{2, 3}')

n = check.search(s)

if n:
    print("Found: ", n.group())

else:
    print('No match')