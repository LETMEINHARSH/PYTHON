# Write a program to find the first appearance of the substrings 'not' and 'poor' in
# a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with
# 'good'. Return the resulting string.
# Sample String : 'The lyrics are not that poor!'
# 'The lyrics are poor!'
# Expected Result : 'The lyrics are good!'
# 'The lyrics are poor!'

str=input("Enter any string:")
s2=str.find("not")
s3=str.find("poor")
if s2!=-1 and s3!=-1 and s2<s3:
    print(str[:s2]+"good"+str[s3+4:])
else:
    print(str)
