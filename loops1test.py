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