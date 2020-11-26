# -*- coding: utf-8 -*-


from decimal import Decimal

from .monthly_guests import MonthlyGuests
from .shared_commission import SharedCommission


class ProfitsViaReferrals:
    def __init__(self,
                 monthly_guests: MonthlyGuests,
                 guest_average: Decimal,
                 period: Decimal,
                 shared_commission: SharedCommission,):
        self.__monthly_guests = monthly_guests
        self.__guest_average = guest_average
        self.__period = period
        self.__shared_commission = shared_commission

    def calculate(self):
        _monthly_guests = self.__monthly_guests.calculate()
        _shared_commission = self.__shared_commission.calculate()

        result = _monthly_guests * self.__guest_average * self.__period * _shared_commission / Decimal(12)
        return result

    def calculate_phase_two(self, previous_interests: Decimal):
        return previous_interests
