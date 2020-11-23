# -*- coding: utf-8 -*-


from decimal import *
from calculator.percentage import Percentage

class SharedCommission:
    def __init__(self, kuspit_commission: Percentage, sowos_commission: Decimal):
        self.__kuspit_commission = kuspit_commission
        self.__sowos_commission = sowos_commission

    def calculate(self):
        _kuspit_commission = self.__kuspit_commission.calculate()
        result = _kuspit_commission * self.__sowos_commission / Decimal(100)
        return result
