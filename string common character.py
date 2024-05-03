# WAP to take two string as input and count

s1=input("Enter string 1:")
s2=input("Enter string 2:")
count=0
for i in s1:
    for j in s2:
        if i==j:
            count=count+1
print(count)