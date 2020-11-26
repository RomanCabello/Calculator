# -*- coding: utf-8 -*-


from decimal import Decimal

from .percentage import Percentage


class InitialInvestmentInterests:
    def __init__(self,
                 initial_investment: Decimal,
                 interest_rate: Percentage):
        self.__initial_investment = initial_investment
        self.__interest_rate = interest_rate

    def calculate(self):
        _initial_investment = self.__initial_investment
        _interest_rate = self.__interest_rate.calculate()
        result = _initial_investment * (Decimal(1) + (_interest_rate / Decimal(12)))
        return result
