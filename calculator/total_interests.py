# -*- coding: utf-8 -*-


from decimal import Decimal

from calculator import InitialInvestmentInterests
from calculator import Interests


class TotalInterests:
    def __init__(self,
                 initial_investment_interests: InitialInvestmentInterests,
                 interests: Interests,
                 initial_investment: Decimal,
                 profits_via_referrals: Decimal,):
        self.__initial_investment_interests = initial_investment_interests
        self.__interests = interests
        self.__initial_investment = initial_investment
        self.__profits_via_referrals = profits_via_referrals

    def calculate(self):
        _initial_investment_interests = self.__initial_investment_interests.calculate()
        _interests = self.__interests.calculate()

        result = (_initial_investment_interests - self.__initial_investment) + \
                 (_interests - self.__profits_via_referrals)
        return result
