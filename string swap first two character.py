# WAP to get a single string from two given string,seperated by a space and swap the first two characters of each string.
# Sample string: 'abc','xyz'
# expected result: 'xyc abz'

s1=input("Enter string 1:")
s2=input("Enter string 2:")
s3=''
s3=s2[0:2]+s1[2:]+' '+s1[0:2]+s2[2:]
print(s3)