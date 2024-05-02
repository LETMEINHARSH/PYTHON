# WAP to take two numbers as input , then check and print the sum of all the the common digits in both the number.

a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
e=b
while a>0:
    c=a%10
    while b>0:
        d=b%10
        if c==d:
            print(c+d)
            break
        else:
            b=b//10
    a=a//10
    b=e
else:
    print("No common digit.")