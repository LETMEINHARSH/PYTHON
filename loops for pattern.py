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

# WAP to print the following pattern.
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

for i in range (5,0,-1):
    for j in range (i):
        print(i,end=' ')
    print()

# 004 WAP to print following pattern
# *
# **
# ***
# ****
# *****

for i in range (1,6):
    for j in range(i):
        print('*',end='')
    print()