import unittest
from should_dsl import should, should_not
from fuel_pump import FuelPump, InsufficientFuel

class FuelPumpTest(unittest.TestCase):

    def setUp(self):
        self.fuel_pump = FuelPump(capacity=5000, price_per_liter=3.00)

    def it_has_a_capacity(self):
        self.fuel_pump.capacity |should| equal_to(5000)

    def it_has_a_price_per_liter(self):
        self.fuel_pump.price_per_liter |should| close_to(3, delta=0.0001)

    def it_has_initially_zero_fuel(self):
        self.fuel_pump.fuel_count |should| close_to(0, delta=0.00001)

    def it_can_be_filled(self):
        self.fuel_pump.fill()
        self.fuel_pump.fuel_count |should| close_to(5000, delta=0.00001)

    def it_can_fuel_by_value(self):
        self.fuel_pump.fill()
        self.fuel_pump.fuel_by_value(90) |should| close_to(30.00, delta=0.0001)
        self.fuel_pump.fuel_count |should| close_to(4970, delta=0.0001)

    def it_raises_error_for_insufficient_fuel(self):
        self.fuel_pump.fill()
        (self.fuel_pump.fuel_by_value, 15001) |should| throw(InsufficientFuel)

    def it_can_fuel_by_liters(self):
        self.fuel_pump.fill()
        self.fuel_pump.fuel_by_liters(10) |should| close_to(30, delta=0.0001)
        self.fuel_pump.fuel_count |should| close_to(4990, delta=0.0001)

    def it_raises_error_for_insufficient_fuel(self):
        self.fuel_pump.fill()
        (self.fuel_pump.fuel_by_liters, 5001) |should| throw(InsufficientFuel)

