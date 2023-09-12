class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance is ${self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance is ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount"

# Creating an instance of BankAccount
account = BankAccount("John Doe")

# Testing deposit and withdrawal functionality
print(account.deposit(1000))  # Deposited $1000. New balance is $1000
print(account.withdraw(500))   # Withdrew $500. New balance is $500
print(account.withdraw(1000))  # Insufficient funds or invalid withdrawal amount
