# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from calculator import MonthlyObjective
from calculator import SharedCommission
from calculator import TotalAssets


class TestTotalAssets(TestCase):
    def test_total_assets_calculation(self):
        monthly_objective_result = Decimal(100)
        shared_commission_result = Decimal(24)

        shared_commission = MagicMock(SharedCommission)
        shared_commission.calculate = Mock()
        shared_commission.calculate.return_value = shared_commission_result

        monthly_objective = MagicMock(MonthlyObjective)
        monthly_objective.calculate = Mock()
        monthly_objective.calculate.return_value = monthly_objective_result

        total_assets = TotalAssets(monthly_objective, shared_commission)
        assert total_assets.calculate() == Decimal(50)
