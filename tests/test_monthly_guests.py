# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from calculator import AnnualGuests
from calculator import MonthlyGuests


class TestMonthlyGuests(TestCase):
    def test_monthly_guests_calculation(self):
        annual_guests_result = Decimal(12)

        annual_guests = MagicMock(AnnualGuests)
        annual_guests.calculate = Mock()
        annual_guests.calculate.return_value = annual_guests_result

        monthly_guests = MonthlyGuests(annual_guests)
        assert monthly_guests.calculate() == Decimal(1)
