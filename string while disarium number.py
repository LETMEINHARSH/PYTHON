# WAP to take a number as input and check if it is disarium number.

n=int(input("Enter a number:"))
s1=str(n)
l=len(s1)
sum=0
while n:
    d=n%10
    sum=sum+(d**l)
    n=n//10
    l=l-1
if sum==int(s1):
    print("Given number is disarium")
else:
    print("Not Disarium.")