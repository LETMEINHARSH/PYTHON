# WAP to check if sum of 2number is divisible by both 5 and 7.
a=int(input("Enter number1 ="))
b=int(input("Enter number2 ="))
c=a+b
if c%5==0 and c%7==0:
    print("SUM of given number is divisible by both 5 and 7")
else:
    print("Sum of given number is not divisible by both 5 and 7")