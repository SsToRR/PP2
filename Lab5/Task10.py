import re

s = input('Input your string: ')

def camel_to_snake(s):
    result = re.sub('([a-z])([A-Z])', r'\1_\2', s)
    return result
    
print(camel_to_snake(s))