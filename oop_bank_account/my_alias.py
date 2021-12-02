class Account:
    def __init__(self, name, init_balance):
        self.owner = name
        self.balance = init_balance

    def __str__(self):
        return "Account Owner: " + self.owner + "\n" + "Account Balance: " + str(self.balance)

    def is_valid_amount(self, amount):
        is_valid = amount >= 0 and type(amount) == int
        return is_valid

    def deposit(self, amount):
        if not self.is_valid_amount(amount):
            raise RuntimeError('amount is not valid')

        self.balance = self.balance + amount
        print('Deposit Accepted')

    def withdraw(self, amount):
        if not self.is_valid_amount(amount):
            raise RuntimeError('amount is not valid')

        if self.balance - amount >= 0:
            self.balance -= amount
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


acct1 = Account('Jose', 100)

print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)
acct1.withdraw(75)

acct1.withdraw(500)

print(acct1)
