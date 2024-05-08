# WAP to a string as input and replace all the a's and e's with a "$" character and display the new string.

s1=input("Enter any string:")
s2=''
# s3='aAEe'
# for i in s1:
#     if i in s3:
#         s2=s2+'$'
#     else:
#         s2=s2+i
# print(s2)

for i in s1:
    if i in "aeAE":
        s2=s2+'$'
    else:
        s2=s2+i
print(s2)