# -*- coding: utf-8 -*-


from decimal import Decimal

from .accumulated_profits import AccumulatedProfits
from .annual_guests import AnnualGuests
from .final_balance import FinalBalance
from .initial_investment import InitialInvestment
from .initial_investment_interests import InitialInvestmentInterests
from .interests import Interests
from .monthly_guests import MonthlyGuests
from .monthly_objective import MonthlyObjective
from .monthly_profits import MonthlyProfits
from .percentage import Percentage
from .period import Period
from .phase import Phase
from .points import Points
from .profits_via_referrals import ProfitsViaReferrals
from .referred_assets import ReferredAssets
from .shared_commission import SharedCommission
from .total_assets import TotalAssets
from .total_guests import TotalGuests
from .total_interests import TotalInterests


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
                 phase1_years: Decimal,
                 interest_rate: Percentage,
                 annual_guests: AnnualGuests,
                 monthly_guests: MonthlyGuests,
                 monthly_contribution: Decimal,
                 reinvest_profits: bool,
                 membership_cost: Decimal,):
        self.__annual_objective = annual_objective
        self.__guest_average = guest_average
        self.__initial_amount = initial_amount
        self.__kuspit_commission = kuspit_commission
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

    def generate_period_list(self, years: int):
        periods = []

        period_number = Decimal(1)

        points = Points()
        points_value = points.calculate()

        phase = Phase(period_number,
                      self.__phase1_years)
        phase_value = phase.calculate()

        initial_investment = InitialInvestment(self.__monthly_contribution)
        initial_investment_value = initial_investment.calculate_first(self.__initial_amount)

        initial_investment_interests = InitialInvestmentInterests(initial_investment_value,
                                                                  self.__interest_rate, )
        initial_investment_interests_value = initial_investment_interests.calculate()

        profits_via_referrals = ProfitsViaReferrals(self.__monthly_guests,
                                                    self.__guest_average,
                                                    period_number,
                                                    self.__shared_commission)
        profits_via_referrals_value = profits_via_referrals.calculate()

        interests = Interests(profits_via_referrals_value,
                              self.__interest_rate)
        interests_value = interests.calculate()

        total_interests = TotalInterests(initial_investment_interests,
                                         interests,
                                         initial_investment_value,
                                         profits_via_referrals_value, )
        total_interests_value = total_interests.calculate()

        final_balance = FinalBalance(initial_investment_interests,
                                     interests,
                                     points,
                                     self.__membership_cost)
        final_balance_value = final_balance.calculate()

        monthly_profits = MonthlyProfits(initial_investment_interests,
                                         interests,
                                         points,
                                         initial_investment_value)
        monthly_profits_value = monthly_profits.calculate()

        accumulated_profits = AccumulatedProfits(monthly_profits)
        accumulated_profits_value = accumulated_profits.calculate_first()

        referred_assets = ReferredAssets(self.__monthly_guests,
                                         period_number,
                                         self.__guest_average)
        referred_assets_value = referred_assets.calculate()

        period = Period(phase_value,
                        period_number,
                        initial_investment_value,
                        initial_investment_interests_value,
                        profits_via_referrals_value,
                        interests_value,
                        self.__membership_cost,
                        points_value,
                        total_interests_value,
                        final_balance_value,
                        monthly_profits_value,
                        accumulated_profits_value,
                        referred_assets_value)

        periods.append(period)

        previous_accumulated_profits = accumulated_profits_value
        previous_final_balance = final_balance_value
        previous_initial_investment_interests = initial_investment_interests_value
        previous_interests = interests_value

        total_periods = years * 12

        for month in range(1, total_periods):
            period_number += Decimal(1)

            phase = Phase(period_number,
                          self.__phase1_years)
            phase_value = phase.calculate()

            if self.__reinvest_profits:
                initial_investment_value = initial_investment.calculate_reinvest(previous_final_balance)

            if not self.__reinvest_profits:
                initial_investment_value =\
                    initial_investment.calculate_not_reinvest(previous_initial_investment_interests)

            initial_investment_interests = InitialInvestmentInterests(initial_investment_value,
                                                                      self.__interest_rate)
            initial_investment_value = initial_investment_interests.calculate()

            profits_via_referrals = ProfitsViaReferrals(self.__monthly_guests,
                                                        self.__guest_average,
                                                        period_number,
                                                        self.__shared_commission)
            if phase_value == 1:
                profits_via_referrals_value = profits_via_referrals.calculate()

            if phase_value == 2:
                profits_via_referrals_value = profits_via_referrals.calculate_phase_two(previous_interests)

            interests = Interests(profits_via_referrals_value,
                                  self.__interest_rate)
            interests_value = interests.calculate()

            total_interests = TotalInterests(initial_investment_interests,
                                             interests,
                                             initial_investment_value,
                                             profits_via_referrals_value)
            total_interests_value = total_interests.calculate()

            final_balance = FinalBalance(initial_investment_interests,
                                         interests,
                                         points,
                                         self.__membership_cost)
            final_balance_value = final_balance.calculate()

            monthly_profits = MonthlyProfits(initial_investment_interests,
                                             interests,
                                             points,
                                             initial_investment_value)
            monthly_profits_value = monthly_profits.calculate()

            accumulated_profits = AccumulatedProfits(monthly_profits)
            accumulated_profits_value = accumulated_profits.calculate(previous_accumulated_profits)

            referred_assets = ReferredAssets(self.__monthly_guests,
                                             period_number,
                                             self.__guest_average)
            referred_assets_value = referred_assets.calculate()

            period = Period(phase_value,
                            period_number,
                            initial_investment_value,
                            initial_investment_interests_value,
                            profits_via_referrals_value,
                            interests_value,
                            self.__membership_cost,
                            points_value,
                            total_interests_value,
                            final_balance_value,
                            monthly_profits_value,
                            accumulated_profits_value,
                            referred_assets_value)
            periods.append(period)

            previous_accumulated_profits = accumulated_profits_value
            previous_final_balance = final_balance_value
            previous_initial_investment_interests = initial_investment_interests_value
            previous_interests = interests_value

        return periods
