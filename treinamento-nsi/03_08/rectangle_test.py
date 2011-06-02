import unittest
from should_dsl import should, should_not
from rectangle import Rectangle, CartesianRectangle, Point

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



class CartesianRectangleTest(unittest.TestCase):

    def setUp(self):
        self.rectangle = CartesianRectangle(width=3, height=2,
            center=Point(x=10, y=20))

    def test_it_has_an_updatable_center(self):
        self.rectangle.center |should| equal_to(Point(x=10, y=20))
        self.rectangle.center = Point(x=20, y=10)
        self.rectangle.center |should| equal_to(Point(x=20, y=10))

    def test_it_has_four_vertices(self):
        self.rectangle |should| have(4).vertices
        self.rectangle.vertices() |should| include_all_of([
            Point(x=7, y=18), Point(x=13, y=18),
            Point(x=7, y=22), Point(x=13, y=22)])

    def test_it_updates_its_vertices_when_center_changes(self):
        self.rectangle.center = Point(x=9, y=19)
        self.rectangle.vertices() |should| include_all_of([
            Point(x=6, y=17), Point(x=12, y=17),
            Point(x=6, y=21), Point(x=12, y=21)])

    def test_it_knows_if_it_is_a_square(self):
        point = Point(1, 1)
        CartesianRectangle(width=3, height=2, center=point) |should_not| be_square
        CartesianRectangle(width=3, height=3, center=point) |should| be_square


class PointTest(unittest.TestCase):

    def test_it_has_x_and_y_values(self):
        point = Point(x=10, y=20)
        point.x |should| be(10)
        point.y |should| be(20)

    def test_it_is_comparable_to_another_point(self):
        Point(x=10, y=20) |should| equal_to(Point(x=10, y=20))
        Point(x=11, y=20) |should_not| equal_to(Point(x=10, y=20))
        Point(x=10, y=21) |should_not| equal_to(Point(x=10, y=20))

