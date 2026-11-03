marks = int(input("Enter the marks: "))

if 90 <= marks <= 100:
    print("A")
elif 70 <= marks < 90:
    print("B")
elif 50 <= marks < 70:
    print("C")
elif 35 <= marks < 50:
    print("D")
elif 0 <= marks < 35:
    print("E and fail")
else:
    print("Invalid marks")