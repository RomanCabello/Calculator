import unittest
from unittest.mock import call, patch, MagicMock
from calculator.annual_guests import *


class TestAnnualGuests(unittest.TestCase):
    def test_total_guests_call(self):
        total_guests_call_function = MagicMock(TotalGuests)
        AnnualGuests(total_guests_call_function, Decimal(5)).calculate()
        calls = [call.calculate(),
                 call.calculate().__truediv__(Decimal('5'))]
        total_guests_call_function.assert_has_calls(calls)

    @patch('calculator.total_guests.TotalGuests.calculate', return_value=Decimal(355.56))
    @patch('calculator.total_guests.TotalGuests')
    def test_calculate(self, total_guests_fake, calculate_fake):
        result = AnnualGuests(total_guests_fake, Decimal(5)).calculate()
        self.assertEqual(result.quantize(Decimal('.01')), Decimal(71.11).quantize(Decimal('.01')))
