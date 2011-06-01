import unittest
from should_dsl import should
from rectangle import Rectangle

class RectangleTest(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(width=3, height=2)

    def test_it_has_width_and_height(self):
        self.rectangle.width |should| equal_to(3)
        self.rectangle.height |should| equal_to(2)

    def test_it_changes_its_width(self):
        self.rectangle.width = 5
        self.rectangle.width |should| equal_to(5)

    def test_it_changes_its_height(self):
        self.rectangle.height = 5
        self.rectangle.height |should| equal_to(5)

    def test_it_calculates_its_area(self):
        self.rectangle.area() |should| equal_to(6)

    def test_it_calculates_its_perimeter(self):
        self.rectangle.perimeter() |should| equal_to(10)

