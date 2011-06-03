import unittest
from should_dsl import should
from complex_number import ComplexNumber


class ComplexNumberTest(unittest.TestCase):

    def setUp(self):
        self.number = ComplexNumber(real=5, imaginary=3)

    def test_it_has_a_real_part(self):
        self.number.real |should| equal_to(5)

    def test_it_has_an_imaginary_part(self):
        self.number.imaginary |should| equal_to(3)

    def test_it_adds_itself_to_another_complex(self):
        c1 = ComplexNumber(real=3, imaginary=2)
        c2 = ComplexNumber(real=4, imaginary=1)
        c1 + c2 |should| equal_to(ComplexNumber(real=7, imaginary=3))

    def test_it_compares_itself_to_another_complex(self):
        ComplexNumber(real=2, imaginary=3) |should| equal_to(
            ComplexNumber(real=2, imaginary=3))

    def test_it_subtracts_other_complex_from_itself(self):
        c1 = ComplexNumber(real=3, imaginary=2)
        c2 = ComplexNumber(real=4, imaginary=1)
        c1 - c2 |should| equal_to(ComplexNumber(real=-1, imaginary=1))

    def test_it_multiplies_itself_by_other_complex(self):
        c1 = ComplexNumber(real=3, imaginary=2)
        c2 = ComplexNumber(real=4, imaginary=1)
        c1 * c2 |should| equal_to(ComplexNumber(real=10, imaginary=11))

    def test_it_divides_itself_by_other_complex(self):
        c1 = ComplexNumber(real=3, imaginary=2)
        c2 = ComplexNumber(real=4, imaginary=1)
        resultado = c1 / c2
        resultado.real |should| close_to(0.8235, delta=0.0001)
        resultado.imaginary |should| close_to(0.2941, delta=0.0001)

    def test_it_provides_a_string_representation(self):
        str(ComplexNumber(real=5, imaginary=3)) |should| equal_to('5+3i')

