class FuelPump(object):

    def __init__(self, capacity, price_per_liter):
        self._capacity = capacity
        self._price_per_liter = price_per_liter
        self._fuel_count = 0

    @property
    def capacity(self):
        return self._capacity

    @property
    def price_per_liter(self):
        return self._price_per_liter

    @property
    def fuel_count(self):
        return self._fuel_count

    def fill(self):
        self._fuel_count = self._capacity

    def fuel_by_value(self, value):
        liters = value / self._price_per_liter
        if liters > self._fuel_count:
            raise InsufficientFuel()
        self._fuel_count -= liters
        return liters

    def fuel_by_liters(self, liters):
        if liters > self._fuel_count:
            raise InsufficientFuel()
        self._fuel_count -= liters
        return liters * self._price_per_liter


class InsufficientFuel(Exception):
    pass

