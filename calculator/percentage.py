# -*- coding: utf-8 -*-


from decimal import *


class Percentage:
    def __init__(self, percent: Decimal):
        self.__percent = percent

    def calculate(self):
        result = self.__percent / Decimal(100)
        return result
