# WAP to lowercase the first n characters in a string.

str=input("Enter any string=").upper()
n=int(input("Enter number of term to lowercase:"))
if len(str)<n:
    print("Invalid term input.")
else:
    print((str[0:n]).lower()+str[n:])