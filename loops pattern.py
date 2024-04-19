# WAP to print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range (1,5):
    for j in range (1,i+1):
        print(j,end=' ')
    print()

# WAP to print the following pattern
# * * * *
# * * *
# * *
# *

for i in range (4,0,-1):
    for j in range (i):
        print("*",end=' ')
    print()