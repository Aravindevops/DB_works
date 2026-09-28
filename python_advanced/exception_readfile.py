try:
    abc=input("enter the file name:")
    f=open(abc,'r')
    print(f.read())

except FileNotFoundError:
    print("file not found")

except:
    print("invalid input")