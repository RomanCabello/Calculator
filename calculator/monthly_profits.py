# -*- coding: utf-8 -*-


from decimal import Decimal

from .initial_investment_interests import InitialInvestmentInterests
from .interests import Interests
from .points import Points


class MonthlyProfits:
    def __init__(self,
                 initial_investment_interests: InitialInvestmentInterests,
                 interests: Interests,
                 points: Points,
                 initial_investment: Decimal):
        if not isinstance(initial_investment_interests, InitialInvestmentInterests):
            raise ValueError(f"Parameter initial_investment_interests: {initial_investment_interests} is not"
                             f"an instance of InitialInvestmentInterests")

        if not isinstance(interests, Interests):
            raise ValueError(f"Parameter interests: {interests} is not an instance of Interests")

        if not isinstance(points, Points):
            raise ValueError(f"Parameter points: {points} is not an instance of Points")

        if not isinstance(initial_investment, Decimal):
            raise ValueError(f"Parameter initial_investment: {initial_investment} is not an instance of Decimal")

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
