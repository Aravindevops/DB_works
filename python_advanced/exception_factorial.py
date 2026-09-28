try:
    x=int(input("enter a number:"))
    for i in range(0,x):
        factorial=1
        factorial=factorial*(i+1)
        print("factorial of",i+1,"is",factorial)

except ValueError:
    print("value error occured")
except:
    print("invalid input")