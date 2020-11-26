# -*- coding: utf-8 -*-


from decimal import Decimal

from .annual_guests import AnnualGuests


class MonthlyGuests:
    def __init__(self, annual_guests: AnnualGuests):
        if not isinstance(annual_guests, AnnualGuests):
            raise ValueError(f"Parameter annual_guests: {annual_guests} is not an instance of AnnualGuests")

        self.__annual_guests = annual_guests

    def calculate(self):
        _annual_guests = self.__annual_guests.calculate()
        result = _annual_guests / Decimal(12)
        return result
