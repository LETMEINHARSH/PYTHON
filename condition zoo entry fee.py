# Write a program that calculates the cost of admission to a zoo based on
# age. Admission is free for children under 3, $10 for children aged 3-12, $15
# for adults aged 13-59, and $12 for seniors aged 60 and above.

age=int(input("Enter your age:"))
if age<3:
    print("Entry if free")
elif 3<=age<=12:
    print("Entry fee is 10$ for children.")
elif 13<=age<=59:
    print("Entry fee is 15$ for adults.")
elif age>=60:
    print("Entry fee is 12$ for seniors.")