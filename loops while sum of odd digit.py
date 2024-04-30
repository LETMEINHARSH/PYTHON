# WAP to take two number as input and check if sum of odd digits of both the number is same or not.

n1=int(input("Enter number1:"))
n2=int(input("Enter number2:"))
s1,s2=0,0
while n1>0:
    n3=n1%10
    if n3%2!=0:
        s1=s1+n3
    n1=n1//10
while n2>0:
    n4=n2%10
    if n4%2!=0:
        s2=s2+n4
    n2=n2//10
if s1==s2:
    print("Sum of odd digit in both number is same")
else:
    print("Sum of odd digit in both number is not same")