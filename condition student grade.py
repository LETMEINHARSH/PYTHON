# WAP to accept percentage from the user and display the grade according to the following criteria:
#  marks            grade
#   >90               A
#  >80and <=90        B
# >=60 and <=80       C
#  below 60           D
a=float(input("Enter the percentage obtained="))
if a>90:
    print("Grade A")
elif a>80 and a<=90:
    print("Grade B")
elif a>=60 and a<=80:
    print("Grade C")
elif a<60:
    print("Grade D")