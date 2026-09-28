import math
while True:
    try:
        x=int(input("enter a number:"))
        print(math.factorial(x))
        break
    except ValueError as v:
        print("value error occured")
        print(type(v))

    except:
        print("invalid input")