# WAP to take a list of 10 elements as input, check and print all numbers which are disarium numbers.
# A number is disarium number when the sum of its digit raised to the power of their respective positions
# is equal to the number it self.

# input: [89,175,8,12,7,135,518,246,1,45]
# output:Disarium numbers in the list are: [89,175,8,7,135,518,1]

l1=[]
l2=[]
for i in range (1,11):
    x=int(input(f"Enter number {i} :"))
    l1.append(x)
for j in l1:
    sum=0
    s1=str(j)
    for k in range (0,len(s1)):
        sum=(int(s1[k])**(k+1))+sum
    if sum==j:
        l2.append(sum)
print(l2)