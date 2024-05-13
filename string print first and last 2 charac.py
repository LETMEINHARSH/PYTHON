# Write a program to get a string made of the first 2 and last 2 characters of a
# given string. If the string length is less than 2, return the empty string instead.
# Sample String : ‘helloworld”'
# Expected Result : 'held’'

str=input("Enter a string:")
if len(str)<2:
    print()
else:
    print(str[0:2]+str[-2:])