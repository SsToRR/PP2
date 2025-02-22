import re

s = input('Input your string: ')

check = re.compile('[A-Z][a-z]+')

n = check.search(s)

if n:
    print("Found: ", n.group())

else:
    print('No match')