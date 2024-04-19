# WAP that iterates the integers from 1 to 50.
# For multiple of 3 print "Fizz"
# For multiple of 5 print "Buzz"
# For number divisible by 3&5 both print "FizzBuzz"

for i in range (1,50):
    if i%3==0 and i%5==0:
        print(i,"= FizzBuzz")
    elif i%3==0:
        print(i,"= Fizz")
    elif i%5==0:
        print(i,"= Buzz")
    else:
        print(i,"=")