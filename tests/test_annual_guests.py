# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from calculator import AnnualGuests
from calculator import TotalGuests


class TestAnnualGuests(TestCase):
    def test_total_guests_calculation(self):
        years = Decimal(5)
        total_guests_result = 10

        total_guests = MagicMock(TotalGuests)
        total_guests.calculate = Mock()
        total_guests.calculate.return_value = total_guests_result

        annual_guests = AnnualGuests(total_guests, years)
        assert annual_guests.calculate() == Decimal(2)
