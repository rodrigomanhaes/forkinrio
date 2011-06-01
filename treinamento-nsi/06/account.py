class Account(object):

    def __init__(self, number, holder):
        self._number = number
        self._holder = holder
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, value):
        self._balance += value

    def withdrawal(self, value):
        if self._balance > value:
            self._balance -= value
        else:
            raise InsufficientBalance()

    @property
    def number(self):
        return self._number

    @property
    def holder(self):
        return self._holder


class InsufficientBalance(Exception):
    pass

