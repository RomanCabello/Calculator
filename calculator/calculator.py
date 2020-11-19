#!/usr/bin/env python
from calculator.period import *
from calculator.interest_rate import InterestRate
from calculator.kuspit import Kuspit
from calculator.shared_commission import SharedCommission
from calculator.monthly_objective import MonthlyObjective
from calculator.total_assests import TotalAssets
from calculator.total_guests import TotalGuests
from calculator.annual_guests import AnnualGuests
from calculator.monthly_guests import MonthlyGuests

annual_objective = Decimal(input("Please enter your annual objective"))
guest_average = Decimal(input("Please enter the average investment of your guests"))
initial_amount = Decimal(input("Please enter the initial amount you will invest"))
monthly_contribution = Decimal(input("Please enter the amount you will be investing monthly"))
reinvest_profits = input("Would you like to automatically reinvest your profits? (Y/N)")
reinvest_profits = reinvest_profits == "Y"

years_to_calculate = Decimal(input("Please enter the amount of years you wish to calculate"))
duration_of_phase_1 = Decimal(input("Please enter the duration of phase 1 in years"))
membership_cost = Decimal(0) - Decimal(input("Please enter the membership cost"))




class Basics:
    def __init__(self, annual_objective: Decimal, guest_average: Decimal, initial_investment: Decimal, shared_commission: SharedCommission, kuspit: Kuspit,
                 monthly_objective: MonthlyObjective, total_assets: TotalAssets, total_guests: TotalGuests, years_to_calculate: Decimal, duration_of_phase_1: Decimal,
                 interest_rate: InterestRate, annual_guests: AnnualGuests,
                 monthly_guests: MonthlyGuests, monthly_contribution: Decimal, reinvest_profits: bool, membership_cost: Decimal, points: Decimal):
        self.__annual_objective = annual_objective
        self.__guest_average = guest_average
        self.__initial_investment = initial_investment
        self.__kuspit = kuspit.calculate()
        self.__years = years_to_calculate
        self.__interest_rate = interest_rate.calculate()
        self.__shared_commission = shared_commission.calculate()
        self.__monthly_objective = monthly_objective.calculate()
        self.__total_assets = total_assets.calculate()
        self.__total_guests = total_guests.calculate()
        self.__annual_guests = annual_guests.calculate()
        self.__monthly_guests = monthly_guests.calculate()
        self.__monthly_contribution = monthly_contribution
        self.__reinvest_profits = reinvest_profits
        self.__membership_cost = membership_cost
        self.__years_investment = duration_of_phase_1
        self.__points = points

    def display(self):
        print(f"Objetivo Anual: {self.__annual_objective.quantize(Decimal('.0001'), rounding=ROUND_HALF_EVEN)}")
        print(f"Promedio de Invitados: {self.__guest_average.quantize(Decimal('.0001'), rounding=ROUND_HALF_EVEN)} \n")
        print(f"objetivo mensual:\t\t ${self.__monthly_objective.quantize(Decimal('.0001'), rounding=ROUND_HALF_EVEN)}")
        print(f"Activos totales:\t\t ${self.__total_assets.quantize(Decimal('.0001'), rounding=ROUND_HALF_EVEN)}")
        print(f"Invitados totales:\t\t ${self.__total_guests.quantize(Decimal('.0001'), rounding=ROUND_HALF_EVEN)}")
        print(f"Invitados anuales:\t\t ${self.__annual_guests.quantize(Decimal('.0001'), rounding=ROUND_HALF_EVEN)}")
        print(
            f"Invitados mensuales:\t\t ${self.__monthly_guests.quantize(Decimal('.0001'), rounding=ROUND_HALF_EVEN)}\n")
        print(
            f"Inversion inicial:\t\t${self.__initial_investment.quantize(Decimal('.0001'), rounding=ROUND_HALF_EVEN)}")
        print(f"Aportación Mensual:\t\t${self.__kuspit.quantize(Decimal('.0001'), rounding=ROUND_HALF_EVEN)}")
        print(
            f"Comisión sowos (sowos +):\t${self.__shared_commission.quantize(Decimal('.0001'), rounding=ROUND_HALF_EVEN)}")

    # def generate_periods(self, years):
    #     number_of_periods = int(years * 12)
    #
    #     periods = []
    #
    #     initial_investment_variable = initial_investment(1, self.__reinvest_profits, self.__monthly_contribution,
    #                                                      initial_amount=self.__initial_investment)
    #
    #     profits_via_referrals_variable = profits_via_referrals()
    #
    #     first_period = PeriodFactory(1, phase(1, duration_of_phase_1), self.__interest_rate, self.__years_investment,
    #                                  self.__reinvest_profits, self.__monthly_contribution, self.__monthly_guests,
    #                                  self.__guest_average, self.__shared_commission, self.__membership_cost,
    #                                  self.__points, initial_investment_interests(initial_investment_variable,
    #                                                                              self.__interest_rate),
    #                                  initial_investment=initial_investment_variable)
    #     periods.append(first_period)
    #     first_period.display_period()
    #
    #     for period in range(1, number_of_periods):
    #         past_period = period - 1
    #         next_period = periods[past_period].create_next()
    #         periods.append(next_period)
    #         next_period.display_period()

