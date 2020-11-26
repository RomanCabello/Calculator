# -*- coding: utf-8 -*-


from decimal import Decimal
from unittest import TestCase

from calculator import Phase


class TestPhase(TestCase):
    def test_calculate(self):
        period = Decimal(70)
        phase1_years = Decimal(5)

        phase = Phase(period, phase1_years)

        self.assertEqual(phase.calculate(), Decimal(2))
