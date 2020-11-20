#!/usr/bin/env python
from decimal import *
from calculator.annual_guests import AnnualGuests


class MonthlyGuests:
    def __init__(self, annual_guests: AnnualGuests):
        self.__annual_guests = annual_guests

    def calculate(self):
        _annual_guests = self.__annual_guests.calculate()
        result = _annual_guests / Decimal(12)
        return result
