# WAP to count number of words with the same first and last characters in a given string.
# input: consistent madam level noon civic race
# output: 4

str=input("Enter a string:")
s1=str.split()
count=0
for i in s1:
    if i[0]==i[-1]:
        count+=1
print(f"Words with the same first and last character:{count}")