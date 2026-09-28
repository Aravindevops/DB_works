#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"

try:
    if int(input("enter anumber:"))<=0:
        raise ValueError("Number must be Positive")
    else:
        print("number is positive")

except ValueError as v:
    print(v)