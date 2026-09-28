#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8 
# characters")

try:
    p=input("enter a password:")
    if len(p)<8:
        raise ValueError("Password should be of 8 characters")

except ValueError as v:
    print(v)