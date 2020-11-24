# -*- coding: utf-8 -*-


from decimal import Decimal


class Phase:
    def __init__(self, period: Decimal, years: Decimal):
        self.__period = period
        self.__years = years

    def calculate(self):
        periods_per_year = Decimal(12)
        if self.__period <= periods_per_year * self.__years:
            return 1

        return 2
