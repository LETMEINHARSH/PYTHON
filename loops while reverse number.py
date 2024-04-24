# WAP to reverse a given integer.

n=int(input("Enter a number:"))
rn=0
while n>0:
    a=n%10
    rn=(rn*10)+a
    n=n//10
print("Reversed number is:",rn)