#write a program to find the count of letters,spaces and digits in a string

s="hello world 365"
letter,space,digit=0,0,0
for i in s:
    if i.isalpha():
        letter+=1
    elif i.isspace():
        space+=1
    else:
        digit+=1

print(f"letter:{letter},space:{space},digit:{digit}")