class Bank_Account:
    def __init__ (self):
        self.balance=0
        print("Hello!welcome to the Deposit & Withdrwal Machine")
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance+=amount
        print("\n Amount Deposited:",amount)
    def withdraw(self):
        amount=float(input("Enter amount to be Withdarwn:"))
        if self.balance>=amount:
            self.balance=amount
            print("\n You Withdraw:",amount)
        else:
            print("\n Insufficient balance")

    def display(self):
           print("\$GetCurrentn Net Avaliable Balance=",self.balance)
s=Bank_Account()
s.deposit()
s.withdraw()
s.display()
