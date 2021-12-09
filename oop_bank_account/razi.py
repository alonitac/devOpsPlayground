
class Account :
    def __init__(self, name, balance):
        self.AccOwner=name
        self.balance =balance

    def deposit(self,amount):
        self.balance = self. balance + amount
        print('deposit accepted ', self.balance)

    def withdraw(self , amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print('succsed withdraw')
        else:
            print('Error Withdraw')






acct1=Account('razi', 188)
print(acct1.AccOwner)
print(acct1.balance)

acct1.deposit(20)
acct1.withdraw(20)
