# Write a program to take a number as user input and check if it is Prime Adam or not.
# Prime Adam number is a number when reversed, the square of the number
# and the square of the reversed number should be reverse of each other and is also a prime number.

n=int(input("Enter a number to check:"))
sq=n**2
s1=str(n)
rev=int(s1[::-1])
revsq=rev**2
rev1=str(revsq)
if str(sq)==rev1[::-1]:
    f=0
    for i in range(2,n):
        if n%i==0:
            f=1
            break

    if f==0:
        print(n," is prime ADAM.")  

    else:
        print(n," is not prime ADAM.")