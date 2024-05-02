# WAP to take a number as input, check and print adam number or not.

n=int(input("Enter a number:"))
sqn=n**2
rn=str(n)
rn=int(rn[-1::-1])
sqrn=rn**2
sqrn=str(sqrn)
if sqn==int(sqrn[::-1]):
    print("ADAM NUMBER.")
else:
    print("Not an adam number.")