# WAP to take a string as input which contains two words seperated by a space.
# Swap the first character of each character with is last character.

s1=input("Enter any string:")
space=s1.index(" ")
s2=''
s2=s1[space-1]+s1[1:space-1]+s1[0]
s2=s2+s1[space]+s1[-1]+s1[space+2:-1]+s1[space+1]
print(s2)