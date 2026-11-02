#Swap two variables, first with a temp variable, then with tuple unpacking
a=int(input("Enter a number"))
print(f"you have entered {a}")
b=int (input("Enter second number"))
print(f"you have entered{b}")
temp =a
a=b
b=temp
print(f"The numbers are {a} and {b}")

a,b=b,a 
print(a,b)