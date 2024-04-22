# WAP to print the sum of all prime number between 1 to 20.

sum=0
for i in range (2,20):
    for j in range (2,i):
     if (i%j)==0:
      break
    else:
      sum=sum+i
print(sum)