import os
def read():
    x=input("enter file name:")
    f=open(x,'r')
    print(f.read())
    f.close()
def write():
    x=input("enter file name: ")
    content=input("enter the content to be written: ")
    f=open(x,'w')
    f.write(content)
    f.close()
def append():
    x=input("enter file name: ")
    content=input("enter the content to be written: ")
    f=open(x,'a')
    f.write(content)
    f.close()
def search():
    x=input("enter file name: ")
    word=input("enter the word to be searched: ")
    f=open(x,'r')
    content=f.read()
    if word in content:
        print(f"word found in file {x}")
    else:
        print("word not found")
def delete():
    x=input("enter file name: ")
    os.remove(x)



    

while True:
    print("1.file read\n2.file write\n3.file append\n4.file search\n5.file delete\n6.exit")
    x=int(input("enter your choice: "))
    if x==1:
        read()
    elif x==2:
        write()
    elif x==3:
        append()
    elif x==4:
        search()
    elif x==5:
        delete()
    else:
        print("exit")
        break