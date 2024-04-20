# WAP to take two number as input and print the sum of even and odd number between them,including the entered number.

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
sum=0
num=0
for i in range (a,b+1):
    if i%2==0:
        sum=sum+i
    else:
        num=num+i
print("Sum of all even number in range:",sum)
print("Sum of all odd number in range:",num)