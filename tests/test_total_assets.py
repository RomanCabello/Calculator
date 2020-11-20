import unittest
from unittest.mock import MagicMock, call, patch

from calculator.total_assets import *


class TestTotalAssets(unittest.TestCase):
    def test_shared_commission_calls(self):
        shared_commission_call_function = MagicMock(SharedCommission)
        TotalAssets(MonthlyObjective(Decimal(12)), shared_commission_call_function).calculate()
        calls = [call.calculate(),
                 call.calculate().__truediv__(Decimal('12')),
                 call.calculate().__truediv__().__rtruediv__(Decimal('1'))
                 ]
        shared_commission_call_function.assert_has_calls(calls)

    @patch('calculator.percentage.Percentage')
    def test_monthly_objective_calls(self, fake_percentage):
        monthly_objective_call_function = MagicMock(MonthlyObjective)
        TotalAssets(monthly_objective_call_function, fake_percentage).calculate()
        calls = [call.calculate(),
                 call.calculate().__truediv__(fake_percentage.calculate().__truediv__())]
        monthly_objective_call_function.assert_has_calls(calls)

    @patch('calculator.monthly_objective.MonthlyObjective.calculate', return_value=Decimal(8333.33))
    @patch('calculator.monthly_objective.MonthlyObjective')
    @patch('calculator.shared_commission.SharedCommission.calculate', return_value=Decimal(0.0019))
    @patch('calculator.shared_commission.SharedCommission')
    def test_calculator(self, fake_shared_commission, fake_shared_commission_calculate, fake_monthly_objective, fake_monthly_objective_calculate):
        result = TotalAssets(fake_monthly_objective, fake_shared_commission).calculate()
        target = Decimal(8333.33)/(Decimal(.0019) / Decimal(12))
        self.assertEqual(result, target)