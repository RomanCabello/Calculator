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

