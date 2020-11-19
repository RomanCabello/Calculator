#!/usr/bin/env python
from decimal import *
from calculator.total_guests import TotalGuests


class AnnualGuests:
    def __init__(self, total_guests: TotalGuests, years: Decimal):
        self.__total_guests = total_guests.calculate()
        self.__years = years

    def calculate(self):
        result = self.__total_guests / self.__years
        return result
