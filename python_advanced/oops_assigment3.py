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
            print(self.balance)

    def deposit(self):
        amount=int(input("enter the deposit amount:"))
        self.balance+=amount
        print(self.balance)


l=[]
while True:
    print("1. Create a new account\n2. Withdraw\n3. Deposit\n4. show balance\n5. Exit")
    x=int(input("Enter your choice"))
    if x==1:
        a=Account()
        l.append(a)
        print(l)


    elif x==2:
        a=int(input("enter account number:"))
        for i in l:
            if i.accnumber==a:
                i.withdraw()
                break
            else:
                print("no aacount exists")

    elif x==3:
        a=int(input("enter account number:"))
        for i in l:
            if i.accnumber==a:
                i.deposit()
                break
            else:
                print("no account exists")

    elif x==4:
        a=int(input("enter account number:"))
        for i in l:
            if i.accnumber==a:
                i.showbalance()
                break
            else:
                print("no account exists")

    elif x==5:
        print("exit")
        break




