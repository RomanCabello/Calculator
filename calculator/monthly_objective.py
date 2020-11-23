# -*- coding: utf-8 -*-


from decimal import Decimal


class MonthlyObjective:
    def __init__(self, annual_objective: Decimal):
        if not isinstance(annual_objective, Decimal):
            raise ValueError(f"Parameter annual_objective: {annual_objective} is not an instance of Decimal")

        self.__annual_objective = annual_objective

    def calculate(self):
        result = Decimal(self.__annual_objective) / Decimal(12)
        return result
