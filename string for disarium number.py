# WAP to take a number as input and check if it is disarium number.

n=int(input("Enter a number:"))
s1=str(n)
s=0
for i in range (0,len(s1)):
    s=s+int(s1[i]**(i+1))
if s==n:
    print("Disarium number.")
else:
    print("Not a disarium number.")