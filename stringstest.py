# Strings

str1 = "Hello There!"
print(str1)

# String Replace
replc1=str1.replace('e','i') 
print(replc1)

replc2=str1.replace('e','i',1)
print(replc2)

# String Concatenation
print(replc1+replc2)

# String Indexing
print("Third character: "+str1[2])
print("Last character: "+str1[11])
print("Last character: "+str1[-1])
print("Last but one character: "+str1[-2])
print("Range 1: "+str1[0:2])
print("Range 2: "+str1[:5])
print("Range 2: "+str1[5:])
print("Range 4: "+str1[-6:-1])