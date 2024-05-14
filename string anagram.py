# WAP to take two string as input and check if they are anagram.

str1=input("Enter a string 1:")
str2=input("Enter a string 2:")
str3=''
for i in str1:
    if i in str2 and (str1.count(i)==str2.count(i)):
        str3=str3+i
if str3==str1 and len(str1)==len(str2):
    print("Anagram")
else:
    print("Not Anagram")