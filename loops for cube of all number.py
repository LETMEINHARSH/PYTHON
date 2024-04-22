# WAP to Calculate the cube of all numbers from 1 to a given number.

a=int(input("Enter the end number:"))
if a>0:
    for i in range (1,a+1):
     cube=i*i*i
     print("Cube of",i,"is",cube)
else:
    print("Enter a positive integer.")