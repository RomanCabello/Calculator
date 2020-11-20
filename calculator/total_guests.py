#!/usr/bin/env python
from decimal import *
from calculator.total_assets import TotalAssets


class TotalGuests:
    def __init__(self, total_assets: TotalAssets, guest_average: Decimal):
        self.__total_assets = total_assets
        self.__guest_average = guest_average

    def calculate(self):
        _total_assets = self.__total_assets.calculate()
        result = _total_assets / self.__guest_average
        return result
