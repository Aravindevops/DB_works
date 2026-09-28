x=input("enter word :\n").lower()
f=open("file.txt",'r')
lines=f.read()
words=lines.split()
if x in words:
    print("word found")
else:
    print("word not found")
f.close()
