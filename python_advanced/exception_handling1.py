try:
    x=int(input("enter a number:"))
    y=int(input("enter a number:"))
    print(x/y)
except ZeroDivisionError:
    print("division by zero is not possible")

except ValueError:
    print("value error occured")