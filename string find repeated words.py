# WAP take a sentence as input ,find and print repeated word.

str=input("Enter a sentence:")
words=str.split()
fr_words=''
max_c=0
for i in words:
    c=words.count(i)
    if max_c<c:
        max_c=c
        fr_words=i
print(f"Most fequent word in the given string is {fr_words} and its frequency is {max_c}")