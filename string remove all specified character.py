# WAP to delete all occurrences of a specified character in a given string.
# input:
# Delete all occurrences of a specified character in a given string.
# Character to be removed: 'a'
# output:
# Delete ll occurrences of  specified chrcter in  given string.

str=input("Enter a string:")
char=input("Character to be removed:")
for i in str:
    if i!=char:
        print(i,end='')