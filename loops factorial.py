# Write a Python function that computes the factorial of a non-negative integer.

a=int(input("Enter a number:"))
if a>0:
 b=a
 for i in range (1,a,1):
    b=b*i
 print("Factorial of",a,"is:",b)
else:
  print("Enter a positive integer.")