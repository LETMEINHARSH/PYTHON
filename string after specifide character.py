# Write a Python program to get the last part of a string after a specified character.
# Sample Input:
# String=Extravagant
# Character=a
# Output:Vagant

str=input("Enter a string:")
char=input("Enter a specified character:")
print(str[str.index(char)+1:].capitalize())