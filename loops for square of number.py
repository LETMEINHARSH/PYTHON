# Develop a Python program that calculates the square of each number from 1 to 10 and 
# stores the results in a list using a for loop

a=int(input("Enter number:"))
if a>1:
    for i in range (1,a+1):
    # print("Square of",i,"is:",i**2)
     print("Square of",end=' ')
     if 1<=i<=9:
        print("00",end='')
     elif 10<=i<=99:
        print("0",end='')
     print(i,"is:",end=' ')
     if 1<=i**2<=9:
        print("00",end='')
     elif 10<=i**2<=99:
        print("0",end='')
     print(i**2)
else:
    print("Enter a positive interger.")