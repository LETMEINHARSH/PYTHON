# WAP to take a number of input and check if it is disarium number.

a=int(input("Enter a number:"))
b,c=a,a
count=0
sum=0
while a>0:
    count=count+1
    a=a//10
for i in range (count,0,-1):
    d=b%10
    sum=(sum)+(d**(i))
    b=b//10
if sum==c:
    print("Disarium Number.")
else:
    print("Not a disarium number.")