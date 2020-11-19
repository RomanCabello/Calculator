#!/usr/bin/env python
from decimal import *


class InterestRate:
    def __init__(self, rate: Decimal):
        self.__rate = rate

    def calculate(self):
        result = self.__rate / Decimal(100)
        return result
