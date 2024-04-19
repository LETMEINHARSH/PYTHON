# Write a Python program to calculate the sum of all numbers in range(take as input) using a for loop. 
# Print the final sum.

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
sum=0
for i in range (a,b+1):
    sum=sum+i
print("Sum of all natural numbers from",a,"to",b,"is:",sum)