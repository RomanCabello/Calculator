# -*- coding: utf-8 -*-


from decimal import Decimal


class Period:
    def __init__(self,
                 phase: Decimal,
                 period: Decimal,
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
        self.__period = period
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
