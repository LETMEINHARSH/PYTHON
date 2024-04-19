# Write a Python program that prints the squares of all numbers in range.

a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
for i in range (a,b+1):
    c=i**2
    print("Square of",i,"is:",c)