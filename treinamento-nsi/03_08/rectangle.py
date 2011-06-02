class Rectangle(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2


class CartesianRectangle(Rectangle):

    def __init__(self, width, height, center):
        Rectangle.__init__(self, width, height)
        self.center = center

    def vertices(self):
        xcenter, ycenter = self.center.x, self.center.y
        width, height = self.width, self.height
        return [Point(xcenter - width, ycenter - height),
                 Point(xcenter - width, ycenter + height),
                 Point(xcenter + width, ycenter - height),
                 Point(xcenter + width, ycenter + height)]

    def is_square(self):
        return self.width == self.height



class Point(object):

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

