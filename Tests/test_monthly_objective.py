import unittest
from unittest.mock import MagicMock, call, patch

from calculator.monthly_objective import *


class TestMonthlyObjective(unittest.TestCase):
    def test_calculate(self):
        result = MonthlyObjective(Decimal(12)).calculate()
        self.assertEqual(result, Decimal(1))
