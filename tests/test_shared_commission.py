# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from calculator import Percentage
from calculator import SharedCommission


class TestSharedCommission(TestCase):
    def test_shared_commission_calculation(self):
        sowos_commission = Decimal(200)
        percentage_result = Decimal(5)

        percentage= MagicMock(Percentage)
        percentage.calculate = Mock()
        percentage.calculate.return_value = percentage_result

        shared_commission = SharedCommission(percentage, sowos_commission)
        assert shared_commission.calculate() == Decimal(10)
