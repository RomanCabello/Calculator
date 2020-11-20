import unittest

from calculator.percentage import *


class TestPercentage(unittest.TestCase):
    def test_calculate(self):
        result = Percentage(Decimal(100)).calculate()
        self.assertEqual(result, Decimal(1))
