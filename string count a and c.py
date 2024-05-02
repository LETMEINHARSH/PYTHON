# WAP to accept a string from the user and count the frequency of alphabet 'a' and 'c'.

s=input("Enter any string:")
a,c=0,0
for i in s:
    if i=='a':
        a=a+1
    if i=='c':
        c=c+1
print("Number of alphabet 'a' is:",a)
print("Number of alphabet 'c' is:",c)