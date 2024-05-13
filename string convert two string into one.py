# Write a Python program to generate two strings from a given string. For the first string, 
# use the characters that occur only once, and for the second, use the
# characters that occur multiple times in the said string.

str1=input("Enter any string:")
str2=''
str3=''
for i in str1:
    count=0
    for j in range (str1.index(i)+1,len(str1)):
        if i==str1[j]:
            count+=1
    if count<1:
        str2=str2+i
    if count>=1:
        str3=str3+i
print("Characters that occur only once:",str2)
print("characters that occur multiple times:",str3)