# WAP to count repeated characters in a string .
# sample string:"thequickbrownfoxjumpsoverthelazydog"
# Expected output:
# o 4
# e3
# u 2
# h 2
# r2
# t2

str=input("Enter a string:")
for i in str:
    count=0
    for j in str:
        if i ==j:
            count+=1
    if count>1:
        print(i,count)