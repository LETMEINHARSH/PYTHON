# WAP to print fibonacci sequence upto "n" term

a,b=0,1
c=int(input("Enter number of term:"))
print("Fibonacci Sequence upto",c,"terms are:",end='')
for i in range (0,c):
    print(a,end=',')
    a,b=b,a+b