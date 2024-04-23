# WAP to find the sum of factorial of all the odd numbers till 20.

sum=0
for i in range (1,21,2):
    fact=1
    for j in range (1,i+1):
        fact=fact*j
    sum=sum+fact
print(sum)