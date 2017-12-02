# Lists
    
l1 = ["N",2.3,5,"Hello"]

# to check type of the variable
print(type(l1))

# extract elements of list
print(l1[1])
print(type(l1[2]))
print(l1[2:])
print(type(l1[2:]))
print(l1[1:3])

# methods
print(dir(l1))

# append new element
l1.append(25)
l1.reverse()
print(l1)
print("Length of List is %d" %len(l1))
help(l1.remove)
