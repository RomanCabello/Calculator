# -*- coding: utf-8 -*-


from decimal import Decimal


class InitialInvestment:
    def __init__(self,
                 monthly_contribution: Decimal, ):
        if not isinstance(monthly_contribution, Decimal):
            raise ValueError(f"Parameter monthly_contribution: {monthly_contribution} is not an instance of Decimal")

        self.__monthly_contribution = monthly_contribution

    def calculate_first(self,
                        initial_amount: Decimal, ):
        return initial_amount

    def calculate_reinvest(self,
                           previous_final_balance: Decimal, ):
        result = previous_final_balance + self.__monthly_contribution
        return result

    def calculate_not_reinvest(self,
                               previous_initial_investment_interests: Decimal, ):
        result = previous_initial_investment_interests + self.__monthly_contribution
        return result
