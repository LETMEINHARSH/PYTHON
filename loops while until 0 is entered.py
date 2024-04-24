# WAP that keep on accepting number from user until user enters ZERO.
# Display the sum and average of all the number.

a=1
sum=0
i=1
j=-1
while (a!=0):
    print("Enter number",i,end=':')
    a=int(input())
    sum=sum+a
    i=i+1
    j=j+1
print("Sum of all entered number is:",sum)
print("Average of all entered number is:",sum/j)