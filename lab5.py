class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        print(f"Your total balance: ${self.balance}, Your deposit: ${amount}")
        self.transactions.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Your total balance: ${self.balance}, Withdrawn amount: ${amount}")
            self.transactions.append(f"Withdrawed ${amount}")

    def display_balance(self):
        print(f"Current balance: ${self.balance}")
    
    def display_transactions(self):
        print("Transaction history:")
        for transaction in self.transactions:
            print(transaction)

account1 = Account(123, 'Ahmet', 1000)
account1.deposit(230)
account1.withdraw(120)
account1.display_balance()
account1.display_transactions()
print("-------------------------------")
account2 = Account(456, "Zeynep", 100)
account2.withdraw(500)
account2.display_balance()
account2.display_transactions()