def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    
    print(f"Uppercase Letters: {upper_count}")
    print(f"Lowercase Letters: {lower_count}")

text = input()
count_case(text)
