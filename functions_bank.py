class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def credited(self,amount):
        self.balance+=amount
        print(f"your are deposited {amount} and your balance is {self.balance}")
    def debited(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"your current balance is {self.balance}")
        else:
            print("insufficient balance")
a1=BankAccount("prasad",0)
print(a1.credited(10000))
print(a1.debited(10000))
print(a1.debited(10001))
