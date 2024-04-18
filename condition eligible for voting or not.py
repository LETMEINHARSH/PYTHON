# Write a program that takes the user's age as input and categorizes them
# as a child, teenager, adult, or senior. Additionally, check if the user is
# eligible to vote (age 18 and above).
age=int(input("Enter the age="))
if 0<=age<=12:
    print("User is a Child.")
elif 13<=age<=18:
    print("User is a Teenager.")
elif 18<=age<=60:
    print("User is a Adult.")
elif 60<=age:
    print("User is a Senior.")
if age>=18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")