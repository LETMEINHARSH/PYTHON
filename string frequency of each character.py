# WAP to take a string as input and find the frequency of each character in the given string.

str=input("Enter any string:")
for i in str:
    count=0
    for j in str:
        if i==j:
            count+=1
    print("Frequency of",i,"is",count)