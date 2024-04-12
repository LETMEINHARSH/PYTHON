# 01-WAP to check whether a person is eligible for voting or not.
# a=int(input("Enter the age="))
# if a>=21:
#     print("You are eligible for voting")
# else:
#     print("You are not eligible for voting")

# 02- WAP to check whether a number entered by user is even or odd.
# a=int(input("Enter a number="))
# if a%2==0:
#     print("Number is even")
# else:
#     print("Number is odd")

# 03- WAP to check whether a number is divisible by 7 or not.
# a=int(input("Enter a number="))
# if a%7==0:
#     print("The entered number is divisible by 7")
# else:
#     print("The entered number is not divisible by 7")

# 04- WAP to display "Hello" if a number entered by user is divisible by five,otherwise print "Bye"
# a=int(input("Enter a number="))
# if a%5==0:
#     print("HELLO")
# else:
#     print("BYE")

# 05- Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria:
# Unit Price
# First 100 units--no charge
# Next 100 units--Rs 5 per unit
# After 200 units--Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)
# a=float(input("Enter number of unit="))
# if 0<=a<=100:
#     print("Total bill amount is Rs 0,no charges for first 100 units")
# elif 100<a<=200:
#     a=(a-100)
#     print("Total bill amount is Rs",a*5)
# elif a>200:
#     a=(a-200)
#     print("the total bill amount is Rs",500+(a*10))
# else:
#     print("Entered unit is INVALID")

# 06- WAP to check whether the last digit of a number(entered by user) is divisible by 3 or not
# a=int(input("Enter a number="))
# c=a%10
# if c%3==0:
#     print("Last digit of the number is divisible by 3")
# else:
#     print("Last digit of number is not divisible by 3")

# 07- WAP to accept percentage from the user and display the grade according to the following criteria:
#  marks            grade
#   >90               A
#  >80and <=90        B
# >=60 and <=80       C
#  below 60           D
# a=float(input("Enter the percentage obtained="))
# if a>90:
#     print("Grade A")
# elif a>80 and a<=90:
#     print("Grade B")
# elif a>=60 and a<=80:
#     print("Grade C")
# elif a<60:
#     print("Grade D")

# 08- WAP to accept the cost price of the bike and display the road tax to be paid according to the following criteria:
#  Cost price (in Rs)        Tax
#    >100000                 15%
#  >50000and <=100000        10%
#   <=50000                   5%
# a=float(input("Enter the cost price of the bike="))
# if a>100000:
#     a=a*0.15
#     print("Road Tax to be paid is Rs",a)
# elif a>50000 and a<=100000:
#     a=a*0.1
#     print("Road Tax to be paid is Rs",a)
# elif a<=50000:
#     a=a*0.05
#     print("Road Tax to be paid is Rs",a)

# 009- Write a Python program to check if a given number is positive, negative, or zero
# a=int(input("Enter a number="))
# if a==0:
#     print("Given number is ZERO")
# elif a<0:
#     print("Given number is negative")
# elif a>0:
#     print("Given number is positive")

# 010- Create a Python program to determine whether a given year is a leap year or not. A leap year is divisible by 4, except for years that are divisible by 100 but not by 400.
# a=int(input("Enter a year ="))
# if a%4==0 and a%100

# 011- WAP to take input of lenght and breadth from the user to check and print if the dimension are of a square or a rectangle
# a=float(input("Enter the LENGHT ="))
# b=float(input("Enter the BREADTH ="))
# if a==b:
#     print("Dimensions are of a SQUARE")
# else:
#     print("Dimensions are of a RECTANGLE")

# 012- WAP to check if sum of 2number is divisible by both 5 and 7.
# a=int(input("Enter number1 ="))
# b=int(input("Enter number2 ="))
# c=a+b
# if c%5==0 and c%7==0:
#     print("SUM of given number is divisible by both 5 and 7")
# else:
#     print("Sum of given number is not divisible by both 5 and 7")

# 013- WAP to check and print if the number is a three digit number or not.
# a=int(input("Enter a number ="))
# if 100<=a<=999:
#     print(a,"is a three digit number.")
# else:
#     print(a,"is not a three digit number")

