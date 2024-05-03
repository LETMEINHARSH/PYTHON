# WAP to take string as input that contains both alphabet and numbers .
# calculate and print the sum of the digit present in the string.

s1=input("Enter any string:")
s2='0123456789'
sum=0
for i in s1:
    for j in s2:
        if i==j:
            sum=sum+int(j)
print(sum)