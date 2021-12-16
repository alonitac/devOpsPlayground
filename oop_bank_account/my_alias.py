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


class StudentAccount(Account):
    """
    Student account is an account that:
    1. For every deposit, the student is getting 10% additional amount from the bank
    2. Student can not withdraw more that 1000$
    3. Students can add their friends as account members
    """

    def deposit(self, amount):
        super().deposit(round(amount * 1.1))

    def withdraw(self, amount):
        if amount <= 1000:
            super().withdraw(amount)
        else:
            print('Unsupported operation for students account')

    def add_friend(self, name):
        """
        Add name to account friends name
        :param name:
        :return:
        """
        pass


acct1 = StudentAccount('Jose', 100)

print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)
print(acct1.balance)

acct1.withdraw(75)

acct1.withdraw(5000)

print(acct1)
