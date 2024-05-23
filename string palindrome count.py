# WAP to count occurrences of all the words which are palindromes in a string.
# input:
# Anna went to see civic events at the noon level in a racecar.
# output:
# Palindrome words and their counts :
# "Anna":1
# 'civic':1
# 'noon':1
# 'level':1
# 'racecar':1

s1=input("Enter a string:")
s2=s1.split()
s3=''
print("Palindrome words and their counts:")
for i in s2:
    if i[0::]==i[-1::-1]:
        count=s2.count(i)
        if i not in s3:
            print(i,count)
            s3=s3+i