f=open("file.txt",'r')
content=f.read()
c=open("file2.txt",'a')
c.write(content)

f.close()
c.close()


