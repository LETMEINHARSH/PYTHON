# WAP to take a list of string as input and filter out all the strings having more than 2 vowels present in them.
# input: ["apple","banana","cherry","date","fig","grape"]
# output:["banana"]

l1=[]
l2=[]
str1="aeiouAEIOU"
range1=int(input("Enter number words to input:"))
for x in range (1,range1+1):
    l1.append(input(f"Enter word{x}:"))
for i in l1:
    count=0
    for j in i:
        if j in str1:
            count+=1
    if count>2:
        l2.append(i)
print(f"Words with more than 2 vowels are {l2}")