class BankAccountAgent:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # double underscore = "private" attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.name}: deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"{self.name}: insufficient funds.")
        else:
            self.__balance -= amount
            print(f"{self.name}: withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance


acc = BankAccountAgent("Chaitanya", 1000)
acc.deposit(500)
acc.withdraw(2000)     # should fail, insufficient funds
acc.withdraw(300)

print(acc.get_balance())   # correct way to access private data

# Try accessing directly (will fail):
# print(acc.__balance)     # uncomment to see the AttributeError