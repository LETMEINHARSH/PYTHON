# WAP to check if the given number is a armstrong number.

n=int(input("Enter a number:"))
num=n
dum=n
sum=0
count=0
while n>0:
    count=count+1
    n=n//10
while num>0:
    a=num%10
    num=num//10
    sum=sum+(a**count)
if dum==sum:
    print("Entered number is an armstrong number.")
else:
    print("Entered number is not an armstrong number.")