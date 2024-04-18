# a school has following rules for grading system:
# below 25--F
# 25 to 45--E
# 45 to 50--D
# 50 to 60--C
# 60 to 80--B
# above 80--A
# ask user to enter marks and print the corresponding grade.

marks=int(input("Enter your marks:"))
if marks<25:
    print("Your grade is F")
elif 25<=marks<45:
    print("Your grade is E")
elif 45<=marks<50:
    print("Your grade is D")
elif 50<=marks<60:
    print("Your grade is C")
elif 60<=marks<80:
    print("Your grade is B")
elif marks>=80:
    print("Your grade is A")