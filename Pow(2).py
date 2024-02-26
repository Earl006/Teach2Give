# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.

num1=int(input("Enter the number: "))
if num1 <= 0:
    print("Invalid input")
elif num1 & (num1-1) == 0:
    print("True")
else:
    print("False")