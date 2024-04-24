# WAP to accept 10 numbers as input and display their average.

sum=0
for i in range (1,11):
    print("Enter number",i,end=': ')
    a=int(input())
    sum=sum+a
print("Average of entered 10 digit number is:",sum/10)