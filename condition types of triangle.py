# accept three sides of a triangle and check whether it is equilateral,isosceles,scalene triangle.

s1=float(input("Enter first side of triangle:"))
s2=float(input("Enter second side of triangle:"))
s3=float(input("Enter third side of triangle:"))
if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
    if s1==s2==s3:
      print("It is an equilateral triangle.")
    elif (s1==s2 and s2!=s3) or (s1==s3 and s3!=s2) or(s2==s3 and s3!=s1):
      print("It is an isosceles triangle.")
    elif s1!=s2 and s2!=s3 and s1!=s3:
      print("It is a scalene triangle.")
else:
    print("Not a valid triangle.")