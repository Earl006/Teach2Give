num1=int(input("Enter the number: "))
if num1 <= 0:
    print("Invalid input")
elif num1 & (num1-1) == 0:
    print("True")
else:
    print("False")