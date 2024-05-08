# WAP to change every alternate character of the string in uppercase if it is an alphabet.

s1=input("Enter any string:")
s2=" "
for i in range (0,len(s1)):
    if i%2==0:
        s2=s2+s1[i].upper()
    else:
        s2=s2+s1[i]
print(s2)