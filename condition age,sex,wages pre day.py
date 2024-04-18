# accept the age,sex,number of days and display the wages accordingly.
#      age         Sex       WAGES/day
# >=18 and <30      M           700
#                   F           750
# >=30 and <=40     M           800
#                   F           850
# If age does not fall in any range then display the following message: "Enter appropriate age"

age=int(input("Enter your age:"))
sex=(input("Gender:"))
days=int(input("Enter number of days worked:"))
if 30>age>=18 and (sex=="M" or sex=="m"):
    print("Total wages is:",days*700)
elif 30>age>=18 and (sex=="F" or sex=="f"):
    print("Total wages is:",days*750)
elif 40>=age>=30 and (sex=="M" or sex=="m"):
    print("Total wages is:",days*800)
elif 40>=age>=30 and (sex=="F" or sex=="f"):
    print("Total wages is:",days*850)
else:
    print("Enter appropriate age")