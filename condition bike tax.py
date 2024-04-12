# WAP to accept the cost price of the bike and display the road tax to be paid according to the following criteria:
#  Cost price (in Rs)        Tax
#    >100000                 15%
#  >50000and <=100000        10%
#   <=50000                   5%
a=float(input("Enter the cost price of the bike="))
if a>100000:
    a=a*0.15
    print("Road Tax to be paid is Rs",a)
elif a>50000 and a<=100000:
    a=a*0.1
    print("Road Tax to be paid is Rs",a)
elif a<=50000:
    a=a*0.05
    print("Road Tax to be paid is Rs",a)