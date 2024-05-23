# WAP to remove dublicate for the list.
# input- [2,3,7,2,9]
# output- [2,3,7,9]

l1=[2,3,7,2,9]
l2=[]
# for i in range (1,11):
#     l1.append(int(input(f"Enter number {i}")))
for j in l1:
    if j in l2:
        continue
    else:
        l2.append(j)
print(l2)