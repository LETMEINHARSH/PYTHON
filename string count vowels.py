# WAP to accept string and count number of vowels.

s=input("Enter any string:")
s1="aeiouAEIOU"
count=0
for i in s:
    if i in s1:
        count=count+1
print("Number of vowels:",count)