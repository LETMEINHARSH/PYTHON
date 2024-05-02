# WAP to take a number as input and check if it is adm number or not.

n=int(input("Enter a number:"))
sqn=n**2
revn,revn1=0,0
while n>0:
    a=n%10
    revn=(revn*10)+a
    n=n//10
sqrevn=revn**2
while sqrevn>0:
    b=sqrevn%10
    revn1=(revn1*10)+b
    sqrevn=sqrevn//10
if sqn==revn1:
    print("Adam Number.")
else:
    print("Not a Adam Number.")