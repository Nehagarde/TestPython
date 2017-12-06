# Functions

def funchelloworld():
    print("Helloo World");

def funcaddtwointegers(a,b):
    return a+b;

def functwofloats(a,b):
    return a+b;

funchelloworld();
print(funcaddtwointegers(5,5));

def funcwithdefaultargs(a=5,b=6):
    return a+b;

print(funcwithdefaultargs());
print(funcwithdefaultargs(8));

a=int(input("Enter first variable: "));
b=int(input("Enter Second Variable: "));

print(funcwithdefaultargs(a,b));



