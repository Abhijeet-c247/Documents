list = [1,2,3,4,5,6,7,8,9,10]
even = []
for i in list:
    if i % 2 == 0:
        even.append(i)
print(even)

# To avoid the for loop, we can use list comprehension

even = [i for i in list if i % 2 == 0]
print(even)


squares = [i*i for i in list]
print(squares)

odd = [i for i in list if i % 2 != 0]
print(odd)
