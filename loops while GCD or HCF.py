# WAP to find the greatest common divisor (GCD) or highest common factor (HCF) of two numbers.

a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
if a>b:
    num=a
else:
    num=b
for i in range (num,0,-1):
    if a%i==0 and b%i==0:
        print("HCF of",a,"and",b,"is:",i)
        break