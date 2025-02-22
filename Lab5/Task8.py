import re

s = input('Input your string: ')

def space_between_big(s):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
    return result

print(space_between_big(s))