# WAP to reverse a string if its length is a multiple of 4.

str=input("Enter any string:")
if len(str)%4==0:
    print(str[-1::-1])
else:
    print(str)