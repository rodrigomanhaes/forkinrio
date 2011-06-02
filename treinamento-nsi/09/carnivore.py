
class Carnivore(object):

    def __init__(self):
        self._stomach = []

    def eat(self, thing):
        self._stomach.append(thing)

    @property
    def stomach(self):
        return self._stomach

    def digest(self):
        if len(self._stomach) > 0:
            del self._stomach[0]

