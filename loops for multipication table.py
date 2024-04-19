# WAP that asks the user to enter a positive integer and prints a multiplication table for that number upto 20.

a=int(input("Enter a number:"))
if a>0:
    for i in range (1,21,1):
     b=a*i
     print(a,"*",i,"=",b)
else:
    print("Enter a positive integer")