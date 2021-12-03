class Bank_Account:

	def __init__(self):
		self.balance = 0
		print("Hello Welcome to the Deposit & Withdrawal ATM Machine")

	def deposit(self):
		amount = float(input("Enter amount For Deposited:"))
		self.balance += amount
		print("\n Amount Deposited:", amount)

	def withdraw(self):
		amount = float(input("Enter amount To Withdrawn: "))
		if self.balance >= amount:
			self.balance -= amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Available Balance=", self.balance)


# creating an object of class
s = Bank_Account()

# functions and objects
s.deposit()
s.withdraw()
s.display()
