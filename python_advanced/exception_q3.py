#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")
class InsuffientBalanceError(Exception):
    pass

try:
    balance=10000
    amount=int(input("enter the amount:"))
    if amount>balance:
        raise InsuffientBalanceError("Not enough balance.Transaction Failed")
    else:
        print("Transaction Successfull")
except ValueError as v:
    print(v)