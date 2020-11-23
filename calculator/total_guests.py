# -*- coding: utf-8 -*-


from decimal import *
from calculator.total_assets import TotalAssets


class TotalGuests:
    def __init__(self, total_assets: TotalAssets, guest_average: Decimal):
        if not isinstance(total_assets, TotalAssets):
            raise ValueError(f"parameter total_assets: {total_assets} is not instance of TotalAssets")

        if not isinstance(guest_average, Decimal):
            raise ValueError(f"Parameter guest_average: {guest_average} is not instance of Decimal")

        self.__total_assets = total_assets
        self.__guest_average = guest_average

    def calculate(self):
        _total_assets = self.__total_assets.calculate()
        result = _total_assets / self.__guest_average
        return result
