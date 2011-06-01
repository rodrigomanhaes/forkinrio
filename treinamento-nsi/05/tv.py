class TV(object):

    def __init__(self, channels=[1], volume_range=(0, 10)):
        self._on = False
        self._channels = channels
        self._channel = channels[0]
        self._volume_range = volume_range
        self._volume = self._volume_range[0]

    @property
    def is_on(self):
        return self._on

    def turn_on(self):
        self._on = True

    def turn_off(self):
        self._on = False

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, number):
        if number not in self._channels:
            raise InvalidChannel()
        self._channel = number

    @property
    def volume(self):
        return self._volume

    def increase_volume(self):
        if self._volume < self._volume_range[1]:
            self._volume += 1

    def decrease_volume(self):
        if self._volume > self._volume_range[0]:
            self._volume -= 1



class InvalidChannel(Exception):
    pass

