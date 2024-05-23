# WAP to take input and print the following pattern
# INPUT: 1
# OUTPUT: *
# I/P: 2
# O/P:  *
#      ***
#       *
# if i/p: 3
# o/p:     *
#         ***
#        *****
#         ***
#          *
n=int(input("Enter:"))
for i in range (1,n+1):
    print((" "*(n-i))+"*"*((2*i)-1))
for j in range (n-1,0,-1):
    print((" "*(n-j))+"*"*((2*j)-1))