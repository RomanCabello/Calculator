#!/usr/bin/env python
from decimal import *
from calculator.kuspit import Kuspit

class SharedCommission:
    def __init__(self, kuspit: Kuspit, percent: Decimal):
        self.__kuspit = kuspit.calculate()
        self.__percent = percent

    def calculate(self):
        result = Decimal(self.__kuspit) * Decimal(self.__percent / Decimal(100))
        return result
