import unittest
from should_dsl import should, should_not
from tv import TV, InvalidChannel

class TvTest(unittest.TestCase):

    def test_it_can_be_turn_on(self):
        tv = TV()
        tv.turn_on()
        tv |should| be_on

    def test_it_can_be_turn_off(self):
        tv = TV()
        tv.turn_on()
        tv.turn_off()
        tv |should_not| be_on

    def test_it_allows_set_current_channel_within_a_given_range(self):
        tv = TV(channels=[1, 2, 3, 5])
        for channel in [1, 2, 3, 5]:
            tv.channel = channel
            tv.channel |should| be(channel)
        def set_channel(channel):
            tv.channel = channel
        (set_channel, 0) |should| throw(InvalidChannel)
        (set_channel, 4) |should| throw(InvalidChannel)
        (set_channel, 6) |should| throw(InvalidChannel)


class TvVolumeTest(unittest.TestCase):

    def setUp(self):
        self.tv = TV(volume_range=(0, 30))

    def test_it_starts_at_the_minimum(self):
        self.tv.volume |should| be(0)
        TV(volume_range=(10, 20)).volume |should| be(10)

    def test_it_increases(self):
        self.tv.increase_volume()
        self.tv.volume |should| be(1)
        self.tv.increase_volume()
        self.tv.volume |should| be(2)

    def test_it_decreases(self):
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.tv.volume |should| be(2)
        self.tv.decrease_volume()
        self.tv.volume |should| be(1)
        self.tv.decrease_volume()
        self.tv.volume |should| be(0)

    def test_it_does_nothing_when_trying_to_increase_beyond_the_maximum(self):
        for i in range(30):
            self.tv.increase_volume()
        self.tv.volume |should| be(30)
        self.tv.increase_volume()
        self.tv.volume |should| be(30)

    def test_it_does_nothing_when_trying_to_decrease_under_the_minimum(self):
        self.tv.volume |should| be(0)
        self.tv.decrease_volume()
        self.tv.volume |should| be(0)

