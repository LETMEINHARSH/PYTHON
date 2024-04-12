# Create a Python program to determine whether a given year is a leap year or not. A leap year is divisible by 4, except for years that are divisible by 100 but not by 400.
a=int(input("Enter a year ="))
if a%4==0 and a%100!=0 or a%400==0:
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")