# Given a pair of non-empty strings. Write a program to count the number of matching characters in
# those strings (consider the single count for the characters which have duplicates in the strings).
# Input : str1 = 'abcdef'
# str2 = 'defghia'
# Output : 4
# (i.e. matching characters :- a, d, e, f)

str1=input("Enter a string 1:")
str2=input("Enter a string 2:")
count=0
for i in str1:
    for j in str2:
        if i==j:
            count+=1
print(count)