# Implement a Python program to convert a given number of days into years, weeks, and days.

a=int(input("Enter Number of Days:"))
yr=a/365         #number of year
weeks=a/7        #number of weeks
hr=a*24          #number of hour
minute=a*1440    #number of minute
second=a*86400   #number of seconds
print("Total number to years:",yr)
print("Total number of weeks:",weeks)
print("Total number of Hours:",hr)
print("Total number of Minutes:",minute)
print("Total number of seconds:",second)