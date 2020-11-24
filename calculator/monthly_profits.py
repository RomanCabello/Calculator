# -*- coding: utf-8 -*-


from decimal import Decimal

from calculator import InitialInvestmentInterests
from calculator import Interests
from calculator import Points


class MonthlyProfits:
    def __init__(self,
                 initial_investment_interests: InitialInvestmentInterests,
                 interests: Interests,
                 points: Points,
                 initial_investment: Decimal):
        self.__initial_investment_interests = initial_investment_interests
        self.__interests = interests
        self.__points = points
        self.__initial_investment = initial_investment

    def calculate(self):
        _initial_investment_interests = self.__initial_investment_interests.calculate()
        _interests = self.__interests.calculate()
        _points = self.__points.calculate()

        result = (_initial_investment_interests - self.__initial_investment) + _interests + _points
        return result
