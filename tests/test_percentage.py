# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase

from calculator import Percentage


class TestPercentage(TestCase):
    def test_percentage_calculation(self):
        percent = Decimal(100)

        percentage = Percentage(percent)
        assert percentage.calculate() == Decimal(1)
