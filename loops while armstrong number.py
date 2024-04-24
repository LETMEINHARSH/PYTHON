# WAP to check if the given number is a armstrong number.

n=int(input("Enter a number:"))
num=n
sum=0
while n>0:
    a=n%10
    n=n//10
    sum=sum+(a*a*a)
if num==sum:
    print("Entered number is an armstrong number.")
else:
    print("Entered number is not an armstrong number.")