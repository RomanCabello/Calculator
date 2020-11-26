# -*- coding: utf-8 -*-


from decimal import Decimal

from .percentage import Percentage


class SharedCommission:
    def __init__(self, kuspit_commission: Percentage, sowos_commission: Decimal):
        if not isinstance(kuspit_commission, Percentage):
            raise ValueError(f"Parameter kuspit_commission: {kuspit_commission} is not an instance of Percentage")

        if not isinstance(sowos_commission, Decimal):
            raise ValueError(f"Parameter sowos_commission: {sowos_commission} is not an instance of Decimal")

        self.__kuspit_commission = kuspit_commission
        self.__sowos_commission = sowos_commission

    def calculate(self):
        _kuspit_commission = self.__kuspit_commission.calculate()
        result = _kuspit_commission * self.__sowos_commission / Decimal(100)
        return result
