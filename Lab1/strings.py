print("Hello")
print('Hello')


print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


a = "Hello"
print(a)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)


a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


txt = "The best things in life are free!"
print("expensive" not in txt)


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


b = "Hello, World!"
print(b[2:5])

print(b[:5])

print(b[2:])

print(b[-5:-2])


a = "Hello, World!"
print(a.upper())
print(a.lower())


print(a.strip()) # returns "Hello, World!"

print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


a = "Hello"
b = "World"
c = a + b
print(c)


a = "Hello"
b = "World"
c = a + " " + b
print(c)


age = 36
txt = f"My name is John, I am {age}"
print(txt)


price = 59
txt = f"The price is {price} dollars"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


txt = f"The price is {20 * 59} dollars"
print(txt)


txt = "We are the so-called \"Vikings\" from the north."

txt = 'It\'s alright.'
print(txt) 


print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "Hello\nWorld!"
print(txt) 

txt = "Hello\rWorld!"
print(txt) 

txt = "Hello\tWorld!"
print(txt) 


#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

a = "Hello, World! {}"

print(a.capitalize())
print(a.casefold())
print(a.center(20))
print(a.count("e"))
print(a.encode())
print(a.endswith("!"))
print(a.expandtabs(2))
print(a.find("e"))
print(a.format("John"))
print(a.index("e"))
print(a.isalnum())
print(a.isalpha())
print(a.isascii())
print(a.isdecimal())
print(a.isdigit())
print(a.isidentifier())
print(a.islower())
print(a.isnumeric())
print(a.isprintable())
print(a.isspace())
print(a.istitle())
print(a.isupper())
print(a.join("John"))
print(a.ljust(20))
print(a.lower())
print(a.lstrip())
print(a.maketrans("H", "J"))
print(a.partition("e"))
print(a.replace("e", "a"))
print(a.rfind("e"))
print(a.rindex("e"))
print(a.rjust(20))
print(a.rpartition("e"))
print(a.rsplit())
print(a.rstrip())
print(a.split())
print(a.splitlines())
print(a.startswith("H"))
print(a.strip())
print(a.swapcase())
print(a.title())
print(a.translate("H"))
print(a.upper())
print(a.zfill(5))
