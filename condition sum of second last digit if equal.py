# WAP to take two number as input and check if theeir second last digit matches,
# then print the sum of those digit.

a=int(input("Enter the first number:"))
b=int(input("Enter the second number"))
if a>=10 and b>=10:
    a=a%100
    a=a//10
    b=b%100
    b=b//10
    if a==b:
        print("Sum of second last digit is:",a+b)
    else:
        print("Second last digit from both entered number is not equal.")
else:
    print("Entered number is not valid")