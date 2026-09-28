class Account:
    def __init__(self):
        self.accnumber=int(input("enter the account number: "))
        self.acctname=input("enter the account name:")
        self.balance=int(input("enter the balance:"))

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


acc1=Account()
acc2=Account()

l=[acc1,acc2]
for i in l:
    print("account number:",i.accnumber)
    print("account name:",i.acctname)
    i.showbalance()
    i.withdraw()
    i.showbalance()
    i.deposit()
    i.showbalance()




