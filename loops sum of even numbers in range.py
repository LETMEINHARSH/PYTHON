# Develop a program that calculates the sum of all even numbers in a given range.

a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
sum=0
if a%2==0:
    a=a+1
for i in range (a,b,1):
    if   i%2==0:
        sum=sum+i
print("sum of even number in given range is:",sum)