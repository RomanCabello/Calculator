# -*- coding: utf-8 -*-


from decimal import Decimal

from calculator import AnnualGuests
from calculator import MonthlyGuests
from calculator import MonthlyObjective
from calculator import SowosCalculator
from calculator import SharedCommission
from calculator import Percentage
from calculator import Points
from calculator import TotalAssets
from calculator import TotalGuests

if __name__ == '__main__':
    annual_objective = Decimal(100000)
    guest_average = Decimal(150000)
    initial_amount = Decimal(1000)
    monthly_contribution = Decimal(1000)
    phase1_years = Decimal(5)
    membership_cost = Decimal(-200)
    years = 10
    reinvest_profits = True
    kuspit_commission = Percentage(Decimal(0.63))
    shared_commission = SharedCommission(kuspit_commission, Decimal(30))
    monthly_objective = MonthlyObjective(annual_objective)
    total_assets = TotalAssets(monthly_objective, shared_commission)
    total_guests = TotalGuests(total_assets, guest_average)
    interest_rate = Percentage(Decimal(4))
    annual_guests = AnnualGuests(total_guests, Decimal(years))
    monthly_guests = MonthlyGuests(annual_guests)
    points = Points()

    calculator = SowosCalculator(annual_objective,
                                 guest_average,
                                 initial_amount,
                                 shared_commission,
                                 kuspit_commission,
                                 monthly_objective,
                                 total_assets,
                                 total_guests,
                                 phase1_years,
                                 interest_rate,
                                 annual_guests,
                                 monthly_guests,
                                 monthly_contribution,
                                 reinvest_profits,
                                 membership_cost,
                                 points)

    periods = calculator.generate_period_list(years)
    for period in periods:
        period.display()
