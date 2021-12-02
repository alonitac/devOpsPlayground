
class Account:

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def __str__(self):
        return "Account Owner: " + self.owner + "\n" + "Account Balance: " + str(self.balance)

    def deposit(self,amount):
        self.balance += amount
        print("Deposit Accepted")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            return print("withdraw successful")
        else:
            print("funds not available")


acc1=Account("adams",1000)
print(acc1)
acc1.deposit(200)
print(acc1)
acc1.withdraw(1000)
print(acc1)
acc1.withdraw(200)
acc1.withdraw(200)
