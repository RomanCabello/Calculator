# -*- coding: utf-8 -*-


from decimal import Decimal


class Percentage:
    def __init__(self, percent: Decimal):
        if not isinstance(percent, Decimal):
            raise ValueError(f"Parameter percent: {percent} is not an instance of Decimal.")

        self.__percent = percent

    def calculate(self):
        result = self.__percent / Decimal(100)
        return result
