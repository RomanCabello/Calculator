# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from calculator import InitialInvestmentInterests
from calculator import Interests
from calculator import TotalInterests


class TestTotalInterests(TestCase):
    def test_calculate(self):
        initial_investment_interests_value = Decimal(1003.3333)
        interests_value = Decimal(141.0900)
        initial_investment = Decimal(1000)
        profits_via_referrals = Decimal(140.6300)

        initial_investment_interests = MagicMock(InitialInvestmentInterests)
        initial_investment_interests.calculate = Mock()
        initial_investment_interests.calculate.return_value = initial_investment_interests_value

        interests = MagicMock(Interests)
        interests.calculate = Mock()
        interests.calculate.return_value = interests_value

        total_interests = TotalInterests(initial_investment_interests,
                                         interests,
                                         initial_investment,
                                         profits_via_referrals)
        self.assertEqual(total_interests.calculate().quantize(Decimal('.0001')),
                         Decimal(3.7933).quantize(Decimal('.0001')))
