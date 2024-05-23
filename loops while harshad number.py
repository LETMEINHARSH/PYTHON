# WAP to take a number as input and check whether it is a Harshad number or not.
# A number is said to be the Harshad number if it is divisible by the sum of its digit.

n=int(input("Enter a number:"))
n1=n
sum=0
while n:
    d=n%10
    sum=sum+d
    n=n//10
if n1%sum==0:
    print("it is harshad number.")
else:
    print("it is not harshad number.")