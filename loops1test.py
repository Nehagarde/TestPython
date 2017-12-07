# For Loops


fruitsandveggies = ['mango is a fruit','apple is fruit','potato is a vege']

for eachitem in fruitsandveggies:
    print(eachitem)

i=0
for eachitem in fruitsandveggies:
    if 'fruit' in eachitem:
        print(eachitem)
    i=i+1
    print(i)

for eachitem in fruitsandveggies:
    if 'vege' in eachitem:
        print(eachitem)

        
names=['neha','sabah','magi']
phones=['9538523675','7350667558','7340657598']		

for i,j in zip(names,phones):
	print(i,j)
