# WAP to print fibonnaci sequence.

t1,t2=0,1
t=int(input("Enter number of terms:"))
c,nt=0,0
while c<t:
    print(t1,end=' ')
    t1,t2=t2,t1+t2
    c=c+1