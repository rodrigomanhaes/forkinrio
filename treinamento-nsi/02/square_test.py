import unittest
from should_dsl import should
from square import Square

class SquareTest(unittest.TestCase):

    def setUp(self):
        self.square = Square(side=3)

    def test_it_has_a_side(self):
        self.square.side |should| equal_to(3)

    def test_it_changes_its_side(self):
        self.square.side = 5
        self.square.side |should| equal_to(5)

    def test_it_calculates_its_area(self):
        self.square.area() |should| equal_to(9)

