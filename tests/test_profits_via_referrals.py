# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from calculator import MonthlyGuests
from calculator import ProfitsViaReferrals
from calculator import SharedCommission


class TestProfitViaReferrals(TestCase):
    def test_calculation(self):
        period = Decimal(1)
        guest_average = Decimal(150000)
        monthly_guest_value = Decimal(6)
        shared_commission_value = Decimal(.0019)

        monthly_guests = MagicMock(MonthlyGuests)
        monthly_guests.calculate = Mock()
        monthly_guests.calculate.return_value = monthly_guest_value

        shared_commission = MagicMock(SharedCommission)
        shared_commission.calculate = Mock()
        shared_commission.calculate.return_value = shared_commission_value

        profits_via_referrals = ProfitsViaReferrals(monthly_guests,
                                                    guest_average,
                                                    period,
                                                    shared_commission)

        assert profits_via_referrals.calculate().quantize(Decimal('.0001')) == Decimal(142.5)

    def test_phase2_calculate(self):
        period = Decimal(1)
        guest_average = Decimal(150000)
        monthly_guest_value = Decimal(6)
        shared_commission_value = Decimal(.0019)
        previous_interests = Decimal(4500)

        monthly_guests = MagicMock(MonthlyGuests)
        monthly_guests.calculate = Mock()
        monthly_guests.calculate.return_value = monthly_guest_value

        shared_commission = MagicMock(SharedCommission)
        shared_commission.calculate = Mock()
        shared_commission.calculate.return_value = shared_commission_value

        profits_via_referrals = ProfitsViaReferrals(monthly_guests,
                                                    guest_average,
                                                    period,
                                                    shared_commission)
        assert profits_via_referrals.calculate_phase_two(previous_interests) == previous_interests
