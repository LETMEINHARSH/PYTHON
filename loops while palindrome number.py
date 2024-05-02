# WAP to take a number as input and check if it is a palindrome number or not.

n=int(input("Enter a number:"))
b=n
sum=0
while n:
    d=n%10
    sum=(sum*10)+d
    n=n//10
if sum==b:
    print("Palindrome Number.")
else:
    print("Not a palindrome number.")