Person = ["Abhijeet" , 8.1 , 25 , "Indore"]

#Person[Strat Index:End Index]  , ending index is not included

print(Person[0])  # Accessing the first element

print(Person[1])  # Accessing the second element

print(Person[2])  # Accessing the third element

print(Person[3])  # Accessing the fourth element

print(Person[-1])  # Accessing the last element

print(Person[-2])  # Accessing the second last element

print(Person[0:2])  # Accessing the first two elements

print(Person[0:3])  # Accessing the first three elements

print(Person[:3]) # Accessing the first three elements (same as above)

print(Person[0:]) # Accessing all elements from the first

Person[0] = "Abhi"  # Changing the first element
print(Person)

print(len(Person))  # Length of the list


# Methods in List

Person.append("B.Tech") # Adding an element at the end
print(Person)

Person.insert(1, "M.Tech")  # Inserting an element at index 1
print(Person)

Person.remove("Indore")  # Removing an element
print(Person)

Person.pop()  # Removing the last element
print(Person)

Person.sort()  # Sorting the list
print(Person)

Person.sort(reverse=True)  # Sorting the list in reverse order
print(Person)

Person.reverse()  # Reversing the list
print(Person)

Person.clear()  # Clearing the list
print(Person)



#-------------------------------------------------------------------------------------
# Tuple Example

Person_Tuple = ("Abhijeet", 8.1, 25, "Indore")

print(Person_Tuple[0])  # Accessing the first element of the tuple
print(Person_Tuple[1])  # Accessing the second element of the tuple
print(Person_Tuple[2])  # Accessing the third element of the tuple
print(Person_Tuple[3])  # Accessing the fourth element of the tuple

print(Person_Tuple[-1])  # Accessing the last element of the tuple
print(Person_Tuple[-2])  # Accessing the second last element of the tuple  
     
print(Person_Tuple[0:2])  # Accessing the first two elements of the tuple
print(Person_Tuple[0:3])  # Accessing the first three elements of the tuple

print(Person_Tuple[:3])  # Accessing the first three elements of the tuple
print(Person_Tuple[0:])  # Accessing all elements from the first of the


