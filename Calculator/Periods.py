#!/usr/bin/env python
from decimal import *


class Period:
    def __init__(self, _period, interest_rate, _years, reinvest_profits, monthly_contribution,
                 monthly_guests, guest_average, shared_commission, membership_cost, points,
                 previous_accumulated_profits=None, previous_interests=None, previous_final_balance=None,
                 previous_initial_investment_interests=None, initial_investment=None):
        self.__period = _period
        self.__initial_investment = initial_investment
        self.__interest_rate = interest_rate
        self.__years = _years
        self.__reinvest_profits = reinvest_profits
        self.__monthly_contribution = monthly_contribution
        self.__previous_final_balance = previous_final_balance
        self.__previous_initial_investment_interests = previous_initial_investment_interests
        self.__monthly_guests = monthly_guests
        self.__guest_average = guest_average
        self.__shared_commission = shared_commission
        self.__previous_interests = previous_interests
        self.__membership_cost = membership_cost
        self.__points = points
        self.__previous_accumulated_profits = previous_accumulated_profits

    def phase(self):
        if self.__period <= (12 * self.__years):
            return 1

        else:
            return 2

    def initial_investment(self):
        if self.__period == 1:
            return self.__initial_investment
        else:
            return self.reinvest_profits()

    def reinvest_profits(self):
        if self.__reinvest_profits:
            return self.__previous_final_balance + self.__monthly_contribution
        else:
            return self.__previous_initial_investment_interests + self.__monthly_contribution

    def initial_investment_interests(self):
        return self.initial_investment() * (1 + (self.__interest_rate / 12))

    def profits_via_referrals(self):
        if self.phase() == 1:
            return self.__monthly_guests * self.__guest_average * self.__period * self.__shared_commission / Decimal(12)
        else:
            return self.__previous_interests

    def interests(self):
        return self.profits_via_referrals() * (Decimal(1) + self.__interest_rate / Decimal(12))

    def total_interests(self):
        return (self.initial_investment_interests() - self.initial_investment()) + \
               (self.interests() - self.profits_via_referrals())

    def final_balance(self):
        return self.initial_investment_interests() + self.interests() + self.__membership_cost + self.__points

    def monthly_profits(self):
        return (self.initial_investment_interests() - self.initial_investment()) + self.interests() + self.__points

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
        previous_initial_investment_interests = self.initial_investment_interests()
        next = Period(period, interest_rate, years, reinvest_profits, monthly_contribution, monthly_guests,
                      guest_average, shared_commission, membership_cost, points, previous_accumulated_profits,
                      previous_interests, previous_final_balance, previous_initial_investment_interests)

        return next

    def display_period(self):
        print(f"period: {self.__period}\t")
        print(f"monthly profits: {self.monthly_profits().quantize(Decimal('.0001'))}")
        print(f"accumulated profits {self.accumulated_profits().quantize(Decimal('.0001'))}")
        print("\n")