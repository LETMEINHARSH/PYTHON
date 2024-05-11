# WAP to add 'ing' at the end of a given string

str=input("Enter any string:")
ing="ing"
if len(str)<3:
    print(str)
elif len(str)>=3:
    if str[-3:]==ing:
        print(str+"ly")
    else:
        print(str+"ing")