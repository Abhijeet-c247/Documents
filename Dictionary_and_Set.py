info = { "name": "Abhijeet",
        "age": 25, 
        "city": "Indore" }


print(info.keys() ) # Returns  all the keys in the dictionary

print(info.values())  # Returns all the values in the dictionary

print(info.items() ) # Returns all the key-value pairs in the dictionary

info.update({"country": "India"})  # Adds a new key-value pair to the dictionary
print(info)


#----------------------------------------------------------------------------------
# Creating a set

my_set = {1, 2, 3, 4, 5}  # A set of integers
print(my_set)

# Adding elements to a set
my_set.add(6)  # Adds a single element
print(my_set)

# Adding multiple elements to a set
my_set.update([7, 8, 9])  # Adds multiple elements from an iterable
print(my_set)

# Removing elements from a set
my_set.remove(1)  # Removes a specific element; raises KeyError if not found
print(my_set)

# Discarding elements from a set
my_set.discard(2)  # Removes a specific element; does not raise an error
print(my_set)

# Checking membership in a set
print(3 in my_set)  # Returns True if 3 is in the set, False otherwise
print(10 in my_set)  # Returns False since 10 is not in the set 

