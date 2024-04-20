# WAP a program to take 10 number as input and print their average.

sum=0
for i in range (0,10):
    a=int(input("Enter a number:"))
    sum=sum+a
print("Average of given number is:",sum/10)