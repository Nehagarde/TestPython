# While Loops
    
password=''
while password != 'pass@123':
    password = input("Enter Password to log in: ")
    if password == 'pass@123':
        print("Login Successful")
    else:
        print("Try Again")
        