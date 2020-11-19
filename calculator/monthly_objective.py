#!/usr/bin/env python
from decimal import *


class MonthlyObjective:
    def __init__(self, annual_objective: Decimal):
        self.__annual_objective = annual_objective

    def calculate(self):
        result = Decimal(self.__annual_objective) / Decimal(12)
        return result
