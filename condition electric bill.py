# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria:
# Unit Price
# First 100 units--no charge
# Next 100 units--Rs 5 per unit
# After 200 units--Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)
a=float(input("Enter number of unit="))
if 0<=a<=100:
    print("Total bill amount is Rs 0,no charges for first 100 units")
elif 100<a<=200:
    a=(a-100)
    print("Total bill amount is Rs",a*5)
elif a>200:
    a=(a-200)
    print("the total bill amount is Rs",500+(a*10))
else:
    print("Entered unit is INVALID")