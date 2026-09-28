f=open("file.txt",'r')
lines=f.readlines()
reverse=lines[::-1]
print(reverse)
f.close()

