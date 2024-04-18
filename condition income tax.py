# 9- Create a program that asks the user for their income and calculates the
# tax they need to pay based on the following tax brackets: 
# ● Income up to $10,000: 5% tax
# ● Income from $10,001 to $50,000: 10% tax
# ● Income above $50,000: 20% tax
a=float(input("Enter your income (in $)="))
if a<=10000:
    a=a*0.05
    print("Tax to be paid is $",a)
elif 10001<=a<50000:
    a=a*0.1
    print("Tax to be paid is $",a)
elif a>=50000:
    a=a*0.20
    print("Tax to be paid is $",a)