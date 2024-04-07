# 1. For this challenge, create a bank account class that has two attributes:

# * owner
# * balance

# and two methods:

# * deposit
# * withdraw


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Accepted")
        else:
            print("Insufficient Balance")

# Instantiate the class
account = BankAccount("Jose", 100)

# # Test deposit and withdrawal
# account.deposit(50)
# account.withdraw(30)

# 2.Print the object
print("Owner:", account.owner)
print("Balance:", account.balance)

# 3.Show account owner attributes
print("Owner attribute:", account.owner)
# 4.Show account balance attribute
print("Balance attribute:", account.balance)

# 5.Attempt to withdraw more than available balance
account.withdraw(200)
