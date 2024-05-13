# Write a program to find the first repeated character in a given string where the
# index of the first occurrence is smallest.

str=input("Enter a string:")
s1=''
for i in str:
    if i in s1:
        print("First repeated character is:",i)
        break
    s1=s1+i