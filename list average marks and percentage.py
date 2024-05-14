# WAP to find average and percentage of marks.
# take 5 subject marks as input.

l1=[]
total_marks=0
for i in range (1,6):
    x=int(input(f"Enter Marks of subject {i}:"))
    l1.append(x)
    total_marks+=x
print(f"Average of marks is {total_marks/5}")
print(f"Percentage obtained by student is {total_marks/5}%")