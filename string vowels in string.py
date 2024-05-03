# WAP to take a string as input and print all the vowels present in the string.

s1=input("Enter any string:")
v="aeiouAEIOU"
for i in v:
    for j in s1:
        if i==j:
            print(i,end=' ')