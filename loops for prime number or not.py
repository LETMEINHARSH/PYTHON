# WAP to check if a number is prime number or not.

a=int(input("Enter a number:"))
if a>0:
 if a==1:
    print("Nor prime,nor composite number")
 else:
    for i in range (2,a):
        if a%i==0:
            print(a,"is not a prime number")
            break
    else:
        print(a,"is a prime number.")
else:
   print("Enter a positive integer")