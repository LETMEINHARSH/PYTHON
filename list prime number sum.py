# WAP to take 10 elements in a list as input .
# Calculate and print sum of all the prime numbers existing in the list.

list=[]
sum=0
for i in range (1,11):
    list.append(int(input(f"Enter number {i}:")))
for j in list:
    if j>1:
        for k in range (2,j):
            if j%k==0:
                break
        else:
            sum+=j
print(f"Sum of all prime numbers in given list is {sum}.")