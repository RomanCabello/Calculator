import unittest
from unittest.mock import MagicMock, patch, call

from calculator.shared_commission import *


class TestSharedCommission(unittest.TestCase):
    def test_percentage_call(self):
        percentage_call_function = MagicMock(Percentage)
        SharedCommission(percentage_call_function, Decimal(.3)).calculate()
        calls = [call.calculate(),
                 call.calculate().__mul__(Decimal(.3)),
                 call.calculate().__mul__().__truediv__(Decimal('100'))]
        percentage_call_function.assert_has_calls(calls)

    @patch('calculator.percentage.Percentage.calculate', return_value=Decimal(0.625))
    @patch('calculator.percentage.Percentage')
    def test_calculate(self, fake_percentage, fake_calculate):
        result = SharedCommission(fake_percentage, Decimal(.30)).calculate()
        self.assertEqual(result.quantize(Decimal('.0001')), Decimal(.0019).quantize(Decimal('.0001')))
