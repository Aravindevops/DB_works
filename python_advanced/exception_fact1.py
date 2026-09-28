import math
while True:
    try:
        x=int(input("enter a number:"))
        print(math.factorial(x))
        break
    except ValueError:
        print("value error occured")

    except:
        print("invalid input")