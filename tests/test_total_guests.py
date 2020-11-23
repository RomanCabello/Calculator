# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from calculator import TotalAssets
from calculator import TotalGuests


class TestTotalGuests(TestCase):
    def test_total_guests_calculation(self):
        guest_average = Decimal(5)
        total_assets_result = Decimal(25)

        total_assets = MagicMock(TotalAssets)
        total_assets.calculate = Mock()
        total_assets.calculate.return_value = total_assets_result

        total_guests = TotalGuests(total_assets, guest_average)
        assert total_guests.calculate() == Decimal(5)
