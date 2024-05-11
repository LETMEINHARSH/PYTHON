# WAP to insert space before every capital letter appears in a given word.
# Sample Data:
# ("PythonExercises") -> "Python Exercises"
# ("Python") -> "Python"
# ("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"

str=input("Enter any string:")
s1=str[0]
for i in range (1,len(str)):
    if str[i].islower():
        s1=s1+str[i]
    elif str[i].isupper():
        s1=s1+' '+str[i]
print(s1)