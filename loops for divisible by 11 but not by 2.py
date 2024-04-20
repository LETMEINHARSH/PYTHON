# WAP to display all numbers which are divisible by 11 but not by 2 between range given by user.

a=int(input("Enter first number of range:"))
b=int(input("Enter second number of range:"))
if a>-1 and b>a:
    print("Number divisible by 11 but not by 2:",end=' ')
    for i in range (a-1,b):
        if i%11==0 and i%2!=0:
            print(i,end=',')
else:
    print("Enter a valid number.")