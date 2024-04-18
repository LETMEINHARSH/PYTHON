# accept the following from the user and calculate the percentage of class attended:
# a. Total number of working days.
# b. Total number of days for absent
# After calculatin show that,if the percentage is less than 75,then student will not be able to sit in exam.

wd=int(input("Enter number of Working Days:"))
ab=int(input("Enter number of days absent:"))
pca=((wd-ab)/wd)*100
print("Percentage of class attended:",pca)
if pca<75:
    print("You are not eligible to sit in exam")
else:
    print("You are eligible to sit in exam")