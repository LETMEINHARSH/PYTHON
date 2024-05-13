# Write a program to find the common values that appear in two given strings.
# Sample Output:
# Original strings:
# Python3
# Python2.7
# Intersection of two said String:
# Python

str1=input("Enter any string 1:")
str2=input("Enter any string 2:")
for i in str1:
    for j in str2:
        if i==j:
            print(i,end='')