# 7- Write a program to find the prime factor of a number.
# If a factor of a number is a prime number then it is its prime factor.

a=int(input("Enter a number:"))
print("Prime Factor of",a,"is",end=':')
for i in range (2,a):
    if a%i==0:
        for j in range (2,i):
            if i%j==0:
                break
        else:
            print(i,end=',')