# WAP to take 3 number as input and check and print which is greater.
a=int(input("Enter a number1 ="))
b=int(input("Enter a number2 ="))
c=int(input("Enter a number3 ="))
if c<a>b:
    print(a,"is greater than",b,"and",c)
elif c<b>a:
    print(b,"is greater than",a,"and",c)
elif a<c>b:
    print(c,"is greater than",a,"and",b)
elif c<a==b>c:
    print(a,"and",b,"are equal and greater than",c)
elif b<a==c>b:
    print(a,"and",c,"are equal and greater than",b)
elif a<c==b>a:
    print(b,"and",c,"are equal and greater than",a)
elif a==b==c:
    print("All given number",a,",",b,"and",c,"are equal")