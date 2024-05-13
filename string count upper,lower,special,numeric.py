# Write a program to count Uppercase, Lowercase, special characters and numeric values in a given string.

str=input("Enter any string:")
countupper,countlower,countspecial,countnumeric=0,0,0,0
for i in str:
    if i.isupper():
        countupper+=1
    elif i.islower():
        countlower+=1
    elif i.isnumeric():
        countnumeric+=1
    else:
        countspecial+=1
print("Uppercase character in string:",countupper)
print("Lowercase character in string:",countlower)
print("Special character in string:",countspecial)
print("Numeric Values in string:",countnumeric)