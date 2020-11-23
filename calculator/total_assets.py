# -*- coding: utf-8 -*-


from decimal import *
from calculator.monthly_objective import MonthlyObjective
from calculator.shared_commission import SharedCommission


class TotalAssets:
    def __init__(self, monthly_objective: MonthlyObjective, shared_commission: SharedCommission):
        if not isinstance(monthly_objective, MonthlyObjective):
            raise ValueError(f"Parameter monthly_objective: {monthly_objective} is not an instance of MonthlyObjective")

        if not isinstance(shared_commission, SharedCommission):
            raise ValueError(f"Parameter shared_commission: {shared_commission} is not an instance of SharedCommission")

        self.__monthly_objective = monthly_objective
        self.__shared_commission = shared_commission

    def calculate(self):
        _monthly_objective = self.__monthly_objective.calculate()
        _shared_commission = self.__shared_commission.calculate()
        result = _monthly_objective / (_shared_commission / Decimal(12))
        return result
