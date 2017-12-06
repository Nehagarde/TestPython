# Conditionals  Part 2

def string_length(my_string):
    if type(my_string) == int:
        return "Length of Integer Cannot be found"
    elif type(my_string) == float:
        return "Length of Float Cannot be found"
    else:
        return len(my_string)



print(string_length(10))
print(string_length(10.5345))
print(string_length("Hello World"))


def cel_to_fahr(c):
    if c<-273.15:
        return "The Lowest possible Temperature cannot be less than -273.15"
    f = c * 9/5 + 32
    return f
    
    
print(cel_to_fahr(-273.15))
print(cel_to_fahr(-274.15))
