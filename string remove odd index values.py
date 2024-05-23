# Write a Python program to remove characters that have odd index values in a string given by the user.

s1=(input("type a string:"))
s2=""
for i in range(len(s1)):
    if i%2==0:
       s2=s2+s1[i]
print(s2)