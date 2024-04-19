# WAP to print fibonacci sequence upto "n" term

a=0
b=1
c=int(input("Enter number:"))
print("Fibonacci Sequence upto",c,"terms are:",end='')
for i in range (0,c):
    a,b=b,a+b
    print(a,end=',')