#!/usr/bin/env python
from decimal import *
from calculator.annual_guests import AnnualGuests


class MonthlyGuests:
    def __init__(self, annual_guests: AnnualGuests):
        self.__annual_guests = annual_guests.calculate()

    def calculate(self):
        result = Decimal(self.__annual_guests / Decimal(12)).quantize(Decimal('1.'))
        return result
