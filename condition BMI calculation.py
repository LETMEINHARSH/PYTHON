# Build a Python program that calculates the BMI (Body Mass Index) of a person based on their weight (in kg) and height (in meters) and provides a classification (Underweight, Normal, Overweight, or Obese)

ht=float(input("Enter your height (in meter):"))
wt=float(input("Enter your weight (in kg):"))
bmi=wt/(ht**2)
print("Your BMI is",bmi)
if bmi<18.5:
    print("UNDERWEIGHT")
elif 18.5<=bmi<=24.9:
    print("HEALTHY")
elif 25<=bmi<=29.9:
    print("OVERWEIGHT")
elif 30<=bmi<=39.9:
    print("OBESE")
elif bmi>=40:
    print("SEVERELY OBESE")