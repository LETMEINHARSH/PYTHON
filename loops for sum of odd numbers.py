# WAP to print sum of all odd number from 1 to 50.

sum=0
for i in range (0,51):
    if i%2==0:
        continue
    else:
     sum=sum+i
print(sum)