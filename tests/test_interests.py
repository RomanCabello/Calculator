# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from calculator import Interests
from calculator import Percentage


class TestInterests(TestCase):
    def test_calculate(self):
        percentage_value = Decimal(.04)
        profits_via_referrals = Decimal(140.6300)

        percentage = MagicMock(Percentage)
        percentage.calculate = Mock()
        percentage.calculate.return_value = percentage_value

        interests = Interests(profits_via_referrals, percentage)

        self.assertEqual(interests.calculate().quantize(Decimal('.0001')),
                         Decimal(141.0988).quantize(Decimal('.0001')))
