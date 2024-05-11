# WAP to find first repeated character in a string.

str=input("Enter any string:")
for i in str:
    for j in range (str.index(i)+1,len(str)):
        if i==str[j]:
            print("First repeated character is:",i)
            break
    if i==str[j]:
        break
else:
    print("No repeated character.")