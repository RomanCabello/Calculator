# -*- coding: utf-8 -*-


from decimal import Decimal

from .total_guests import TotalGuests


class AnnualGuests:
    def __init__(self, total_guests: TotalGuests, years: Decimal):
        if not isinstance(total_guests, TotalGuests):
            raise ValueError(f"Parameter total_guests: {total_guests} is not an instance of TotalGuests")

        if not isinstance(years, Decimal):
            raise ValueError(f"Parameter years: {years} is not an instance of Decimal")

        self.__total_guests = total_guests
        self.__years = years

    def calculate(self):
        _total_guests = self.__total_guests.calculate()
        result = _total_guests / self.__years
        return result
