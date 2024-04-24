# WAP to take a number as input to count the number of digit present in the number.

n=int(input("enter a number:"))
count=0
if n>=0:
    if n==0:
        print("number of digit entered is: 1")
    else:
        while n>0:
            n=n//10
            count=count+1
        print("Number of digit entered is:",count)
else:
    print("Enter a positive integer.")