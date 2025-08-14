text = "Python Programming"
print(text.upper())      # 'PYTHON PROGRAMMING'
print(text.lower())      # 'python programming'
print(text.title())      # 'Python Programming'
print(text.capitalize()) # 'Python programming'


text = "   Hello World!   "
print(text.strip())   # 'Hello World!' (removes both sides spaces)
print(text.lstrip())  # 'Hello World!   ' (removes left spaces)
print(text.rstrip())  # '   Hello World!' (removes right spaces)


text = "I like Java"
print(text.replace("Java", "Python"))  # 'I like Python'
print(text.find("like"))               # 2 (index position)
print(text.find("C++"))                 # -1 (not found)


text = "apple,banana,cherry"
fruits = text.split(",")         # ['apple', 'banana', 'cherry']
print(fruits)

joined = "-".join(fruits)
print(joined)                    # 'apple-banana-cherry'


text = "Python123"
print(text.isalpha())   # False (contains numbers)
print(text.isdigit())   # False (contains letters)
print("12345".isdigit())# True
print(text.isalnum())   # True if only letters & numbers


text = "Python"

print(text[0:4])     # 'Pyth' (index 0 to 3)
print(text[:4])      # 'Pyth' (start default)
print(text[2:])      # 'thon' (end default)
print(text[-3:])     # 'hon' (negative index counts from end)
print(text[::-1])    # 'nohtyP' (reverse string)
print(text[::2])     # 'Pto' (every 2nd letter)