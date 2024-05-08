# WAP to take a string as input which contains both alphabet and numbers.
# print the sum of all the numbers and a segregated string.

str=input("Enter any string:")
s1='abcdefghijklmnopqrstuvwxyz'
num='0123456789'
sum=0
for i in s1:
    for j in str:
        if i==j:
            print(i,end='')
print()
for k in num:
    for l in str:
        if k==l:
            sum=sum+int(k)
print(sum)