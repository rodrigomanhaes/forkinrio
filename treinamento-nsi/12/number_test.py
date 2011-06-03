import unittest
from should_dsl import should, should_not
from number import Number


class NumberTest(unittest.TestCase):

    def test_it_informs_it_is_odd(self):
        Number(0) |should_not| be_odd
        Number(1) |should| be_odd
        Number(2) |should_not| be_odd
        Number(3) |should| be_odd
        Number(4) |should_not| be_odd
        Number(5) |should| be_odd

    def test_it_informs_it_is_even(self):
        Number(0) |should| be_even
        Number(1) |should_not| be_even
        Number(2) |should| be_even
        Number(3) |should_not| be_even
        Number(4) |should| be_even
        Number(5) |should_not| be_even

    def test_it_converts_itself_to_roman_numeral(self):
        Number(1).roman |should| equal_to('I')
        Number(2).roman |should| equal_to('II')
        Number(3).roman |should| equal_to('III')
        Number(4).roman |should| equal_to('IV')
        Number(5).roman |should| equal_to('V')
        Number(6).roman |should| equal_to('VI')
        Number(7).roman |should| equal_to('VII')
        Number(8).roman |should| equal_to('VIII')
        Number(9).roman |should| equal_to('IX')
        Number(10).roman |should| equal_to('X')

        Number(12).roman |should| equal_to('XII')
        Number(23).roman |should| equal_to('XXIII')
        Number(34).roman |should| equal_to('XXXIV')
        Number(45).roman |should| equal_to('XLV')
        Number(56).roman |should| equal_to('LVI')
        Number(67).roman |should| equal_to('LXVII')
        Number(78).roman |should| equal_to('LXXVIII')
        Number(89).roman |should| equal_to('LXXXIX')
        Number(91).roman |should| equal_to('XCI')
        Number(100).roman |should| equal_to('C')

        Number(102).roman |should| equal_to('CII')
        Number(213).roman |should| equal_to('CCXIII')
        Number(324).roman |should| equal_to('CCCXXIV')
        Number(435).roman |should| equal_to('CDXXXV')
        Number(546).roman |should| equal_to('DXLVI')
        Number(657).roman |should| equal_to('DCLVII')
        Number(768).roman |should| equal_to('DCCLXVIII')
        Number(879).roman |should| equal_to('DCCCLXXIX')
        Number(981).roman |should| equal_to('CMLXXXI')

        Number(1000).roman |should| equal_to('M')
        Number(1673).roman |should| equal_to('MDCLXXIII')
        Number(2456).roman |should| equal_to('MMCDLVI')
        Number(3888).roman |should| equal_to('MMMDCCCLXXXVIII')
        Number(3999).roman |should| equal_to('MMMCMXCIX')

    def it_calculates_its_value_in_fibonacci_set(self):
        Number(1).fibonacci |should| equal_to(Number(1))
        Number(2).fibonacci |should| equal_to(Number(1))
        Number(3).fibonacci |should| equal_to(Number(2))
        Number(4).fibonacci |should| equal_to(Number(3))
        Number(5).fibonacci |should| equal_to(Number(5))
        Number(6).fibonacci |should| equal_to(Number(8))
        Number(7).fibonacci |should| equal_to(Number(13))
        Number(8).fibonacci |should| equal_to(Number(21))
        Number(9).fibonacci |should| equal_to(Number(34))
        Number(10).fibonacci |should| equal_to(Number(55))

    def it_calculates_its_factorial(self):
        for method in ['looping_factorial', 'recursive_factorial', 'functional_factorial']:
            getattr(Number(1), method)() |should| equal_to(1)
            getattr(Number(2), method)() |should| equal_to(2)
            getattr(Number(3), method)() |should| equal_to(6)
            getattr(Number(4), method)() |should| equal_to(24)
            getattr(Number(5), method)() |should| equal_to(120)
            getattr(Number(6), method)() |should| equal_to(720)

