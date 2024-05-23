# i/p  aaabbbccc
# o/p  a3 b3 c3

str=input("Enter")
str1=''
for i in str:
    if i not in str1:
        count=str.count(i)
        str1=str1+i
        print(f"{i}{count}",end='')