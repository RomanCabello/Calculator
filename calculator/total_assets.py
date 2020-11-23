# -*- coding: utf-8 -*-


from decimal import *
from calculator.monthly_objective import MonthlyObjective
from calculator.shared_commission import SharedCommission


class TotalAssets:
    def __init__(self, monthly_objective: MonthlyObjective, shared_commission: SharedCommission):
        self.__monthly_objective = monthly_objective
        self.__shared_commission = shared_commission

    def calculate(self):
        _monthly_objective = self.__monthly_objective.calculate()
        _shared_commission = self.__shared_commission.calculate()
        result = _monthly_objective / (_shared_commission / Decimal(12))
        return result
