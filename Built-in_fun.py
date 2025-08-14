list = [1, 2, 3, 4, 5,6,7,8,9,10 ]  # A list of integers

#len example
print(len(list))  # Output: 10, the number of elements in the list

#sum example
print(sum(list))  # Output: 55, the sum of all elements in the list

#map example
cube = set(map(lambda x: x**3, list)) # Using map to cube each element in the list
print(cube)  # Output: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#filter example
even = set(filter(lambda x: x % 2 == 0, list))  # Using filter to get even numbers

#reduce example
from functools import reduce
sum = reduce(lambda x, y: x + y, list)  # Using reduce to sum all elements in the list
print(sum)  

#zip example
names = ["Abhijeet", "chiku", "banty"]
ages = [25, 30, 35]
combined = zip(names, ages)
print(set(combined))  

#enumrate example
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)