# WAP to check whether the last digit of a number(entered by user) is divisible by 3 or not
a=int(input("Enter a number="))
c=a%10
if c%3==0:
    print("Last digit of the number is divisible by 3")
else:
    print("Last digit of number is not divisible by 3")