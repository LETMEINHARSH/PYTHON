# WAP to takea threshold as input ,print all the numbers divisible by both 3 & 5 till that number.

a=int(input("Enter the threshold:"))
print("Number divisible by both 3 & 5 are:",end='')
for i in range (1,a+1):
    if i%3==0 and i%5==0:
        print(i,end=',')