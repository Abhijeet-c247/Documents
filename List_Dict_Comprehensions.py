
# List Comprehensions

numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)  # [2, 4]

word = "Python"
letters = [char.upper() for char in word]
print(letters)  # ['P', 'Y', 'T', 'H', 'O', 'N']

#-----------------------------------------------------------------------------

# Dictionary Comprehensions

numbers = [1, 2, 3, 4]
squares_dict = {n: n**2 for n in numbers}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16}

numbers = [1, 2, 3, 4, 5]
even_square_dict = {n: n**2 for n in numbers if n % 2 == 0}
print(even_square_dict)  # {2: 4, 4: 16}

text = "apple"
letter_count = {char: text.count(char) for char in text}
print(letter_count)  # {'a': 1, 'p': 2, 'l': 1, 'e': 1}