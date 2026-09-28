class Account:
    def __init__(self):
        self.accnumber=int(input("enter the account number:"))
        self.acctname=input("enter the account name:")
        self.balance=0

    def showbalance(self):
        print("balance:",self.balance)

    def withdraw(self):
        amount=int(input("enter the withdraw amount:"))
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount

    def deposit(self):
        amount=int(input("enter the deposit amount:"))
        self.balance+=amount



while True:
    print("1. Create a new account\n2. Withdraw\n3. Deposit\n4. show balance\n5. Exit")
    x=int(input("Enter your choice"))
    if x==1:
        a=input("enter account number:")
        a=Account()


    elif x==2:
        a=input("enter account number:")
        a.withdraw()

    elif x==3:
        a=input("enter account number:")
        a.deposit()

    elif x==4:
        a=input("enter account number:")
        a.showbalance()

    elif x==5:
        print("exit")
        break




