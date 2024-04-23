# WAP to take a three digit number as input and if the last digit of the number is prime then find the 
# factorial of the last digit.

a=int(input("Enter a 3 digit number:"))
if 100<=a<=999:
    a=a%10
    if a==0:
        print(a,"is nor prime nor composite.")
    elif a==1:
        print(a,"is nor prime nor composite.")
        print("Factorial of",a,"is 1.")
    elif 2<=a<=9:
        for i in range (2,a):
            if a%i==0:
                print(a,"is not a prime number.")
                break
        else:
            print(a,"is a prime number.")
            fact=1
            for i in range (a,0,-1):
                fact=fact*i
            print("Factorial of",a,"is",fact,".")
else:
    print("Enter a positive three digit number.")