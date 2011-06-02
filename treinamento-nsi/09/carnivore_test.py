import unittest
from should_dsl import should
from carnivore import Carnivore


class CarnivoreTest(unittest.TestCase):

    def test_it_eats_anything(self):
        carnivore = Carnivore()
        carnivore.eat(1)
        carnivore.eat(map)
        carnivore.eat({'i am': 'uneatable'})
        carnivore.eat(object)
        carnivore.eat(range(100))
        carnivore.eat(carnivore)
        carnivore.stomach |should| equal_to([
            1, map, {'i am': 'uneatable'}, object, range(100), carnivore])

    def test_it_digests_oldest_eaten_thing(self):
        carnivore = Carnivore()
        carnivore.eat(1)
        carnivore.eat(2)
        carnivore.eat(3)
        carnivore.digest()
        carnivore.stomach |should| equal_to([2, 3])
        carnivore.digest()
        carnivore.stomach |should| equal_to([3])
        carnivore.eat(4)
        carnivore.digest()
        carnivore.stomach |should| equal_to([4])

    def it_ignores_digestion_at_an_empty_stomach(self):
        carnivore = Carnivore()
        carnivore.stomach |should| be_empty
        carnivore.digest()
        carnivore.stomach |should| be_empty

