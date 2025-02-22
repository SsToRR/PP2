import re

s = input('Input your string: ')

def snake_to_camel(s):
    words = s.split('_')
    c_words = words[0].capitalize() + ''.join(word.capitalize() for word in words[1:])
    return c_words    
    
print(snake_to_camel(s))