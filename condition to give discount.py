# Implement a Python program to calculate the total cost based on the quantity of items purchased, considering a discount of 10% if the total cost exceeds $1000.

a=int(input("Enter number of units purchased:"))
b=int(input("Cost of per unit (in $):$"))
tc=a*b
if tc>1000:
    print("Amount to be paid after 10% discount: $",tc-(tc*0.1))
else:
    print("Amount to be paid: $",tc)