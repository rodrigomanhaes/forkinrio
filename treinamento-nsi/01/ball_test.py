import unittest
from should_dsl import should
from ball import Ball

class BallTest(unittest.TestCase):

    def setUp(self):
        self.ball = Ball(color='red')

    def test_it_has_a_color(self):
        self.ball.color |should| equal_to('red')

    def test_it_changes_its_color(self):
        self.ball.color = 'green'
        self.ball.color |should| equal_to('green')

