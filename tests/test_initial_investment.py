# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase

from calculator import InitialInvestment


class TestInitialInvestment(TestCase):
    def test_calculate_first(self):
        initial_amount = Decimal(1000)
        monthly_contribution = Decimal(1000)

        initial_investment = InitialInvestment(monthly_contribution)

        assert initial_investment.calculate_first(initial_amount) == Decimal(1000)

    def test_calculate_reinvest(self):
        monthly_contribution = Decimal(1000)
        previous_final_balance = Decimal(994.43)

        initial_investment = InitialInvestment(monthly_contribution)
        initial_investment_result = initial_investment.calculate_reinvest(previous_final_balance)

        self.assertEqual(initial_investment_result.quantize(Decimal('.0001')),
                         Decimal(1994.43).quantize(Decimal('.0001')))

    def test_calculate_not_reinvest(self):
        monthly_contribution = Decimal(1000)
        previous_initial_investment_interests = Decimal(1003.33)

        initial_investment = InitialInvestment(monthly_contribution)
        initial_investment_result = initial_investment.calculate_not_reinvest(previous_initial_investment_interests)

        self.assertEqual(initial_investment_result.quantize(Decimal('.0001')),
                         Decimal('2003.33').quantize(Decimal('.0001')))
