import unittest
from unittest.mock import MagicMock, call, patch
from calculator.monthly_guests import *


class TestMonthlyGuests(unittest.TestCase):
    def test_annual_guests_call(self):
        annual_guest_call_function = MagicMock(AnnualGuests)
        MonthlyGuests(annual_guest_call_function).calculate()
        calls = [call.calculate(),
                 call.calculate().__truediv__(Decimal('12'))]
        annual_guest_call_function.assert_has_calls(calls)

    @patch('calculator.annual_guests.AnnualGuests.calculate', return_value=Decimal(71.11))
    @patch('calculator.annual_guests.AnnualGuests')
    def test_calculate(self, annual_guests_fake, calculate_fake):
        result = MonthlyGuests(annual_guests_fake).calculate()
        self.assertEqual(result.quantize(Decimal('1')), Decimal(6).quantize(Decimal('1')))
