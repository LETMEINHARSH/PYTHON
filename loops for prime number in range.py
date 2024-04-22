# WAP to Print all prime number in range.

a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
if a>=1 and b>a:
    print("Prime number in given range are:",end='')
    for i in range (a,b):
        if i>1:
            for j in range (2,i):
             if (i%j)==0:
              break
            else:
             print(i,end=',')
else:
    print("Enter a valid number.")