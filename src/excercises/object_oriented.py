from src.excercises.bank_excepton import TransactionException


class BankAccount():

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise TransactionException('Cannot deposit negative amount')
        else:
            self.balance += amount
            self.display_balance()

    def withdraw(self, amount):
        if self.balance < amount:
            raise TransactionException('Insufficient funds!!')
        else:
            self.balance -= amount
            self.display_balance()

    def display_balance(self):
        print(f'{self.name}::Your new balance is {self.balance}')


try:
    raj_account = BankAccount('Raj', 1000)
    raj_account.deposit(500)
    raj_account.withdraw(700)
    raj_account.withdraw(900)
except TransactionException as ex:
    print(ex.args[1])
