# A company decided to give bonus on the following criteria:
# time period of service     Bonus
# more than 10 years          10%
# >=6 and <=10                 8% 
# less than 6 years            5%
# Ask user for their salary and years of service and print the net bonus amount.

sl=int(input("Current salary: Rs"))
yr=int(input("Years of service:"))
if yr>10:
    print("Net Bonus Amount Reciveable: Rs",sl*0.1)
elif 6<=yr<=10:
    print("Net Bonus Amount Reciveable: Rs",sl*0.08)
elif yr<6:
    print("Net Bonus Amount Receiveable: Rs",sl*0.05)