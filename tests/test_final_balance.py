# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from calculator import FinalBalance
from calculator import InitialInvestmentInterests
from calculator import Interests
from calculator import Points


class TestFinalBalance(TestCase):
    def test_calculate(self):
        initial_investment_interests_value = Decimal(1003.3333)
        interests_value = Decimal(141.0900)
        points_value = Decimal(50)
        membership_cost = Decimal(-200)

        initial_investment_interests = MagicMock(InitialInvestmentInterests)
        initial_investment_interests.calculate = Mock()
        initial_investment_interests.calculate.return_value = initial_investment_interests_value

        interests = MagicMock(Interests)
        interests.calculate = Mock()
        interests.calculate.return_value = interests_value

        points = MagicMock(Points)
        points.calculate = Mock()
        points.calculate.return_value = points_value

        final_balance = FinalBalance(initial_investment_interests,
                                     interests,
                                     points,
                                     membership_cost)
        self.assertEqual(final_balance.calculate().quantize(Decimal('.0001')),
                         Decimal(994.4233).quantize(Decimal('.0001')))
