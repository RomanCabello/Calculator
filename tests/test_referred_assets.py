# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from calculator import MonthlyGuests
from calculator import ReferredAssets


class TestReferredAssets(TestCase):
    def test_calculate(self):
        monthly_guests_value = Decimal(6)
        period = Decimal(1)
        guest_average = Decimal(150000)

        monthly_guests = MagicMock(MonthlyGuests)
        monthly_guests.calculate = Mock()
        monthly_guests.calculate.return_value = monthly_guests_value

        referred_assets = ReferredAssets(monthly_guests,
                                         period,
                                         guest_average)
        self.assertEqual(referred_assets.calculate().quantize(Decimal('.0001')),
                         Decimal(900000))
