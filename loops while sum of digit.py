# WAP to find sum of digits of number accepted from the user.

n=int(input("Enter a number:"))
sum=0
if n>=0:
    while n>0:
        a=n%10
        sum=sum+a
        n=n//10
    print("Sum of all digit is:",sum)
else:
    print("Enter a positive interger.")