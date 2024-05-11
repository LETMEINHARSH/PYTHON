# WAP to find the first non-repeating character in a given string.

str=input("Enter any string:")
for i in str:
    count=0
    for j in str:
        if i==j:
            count+=1
    if count==1:
        print("First non repeating character is:",i)
        break