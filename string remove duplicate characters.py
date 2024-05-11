# WAP to remove duplicate characters from a given string.

str=input("Enter any string:")
print("New String:",end='')
for i in str:
    c=0
    for j in str:
        if i==j:
            c+=1
    if c==1:
        print(i,end='')