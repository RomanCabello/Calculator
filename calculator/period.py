#!/usr/bin/env python
from decimal import *


def phase(period, years):
    if period <= (12 * years):
        return 1
    return 2


def initial_investment(period: int, reinvest_profits, monthly_contribution, previous_final_balance=None,
                       previous_initial_investment_interests=None, initial_amount=None):
    if period == 1:
        return initial_amount

    return reinvestment(reinvest_profits, previous_final_balance, monthly_contribution,
                        previous_initial_investment_interests)


def reinvestment(reinvest_profits, previous_final_balance, monthly_contribution,
                 previous_initial_investment_interests):
    if reinvest_profits:
        return previous_final_balance + monthly_contribution
    else:
        return previous_initial_investment_interests + monthly_contribution


def initial_investment_interests(initial_investment, interest_rate):
    return initial_investment * (Decimal(1) + (interest_rate / Decimal(12)))


def profits_via_referrals(phase: int, monthly_guests, guest_average, period, shared_commission,
                          previous_interests=None):
    if phase == 1:
        return monthly_guests * guest_average * period * shared_commission / Decimal(12)
    else:
        return previous_interests


class PeriodFactory:
    def __init__(self, period, phase, interest_rate, _years, reinvest_profits, monthly_contribution,
                 monthly_guests, guest_average, shared_commission, membership_cost, points, profits_via_referrals,
                 initial_investment_interests, previous_accumulated_profits=None, initial_investment=None):
        self.__period = _period
        self.__initial_investment = initial_investment
        self.__interest_rate = interest_rate
        self.__years = _years
        self.__reinvest_profits = reinvest_profits
        self.__monthly_contribution = monthly_contribution
        self.__monthly_guests = monthly_guests
        self.__guest_average = guest_average
        self.__shared_commission = shared_commission
        self.__membership_cost = membership_cost
        self.__points = points
        self.__previous_accumulated_profits = previous_accumulated_profits
        self.__phase = phase
        self.__initial_investment_interests = initial_investment_interests
        self.__profits_via_referrals = profits_via_referrals

    def interests(self):
        return self.__profits_via_referrals * (Decimal(1) + self.__interest_rate / Decimal(12))

    def total_interests(self):
        return (self.__initial_investment_interests - self.__initial_investment) + \
               (self.interests() - self.__profits_via_referrals)

    def final_balance(self):
        return self.__initial_investment_interests + self.interests() + self.__membership_cost + self.__points

    def monthly_profits(self):
        return (self.__initial_investment_interests - self.__initial_investment) + self.interests() + self.__points

    def accumulated_profits(self):
        if self.__period == 1:
            return self.monthly_profits()
        else:
            return self.__previous_accumulated_profits + self.monthly_profits()

    def referred_assets(self):
        return self.__period * self.__monthly_guests * self.__guest_average

    def create_next(self):  
        period = self.__period + 1
        interest_rate = self.__interest_rate
        years = self.__years
        reinvest_profits = self.__reinvest_profits
        monthly_contribution = self.__monthly_contribution
        monthly_guests = self.__monthly_guests
        guest_average = self.__guest_average
        shared_commission = self.__shared_commission
        membership_cost = self.__membership_cost
        points = self.__points
        previous_accumulated_profits = self.accumulated_profits()
        previous_interests = self.interests()
        previous_final_balance = self.final_balance()
        previous_initial_investment_interests = self.__initial_investment_interests

        initial_investment_variable = initial_investment(period, reinvest_profits, monthly_contribution,
                                                         previous_final_balance, previous_initial_investment_interests)

        profits_via_referrals_variable = profits_via_referrals(1, )

        next_period = PeriodFactory(period, phase(period, years), interest_rate, years, reinvest_profits,
                                    monthly_contribution,
                                    monthly_guests, guest_average, shared_commission, membership_cost, points,
                                    profits_via_referrals_variable,
                                    initial_investment_interests(initial_investment_variable, self.__interest_rate),
                                    previous_accumulated_profits, initial_investment_variable)

        return next_period

    def display_period(self):
        print(f"period: {self.__period}\t")
        print(f"monthly profits: {self.monthly_profits().quantize(Decimal('.0001'))}")
        print(f"accumulated profits {self.accumulated_profits().quantize(Decimal('.0001'))}")
        print("\n")
