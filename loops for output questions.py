# # 001
# x=2
# for i in range (1,5):
#     x=x+5
# print(x)

# # 002
# x=5
# y=2
# for i in range (1,10,2):
#     x=x+5
#     y=x+y
# print(x)
# print(y)

# # 003
# x=9654392
# y=2
# for i in range (1,15,3):
#     x=x//10
#     y=(x%100)+y
#     print(x)
# print(x)
# print(y)

# # 004
# y=912
# z=243
# for i in range (1,7,2):
#     x=(y%10)+(z//10)
#     y=y//10
#     z=z//10
#     print(x+i)
# print(x)
# print(y)
# print(z)

# # 005
# x=9
# y=7
# for i in range(0,10,2):
#     if(x+i)%2==0:
#         x=x+5
#         y=x+i+y
#     elif(x+i)%3==0:
#         y=y+9
#         x=x+i+y
#     else:
#         x=x+i
#         y=y+i
#     print(x)
#     print(y)
# print(x)
# print(y)

# # 006
# a=5
# b=456789
# for i in range (a,b%10):
#     if a%5==0 and b%5==0:
#         b=b//100
#         print(a+100)
#     elif (b%10)%3==0:
#         print(b+a)
#         b=b%10
#     else:
#         a=a+5
#         print(a)
#     b=b//10
# print(a)
# print(b)