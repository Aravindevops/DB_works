try:
    print("1.Add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    a=int(input("enter your choice:"))
    x=int(input("enter a number:"))
    y=int(input("enter a number:"))

    if a==1:
        print(x+y)
    elif a==2:
        print(x-y)  
    elif a==3:
        print(x*y)
    elif a==4:
        print(x/y)

except ZeroDivisionError:
    print("division by zero is not possible")

except ValueError:
    print("value error occured")

except:
    print("invalid input")


    
