# WAP to take 10 element as input ,
# find all the element who have their sum of digits as odd number.

l1,l2=[],[]
for i in range (1,11):
    l1.append(int(input(f"Enter number {i} = ")))
for i in l1:
    s1=str(i)
    sum=0
    for j in s1:
        sum+=int(j)
    if sum%2!=0:
       l2.append(i)
print(f"Element whose sum of digit is odd are {l2}")