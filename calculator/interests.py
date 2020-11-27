# -*- coding: utf-8 -*-


from decimal import Decimal

from .percentage import Percentage


class Interests:
    def __init__(self,
                 profits_via_referrals: Decimal,
                 interest_rate: Percentage,):
        if not isinstance(profits_via_referrals, Decimal):
            raise ValueError(f"Parameter profits_via_referrals: {profits_via_referrals} is not an instance of Decimal")

        if not isinstance(interest_rate, Percentage):
            raise ValueError(f"Parameter interest_rate: {interest_rate} is not an instance of Percentage")

        self.__interest_rate = interest_rate
        self.__profits_via_referrals = profits_via_referrals

    def calculate(self):
        _profits_via_referrals = self.__profits_via_referrals
        _interest_rate = self.__interest_rate.calculate()
        result = _profits_via_referrals * (Decimal(1) + _interest_rate / Decimal(12))
        return result
