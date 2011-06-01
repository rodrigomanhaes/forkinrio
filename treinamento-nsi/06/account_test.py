import unittest
from should_dsl import should, should_not
from account import Account, InsufficientBalance

class AccountTest(unittest.TestCase):

    def setUp(self):
        self.account = Account(number='123456', holder='Linus')

    def test_it_has_a_number(self):
        self.account.number |should| equal_to('123456')

    def test_it_as_a_holder(self):
        self.account.holder |should| equal_to('Linus')

    def test_it_has_a_balance_beginning_at_zero(self):
        self.account.balance |should| be(0)

    def test_it_allows_deposit(self):
        self.account.deposit(100)
        self.account.balance |should| be(100)
        self.account.deposit(100)
        self.account.balance |should| be(200)

    def test_it_allows_withdrawals(self):
        self.account.deposit(100)
        self.account.withdrawal(75)
        self.account.balance |should| be(25)

    def test_it_raises_an_error_for_insufficient_balance(self):
        self.account.deposit(100)
        (self.account.withdrawal, 100.01) |should| throw(InsufficientBalance)

