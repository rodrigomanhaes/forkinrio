import unittest
from should_dsl import should
from person import Person

class PersonTest(unittest.TestCase):

    def setUp(self):
        self.person = Person(age=25, weight=50, height=1.50)

    def test_it_has_age_weight_and_height(self):
        self.person.age |should| be(25)
        self.person.weight |should| equal_to(50)
        self.person.height |should| equal_to(1.50)

    def test_it_has_a_birthday(self):
        self.person.birthday()
        self.person.age |should| be(26)

    def test_it_grows_up_10_cm_at_each_birthday_if_under_21(self):
        person = Person(age=19, weight=50, height=1.50)
        person.birthday()
        person.age |should| be(20)
        person.height |should| close_to(1.60, delta=0.0001)

        person.birthday()
        person.age |should| be(21)
        person.height |should| close_to(1.70, delta=0.0001)

        person.birthday()
        person.age |should| be(22)
        person.height |should| close_to(1.70, delta=0.0001)

    def test_it_fattens(self):
        self.person.fatten(10)
        self.person.weight |should| equal_to(60)

    def test_it_thins(self):
        self.person.thin(10)
        self.person.weight |should| equal_to(40)

