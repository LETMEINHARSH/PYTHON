# WAP to find product of digits of number entered by the user.

n=int(input("Enter a number:"))
product=1
if n>=0:
    if n==0:
        print("Product of entered number is: 0")
    else:
        while n>0:
            p=n%10
            product=product*p
            n=n//10
        print("Product of entered number is:",product)
else:
    print("Invalid Input")