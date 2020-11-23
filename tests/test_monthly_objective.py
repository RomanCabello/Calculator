# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase

from calculator import MonthlyObjective


class TestMonthlyObjective(TestCase):
    def test_monthly_objective_calculation(self):
        annual_objective = Decimal(12)

        monthly_objective = MonthlyObjective(annual_objective)
        assert monthly_objective.calculate() == Decimal(1)
