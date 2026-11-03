#. Given three side lengths, check whether they can form a triangle.
a=int(input("Enter the first side"))
b=int(input ("Enter the second side "))
c=int(input("Enter the third side"))

if (a+b>c and b+c>a and c+a>b):
    print("It can form a triangle")
else:
    print("It cannot form a triangle")
    