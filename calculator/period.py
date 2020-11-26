# -*- coding: utf-8 -*-


from decimal import Decimal


class Period:
    def __init__(self,
                 phase: Decimal,
                 period_number: Decimal,
                 initial_investment: Decimal,
                 initial_investment_interests: Decimal,
                 profits_via_referrals: Decimal,
                 interests: Decimal,
                 membership_cost: Decimal,
                 points: Decimal,
                 total_interests: Decimal,
                 final_balance: Decimal,
                 monthly_profits: Decimal,
                 accumulated_profits: Decimal,
                 referred_assets: Decimal):
        self.__phase = phase
        self.__period_number = period_number
        self.__initial_investment = initial_investment
        self.__initial_investment_interests = initial_investment_interests
        self.__profits_via_referrals = profits_via_referrals
        self.__interests = interests
        self.__membership_cost = membership_cost
        self.__points = points
        self.__total_interests = total_interests
        self.__final_balance = final_balance
        self.__monthly_profits = monthly_profits
        self.__accumulated_profits = accumulated_profits
        self.__referred_assets = referred_assets

    def get_phase(self):
        return self.__phase

    def get_period_number(self):
        return self.__period_number

    def get_initial_investment(self):
        return self.__initial_investment

    def get_initial_investment_interests(self):
        return self.__initial_investment_interests

    def get_profits_via_referrals(self):
        return self.__profits_via_referrals

    def get_interests(self):
        return self.__interests

    def get_membership_cost(self):
        return self.__membership_cost

    def get_points(self):
        return self.__points

    def get_total_interests(self):
        return self.__total_interests

    def get_final_balance(self):
        return self.__final_balance

    def get_monthly_profits(self):
        return self.__monthly_profits

    def get_accumulated_profits(self):
        return self.__accumulated_profits

    def get_referred_assets(self):
        return self.__referred_assets

    def display_summary(self):
        print("////////////////////////////////////////////////")
        print(f"Phase: {self.__phase}")
        print(f"Period number: {self.__period_number}")
        print(f"Initial investment: {self.__initial_investment.quantize(Decimal('.0001'))}")
        print(f"Initial investment interests: {self.__initial_investment_interests.quantize(Decimal('.0001'))}")
        print(f"Profits via referrals: {self.__profits_via_referrals.quantize(Decimal('.0001'))}")
        print(f"Interests: {self.__interests.quantize(Decimal('.0001'))}")
        print(f"Membership cost: {self.__membership_cost.quantize(Decimal('.0001'))}")
        print(f"Points: {self.__points.quantize(Decimal('.0001'))}")
        print(f"Total interests: {self.__total_interests.quantize(Decimal('.0001'))}")
        print(f"Final balance: {self.__final_balance.quantize(Decimal('.0001'))}")
        print(f"Monthly profits: {self.__monthly_profits.quantize(Decimal('.0001'))}")
        print(f"Accumulated_profits: {self.__accumulated_profits.quantize(Decimal('.0001'))}")
        print(f"Referred assets: {self.__referred_assets.quantize(Decimal('.0001'))}")
