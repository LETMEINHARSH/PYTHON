# WAP to take number as input and find sum of all prime digit present in the number.

a=int(input("Enter a number:"))
sum=0
n=a
while a>0:
    n=a%10
    if n>1:
        for i in range (2,n):
            if n%i==0:
                break
        else:
            sum=sum+n
    a=a//10
print("Sum of all prime digit present in the number is:",sum)