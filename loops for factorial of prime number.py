# WAP to print the factorial of all the prime numbers till 20.

for i in range (2,21):
    for j in range (2,i):
        if (i%j)==0:
            break
    else:
        fact=1
        for k in range (i,0,-1):
            fact=fact*k
        print("Fact of",i,"is",fact,".")