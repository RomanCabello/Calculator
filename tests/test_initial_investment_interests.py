# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from calculator import InitialInvestmentInterests
from calculator import Percentage


class TestInitialInvestmentInterests(TestCase):
    def test_calculate(self):
        initial_investment = Decimal(1000)
        interest_rate_value = Decimal(.04)

        interest_rate = MagicMock(Percentage)
        interest_rate.calculate = Mock()
        interest_rate.calculate.return_value = interest_rate_value

        initial_investment_interests = InitialInvestmentInterests(initial_investment, interest_rate)

        self.assertEqual(initial_investment_interests.calculate().quantize(Decimal('.0001')),
                         Decimal(1003.3333).quantize(Decimal('.0001')))
