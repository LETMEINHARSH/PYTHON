# Create a program that determines if a given year is a "century year" (ends in 00) and whether it's a leap year.

yr=int(input("Enter a Year:"))
if yr%100==0:
    print("It is a CENTURY year")
else:
    print("Its not a CENTURY year")
if yr%4==0 and yr%100!=0 or yr%400==0:
    print("Its a LEAP YEAR")
else:
    print("Its not a LEAP YEAR")