# WAP to reverse the input number.

a=int(input("Enter a number:"))
if a>0:
    for i in range (a):
     b=a%10
     a=a//10
     print(b,end='')
     if a<10:
        print(a)
        break
else:
   print("Enter a positive interger.")