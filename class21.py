class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = 0
        if balance > 0:
            self._balance = balance
        self._transactionhistory = []

    def get_owner(self):
        return self.owner

    def get_balance(self):
        return self._balance

    def display_account(self, owner):
        if self.owner == owner:
            print(f"{self.owner}, ${self._balance:,.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self._balance += amount
        print(f"Deposited {amount}. New balance: ${self ._balance:,.2f}")
        self._transactionhistory.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount
        print(f"Withdrew {amount}. New balance: ${self._balance:,.2f}")
        self._transactionhistory.append(f"Withdrew {amount}")

    def print_history(self):
        print(self._transactionhistory)

class Bank:
    def __init__(self, name):
        self.name = name
        self._accounts = []

    def open_account(self, owner, balance=0):
        
        new_account = BankAccount(owner, balance)
        self._accounts.append(new_account)
        print(f"Account opened for {owner}. Account opened with ${balance:,.2f}")

    def find_account(self, owner):
        for account in self._accounts:
            if account.get_owner() == owner:
                return account
        return None

    def deposit_to(self, owner, amount):
        account = self.find_account(owner)
        if account is None:
            print("Account not found. Did you make a typo?")
            return
        account.deposit(amount)

    def withdraw_from(self, owner, amount):
        account = self.find_account(owner)
        if account is None:
            print("Account not found. Did you make a typo?")
            return
        account.withdraw(amount)

    def total_balance(self):
        return sum(account.get_balance() for account in self._accounts)

    def list_accounts(self):
        if not self._accounts:
            print("No accounts yet. Did you make a typo?")
            return
        for account in self._accounts:
            print(f"{account.get_owner()}: {account.get_balance()}")

    def close_account(self, owner):
        account = self.find_account(owner)
        if account is None:
            print("Account not found. Did you make a typo?")
            return
        account.remove()

    def avg_balance(self):
        total = sum(account.get_balance() for account in self._accounts)
        avg = total/len(self._accounts)
        return avg
    def richest_customer(self):
        richest = max(self._accounts, key=lambda account:account.balance)


acc = BankAccount('Ithasanamenow', 10000)
acc.deposit(10000)
acc.withdraw(5000)

acc.print_history()