# -*- coding: utf-8 -*-


from decimal import Decimal

from calculator import MonthlyGuests


class ReferredAssets:
    def __init__(self,
                 monthly_guests: MonthlyGuests,
                 period: Decimal,
                 guest_average: Decimal):
        self.__monthly_guests = monthly_guests
        self.__period = period
        self.__guest_average = guest_average

    def calculate(self):
        _monthly_guests = self.__monthly_guests.calculate()

        result = self.__period * _monthly_guests * self.__guest_average
        return result
