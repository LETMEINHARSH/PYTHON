# WAP to take a list of 10 element as input segregated and print the sum of odd and even number seperately.

l1=[]
for i in range (1,11):
    l1.append(int(input(f"Enter a number {i} = ")))
sum_even,sum_odd=0,0
for j in l1:
    if j%2==0:
        sum_even+=j
    else:
        sum_odd+=j
print(f"Sum of all even numbers are {sum_even}")
print(f"Sum of all odd numbers are {sum_odd}")