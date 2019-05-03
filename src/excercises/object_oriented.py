from src.excercises.bank_excepton import TransactionException
import logging
from unittest import TestCase
import unittest

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
            self.display_balance()

    def withdraw(self, amount):
        if self.balance < amount:
            raise TransactionException('Insufficient funds!!')
        else:
            self.balance -= amount
            self.display_balance()

    def display_balance(self):
        logger.info(f'{self.name}::Your new balance is {self.balance}')

    def __str__(self):
        return f'Owner: {self.name}, Balance: {self.balance}'


class BankAccountTest(TestCase):

    def testDepositSuccess(self):
        bank_account = BankAccount('Raj', 1000)
        self.assertEqual('Raj', bank_account.name)
        self.assertEqual(1000, bank_account.balance)
        bank_account.deposit(500)
        self.assertEqual(1500, bank_account.balance)

    def testDepositNegativeAmount(self):
        bank_account = BankAccount('Raj', 1000)
        with self.assertRaises(TransactionException) as error:
            bank_account.deposit(-500)
        self.assertTrue('Cannot deposit negative amount' in error.exception.args)

    def testWithdrawSuccess(self):
        bank_account = BankAccount('Raj', 1000)
        bank_account.withdraw(500)
        self.assertEqual(500, bank_account.balance)

    def testWithdrawMoreThanBalance(self):
        bank_account = BankAccount('Raj', 1000)
        with self.assertRaises(TransactionException) as error:
            bank_account.withdraw(1500)
        self.assertTrue('Insufficient funds!!' in error.exception.args)

    def testDisplayStr(self):
        owner, balance = ('Raj', 1000)
        bank_account = BankAccount(owner, balance)
        result = str(bank_account)
        self.assertEqual(f'Owner: {owner}, Balance: {balance}', result)


if __name__ == '__main__':
    unittest.main()
