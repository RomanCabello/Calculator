# -*- coding: utf-8 -*-


from decimal import Decimal


class Phase:
    def __init__(self, period: Decimal, phase1_years: Decimal):
        self.__period = period
        self.__phase1_years = phase1_years

    def calculate(self):
        periods_per_year = Decimal(12)
        if self.__period <= periods_per_year * self.__phase1_years:
            return 1

        return 2
