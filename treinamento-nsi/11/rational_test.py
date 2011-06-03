import unittest
from should_dsl import should
from rational import RationalNumber


class RationalNumberTest(unittest.TestCase):

    def test_it_has_numerator_and_denominator(self):
        number = RationalNumber(numerator=2, denominator=3)
        number.numerator |should| be(2)
        number.denominator |should| be(3)

    def test_it_automatically_reduce_itself_to_simplest_form(self):
        number = RationalNumber(6, 18)
        number.numerator |should| be(1)
        number.denominator |should| be(3)

    def test_it_adds_itself_to_another_rational(self):
        r1 = RationalNumber(1, 2)
        r2 = RationalNumber(2, 3)
        r1 + r2 |should| equal_to(RationalNumber(7, 6))

    def test_it_subtracts_other_rational_from_itself(self):
        r1 = RationalNumber(2, 3)
        r2 = RationalNumber(1, 2)
        r1 - r2 |should| equal_to(RationalNumber(1, 6))

    def test_it_multiplies_itself_by_other_rational(self):
        r1 = RationalNumber(2, 3)
        r2 = RationalNumber(3, 5)
        r1 * r2 |should| equal_to(RationalNumber(2, 5))

    def test_it_divides_itself_by_other_rational(self):
        r1 = RationalNumber(2, 3)
        r2 = RationalNumber(5, 6)
        r1 / r2 |should| equal_to(RationalNumber(4, 5))

    def test_it_compares_itself_to_another_rational(self):
        RationalNumber(2, 3) |should| equal_to(RationalNumber(4, 6))

    def test_it_provides_a_string_representation(self):
        str(RationalNumber(5, 3)) |should| equal_to('5/3')

