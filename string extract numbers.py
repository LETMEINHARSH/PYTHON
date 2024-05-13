# Write a Python program to extract numbers from a given string.
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: 12 45


str=input("Enter a string:")
print("Numbers from the said string:",end='')
s1=str.split()
for i in s1:
    if i.isnumeric():
        print(i,end=' ')