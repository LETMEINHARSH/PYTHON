# Write a program that categorizes a given temperature into different
# levels: "Freezing" for temperatures below 0 degrees Celsius, "Cold" for
# temperatures between 0 and 10 degrees Celsius, "Moderate" for
# temperatures between 10 and 25 degrees Celsius, and "Hot" for
# temperatures above 25 degrees Celsius.

temp=int(input("Input Temperature in °Celsius:"))
if temp<=0:
    print("Freezing")
elif 0<temp<=10:
    print("Cold")
elif 10<temp<=25:
    print("Moderate")
else:
    print("Hot")