# WAP to print all the twin prime numbers till 200.

print("Twin prime number till 200 is:",end='')
for i in range (2,201):
    for j in range (2,i):
        if i%j==0:
            break
    else:
        a=i
        b=i+2
        for k in range (2,b):
            if b%k==0:
                break
        else:
            print("(",a,",",b,")",end='')