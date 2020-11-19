#!/usr/bin/env python
from decimal import *
from calculator.total_assests import TotalAssets


class TotalGuests:
    def __init__(self, total_assets: TotalAssets, guest_average: Decimal):
        self.__total_assets = total_assets.calculate()
        self.__guest_average = guest_average

    def calculate(self):
        result = self.__total_assets / self.__guest_average
        return result
