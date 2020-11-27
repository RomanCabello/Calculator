# -*- coding: utf-8 -*-


from decimal import Decimal

from .monthly_profits import MonthlyProfits


class AccumulatedProfits:
    def __init__(self,
                 monthly_profits: MonthlyProfits,):
        if not isinstance(monthly_profits, MonthlyProfits):
            raise ValueError(f"Parameter monthly_profits: {MonthlyProfits} is not an instance of MonthlyProfits")

        self.__monthly_profits = monthly_profits

    def calculate_first(self):
        _monthly_profits = self.__monthly_profits.calculate()
        return _monthly_profits

    def calculate(self, previous_accumulated_profits: Decimal):
        _monthly_profits = self.__monthly_profits.calculate()

        result = previous_accumulated_profits + _monthly_profits
        return result
