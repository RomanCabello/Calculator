#!/usr/bin/env python
from decimal import *
from calculator.monthly_objective import MonthlyObjective
from calculator.shared_commission import SharedCommission


class TotalAssets:
    def __init__(self, monthly_objective: MonthlyObjective, shared_commission: SharedCommission):
        self.__monthly_objective = monthly_objective.calculate()
        self.__shared_commission = shared_commission.calculate()

    def calculate(self):
        result = self.__monthly_objective / (self.__shared_commission / Decimal(12))
        return result
