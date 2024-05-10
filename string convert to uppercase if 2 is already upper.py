# WAP to convert a given string to all uppercase if it contains at lest 2 uppercase character in first 
# 4 character.

str=input("Enter any string:")
count=0
for i in range (0,4):
    if str[i].isupper():
        count=count+1
if count>=2:
    print("String in upper case:",str.upper())
else:
    print(str)