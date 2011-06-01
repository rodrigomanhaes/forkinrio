class Person(object):

    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height

    def birthday(self):
        if self.age < 21:
            self.height += 0.10
        self.age += 1

    def fatten(self, count):
        self.weight += count

    def thin(self, count):
        self.weight -= count

