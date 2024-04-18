# 10- Write a program that checks if a given number is divisible by both 3 and 5, or only by 3 or 5.

num=int(input("Enter a number:"))
if num%3==0 and num%5==0:
    print("Entered number is divisible by both 3 and 5.")
elif num%3==0:
    print("It is only divisible by 3.")
elif num%5==0:
    print("It is only divisible by 5.")
else:
    print("Entered number is not divisible by 3 and 5.")