from src.excercises.bank_excepton import TransactionException
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
logger = logging.getLogger()


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise TransactionException('Cannot deposit negative amount')
        else:
            self.balance += amount
            # self.display_balance()

    def withdraw(self, amount):
        if self.balance < amount:
            raise TransactionException('Insufficient funds!!')
        else:
            self.balance -= amount
            # self.display_balance()

    def display_balance(self):
        logger.info(f'{self.name}::Your new balance is {self.balance}')

    def __str__(self):
        return f'Owner: {self.name}, Balance: {self.balance}'


try:
    raj_account = BankAccount('Raj', 1000)
    logger.info(raj_account)
    raj_account.deposit(500)
    logger.info(raj_account)
    raj_account.withdraw(700)
    logger.info(raj_account)
    raj_account.withdraw(900)
    logger.info(raj_account)
except TransactionException as ex:
    logger.error(ex.args[1])
