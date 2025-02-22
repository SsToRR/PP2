import re

s = input('Input your string: ')

print(re.sub(r'[ ,.]', ':', s))