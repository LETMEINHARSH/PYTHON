# WAP to take 7 numbers as input find the smallest element among them.

list1=[]
for i in range (1,7):
    x=int(input(f"Enter number {i}="))
    list1.append(x)
l1=list1[0]
for i in list1:
    if i<l1:
        l1=i
print(f"Smallest entered value is {l1}.")