# -*- coding: utf-8 -*-


from calculator.period import *
from calculator.percentage import Percentage
from calculator.shared_commission import SharedCommission
from calculator.monthly_objective import MonthlyObjective
from calculator.total_assets import TotalAssets
from calculator.total_guests import TotalGuests
from calculator.annual_guests import AnnualGuests
from calculator.monthly_guests import MonthlyGuests
from calculator.points import Points


class SowosCalculator:
    def __init__(self,
                 annual_objective: Decimal,
                 guest_average: Decimal,
                 initial_investment: Decimal,
                 shared_commission: SharedCommission,
                 kuspit_commission: Percentage,
                 monthly_objective: MonthlyObjective,
                 total_assets: TotalAssets,
                 total_guests: TotalGuests,
                 years: Decimal,
                 phase1_years: Decimal,
                 interest_rate: Percentage,
                 annual_guests: AnnualGuests,
                 monthly_guests: MonthlyGuests,
                 monthly_contribution: Decimal,
                 reinvest_profits: bool,
                 membership_cost: Decimal,
                 points: Points):
        self.__annual_objective = annual_objective
        self.__guest_average = guest_average
        self.__initial_investment = initial_investment
        self.__kuspit_commission = kuspit_commission
        self.__years = years
        self.__interest_rate = interest_rate
        self.__shared_commission = shared_commission
        self.__monthly_objective = monthly_objective
        self.__total_assets = total_assets
        self.__total_guests = total_guests
        self.__annual_guests = annual_guests
        self.__monthly_guests = monthly_guests
        self.__monthly_contribution = monthly_contribution
        self.__reinvest_profits = reinvest_profits
        self.__membership_cost = membership_cost
        self.__phase1_years = phase1_years
        self.__points = points

    def generate_periods(self, years):
        number_of_periods = int(years * 12)

        periods = []

        initial_investment_variable = initial_investment(1,
                                                         self.__reinvest_profits,
                                                         self.__monthly_contribution,
                                                         initial_amount=self.__initial_investment)

        profits_via_referrals_variable = profits_via_referrals()

        first_period = PeriodFactory(1, phase(1, self.__phase1_years), self.__interest_rate, self.__phase1_years,
                                     self.__reinvest_profits, self.__monthly_contribution, self.__monthly_guests,
                                     self.__guest_average, self.__shared_commission, self.__membership_cost,
                                     self.__points, initial_investment_interests(initial_investment_variable,
                                                                                 self.__interest_rate),
                                     initial_investment=initial_investment_variable)
        periods.append(first_period)
        first_period.display_period()

        for period in range(1, number_of_periods):
            past_period = period - 1
            next_period = periods[past_period].create_next()
            periods.append(next_period)
            next_period.display_period()
