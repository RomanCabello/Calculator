# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from calculator import AccumulatedProfits
from calculator import MonthlyProfits


class TestAccumulatedProfits(TestCase):
    def test_calculate_first(self):
        monthly_profits_value = Decimal(194.43)

        monthly_profits = MagicMock(MonthlyProfits)
        monthly_profits.calculate = Mock()
        monthly_profits.calculate.return_value = monthly_profits_value

        accumulated_profits = AccumulatedProfits(monthly_profits)

        self.assertEqual(accumulated_profits.calculate_first().quantize(Decimal('.0001')),
                         monthly_profits_value.quantize(Decimal('.0001')))

    def test_calculate(self):
        monthly_profits_value = Decimal(588.84)
        previous_accumulated_profits = Decimal(194.43)

        monthly_profits = MagicMock(MonthlyProfits)
        monthly_profits.calculate = Mock()
        monthly_profits.calculate.return_value = monthly_profits_value

        accumulated_profits = AccumulatedProfits(monthly_profits)
        accumulated_profits_result = accumulated_profits.calculate(previous_accumulated_profits)

        self.assertEqual(accumulated_profits_result.quantize(Decimal('.0001')),
                         Decimal(783.27).quantize(Decimal('.0001')))
