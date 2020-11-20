#!/usr/bin/env python
from decimal import *
from calculator.total_guests import TotalGuests


class AnnualGuests:
    def __init__(self, total_guests: TotalGuests, years: Decimal):
        self.__total_guests = total_guests
        self.__years = years

    def calculate(self):
        _total_guests = self.__total_guests.calculate()
        result = _total_guests / self.__years
        return result
