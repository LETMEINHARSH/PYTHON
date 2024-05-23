# WAP to take a list of 10 element as input,find and print second largest element present in the list.

l1=[]
for i in range (1,11):
    l1.append(int(input(f"Enter number {i}=")))
l3=[]
for k in range (0,2):
    l2=0
    for j in l1 :
        if j in l3:
            break
        else:
            if j>l2:
                l2=j
    l3.append(l2)
print(f"Second Largest Element is {l3[1]}.")