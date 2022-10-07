"""
Create a Python class called BankAccount which represents a bank account, 
having as attributes: accountNumber (numeric type), name (name of the account 
owner as string type), balance.

-Create a constructor with parameters: accountNumber, name, balance.
-Create a Deposit() method which manages the deposit actions.
-Create a Withdrawal() method which manages withdrawals actions.
-Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
-Create a display() method to display account details.
-Give the complete code for the BankAccount class
"""


BANK_FEES_PERCENTAGE = 0.05


class Account:
    account_number: int
    owner_name: str
    balance: float

    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner_name = owner
        self.balance = balance

    def __repr__(self):
        data_dict = {
            'account_number': self.account_number,
            'owner_name': self.owner_name,
            'balance': self.get_balance(),
            'bank_fees': self.get_bank_fees()
        }
        return f"Bank Account: {data_dict}"

    def deposit(self, amount):
        self.balance += amount
        return self.get_balance()

    def withdraw(self, amount):
        self.balance -= amount
        return self.get_balance()

    def get_bank_fees(self):
        return self.get_balance() * BANK_FEES_PERCENTAGE

    def get_balance(self):
        return self.balance
