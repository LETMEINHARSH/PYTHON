# WAP to remove all spaces in a string.

str=input("Enter any string:")
s2=' '
print("String without spaces:",end='')
for i in str:
    for j in s2:
        if i!=j:
            print(i,end='')