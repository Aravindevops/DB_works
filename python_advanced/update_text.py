f=open("file.txt",'r')
lines=f.readlines()
lines[1]="hahaha\n"
print(lines)
f.close()

f=open("file.txt",'w')
f.writelines(lines)
f.close()

