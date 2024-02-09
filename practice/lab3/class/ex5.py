class bank_account:
    def __init__(self):
        self.owner = input("owner ? : ")
        self.balance = 0
    def deposit(self):
        x = int(input("enter deposit : "))
        self.balance = x + self.balance
    def withdraw(self):
        y = int(input("enter withdraw : "))
        self.balance = self.balance - y
    def show(self):
        print("owner - "+self.owner)
        print("balance - "+str(self.balance))
ba = bank_account()

ba.deposit()
ba.show()
ba.withdraw()
ba.show()

