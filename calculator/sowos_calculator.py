# -*- coding: utf-8 -*-


from decimal import Decimal


from calculator import AccumulatedProfits
from calculator import AnnualGuests
from calculator import FinalBalance
from calculator import InitialInvestment
from calculator import InitialInvestmentInterests
from calculator import Interests
from calculator import MonthlyGuests
from calculator import MonthlyObjective
from calculator import MonthlyProfits
from calculator import Percentage
from calculator import Period
from calculator import Phase
from calculator import Points
from calculator import ProfitsViaReferrals
from calculator import ReferredAssets
from calculator import SharedCommission
from calculator import TotalAssets
from calculator import TotalGuests
from calculator import TotalInterests


class SowosCalculator:
    def __init__(self,
                 annual_objective: Decimal,
                 guest_average: Decimal,
                 initial_amount: Decimal,
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
        self.__initial_amount = initial_amount
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

    def add_period_list(self):
        items = []

    def generate_first_period(self):
        period = Decimal(1)
        points_value = self.__points.calculate()

        phase = Phase(period,
                      self.__phase1_years)
        phase_value = phase.calculate()

        initial_investment = InitialInvestment(self.__monthly_contribution)
        initial_investment_value = initial_investment.calculate_first(self.__initial_amount)

        initial_investment_interests = InitialInvestmentInterests(initial_investment_value,
                                                                  self.__interest_rate,)
        initial_investment_interests_value = initial_investment_interests.calculate()

        profits_vis_referrals = ProfitsViaReferrals(phase,
                                                    self.__monthly_guests,
                                                    self.__guest_average,
                                                    period,
                                                    self.__shared_commission)
        profits_vis_referrals_value = profits_vis_referrals.calculate()

        interests = Interests(profits_vis_referrals_value,
                              self.__interest_rate)
        interests_value = interests.calculate()

        total_interests = TotalInterests(initial_investment_interests,
                                         interests,
                                         initial_investment_value,
                                         profits_vis_referrals_value,)
        total_interests_value = total_interests.calculate()

        final_balance = FinalBalance(initial_investment_interests,
                                     interests,
                                     self.__points,
                                     self.__membership_cost)
        final_balance_value = final_balance.calculate()

        monthly_profits = MonthlyProfits(initial_investment_interests,
                                         interests,
                                         self.__points,
                                         initial_investment_value)
        monthly_profits_value = monthly_profits.calculate()

        accumulated_profits = AccumulatedProfits(monthly_profits)
        accumulated_profits_value = accumulated_profits.calculate_first()

        referred_assets = ReferredAssets(self.__monthly_guests, period, self.__guest_average)
        referred_assets_value = referred_assets.calculate()

        period = Period(phase_value,
                        period,
                        initial_investment_value,
                        initial_investment_interests_value,
                        profits_vis_referrals_value,
                        interests_value,
                        self.__membership_cost,
                        points_value,
                        total_interests_value,
                        final_balance_value,
                        monthly_profits_value,
                        accumulated_profits_value,
                        referred_assets_value)
        
