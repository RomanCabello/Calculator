#!/usr/bin/env python
from decimal import *
from sys import argv



script, annual_objective, guest_average, initial_investment = argv

annual_objective = Decimal(annual_objective)
guest_average = Decimal(guest_average)
initial_investment = Decimal(initial_investment)

def years():
    return Decimal(5)

def interest_rate():
    rate = Decimal(4)
    return rate / Decimal(100)

def kuspit():
    rate = Decimal(0.63)
    return rate / Decimal(100)

def shared_commission(kuspit):
    percent = Decimal(30)
    return Decimal(kuspit) * Decimal(percent / Decimal(100))

def monthly_objective(annual_objective):
    return Decimal(annual_objective) / Decimal(12)

def total_assets(monthly_objective, shared_commission):
    return monthly_objective / (shared_commission / Decimal(12))

def total_guests(total_assets, guest_average):
    return total_assets / Decimal(guest_average)

def annual_guests(total_guests, years):
    return total_guests / years

def monthly_guests(annual_guests):
    return Decimal(annual_guests / Decimal(12)).quantize(Decimal('1.'), rounding=ROUND_UP)


class Basics:
    def __init__(self, annual_objective, guest_average, initial_investment, shared_commission, kuspit,
                 monthly_objective, total_assets, total_guests, years, interest_rate, annual_guests, monthly_guests):
        self.__annual_objective = annual_objective
        self.__guest_average = guest_average
        self.__initial_investment = initial_investment
        self.__kuspit = kuspit
        self.__years = years
        self.__interest_rate = interest_rate
        self.__shared_commission = shared_commission
        self.__monthly_objective = monthly_objective
        self.__total_assets = total_assets
        self.__total_guests = total_guests
        self.__annual_guests = annual_guests
        self.__monthly_guests = monthly_guests

    def check_type(self):
        print(f"annual objective: {type(self.__annual_objective)}")
        print(f"guest average: {type(self.__guest_average)}")
        print(f"initial investment: {type(self.__initial_investment)}")
        print(f"kuspit: {type(self.__kuspit)}")
        print(f"years: {type(self.__years)}")
        print(f"interest rate: {type(self.__interest_rate)}")
        print(f"shared commission: {type(self.__shared_commission)}")
        print(f"monthly objective: {type(self.__monthly_objective)}")
        print(f"total assets: {type(self.__total_assets)}")
        print(f"total guests: {type(self.__total_guests)}")
        print(f"annual guests: {type(self.__annual_guests)}")
        print(f"monthly guests: {type(self.__monthly_guests)}")


    def display(self):
        print(f"Objetivo Anual: {self.__annual_objective.quantize(Decimal('.0001'))}")
        print(f"Promedio de Invitados: {self.__guest_average.quantize(Decimal('.0001'))} \n")
        print(f"objetivo mensual:\t\t ${self.__monthly_objective.quantize(Decimal('.0001'))}")
        print(f"Activos totales:\t\t ${self.__total_assets.quantize(Decimal('.0001'))}")
        print(f"Invitados totales:\t\t ${self.__total_guests.quantize(Decimal('.0001'))}")
        print(f"Invitados anuales:\t\t ${self.__annual_guests.quantize(Decimal('.0001'))}")
        print(f"Invitados mensuales:\t\t ${self.__monthly_guests.quantize(Decimal('.0001'))}\n")
        print(f"Inversion inicial:\t\t${self.__initial_investment.quantize(Decimal('.0001'))}")
        print(f"Aportación Mensual:\t\t${self.__kuspit.quantize(Decimal('.0001'))}")
        print(f"Comisión sowos (sowos +):\t${self.__shared_commission.quantize(Decimal('.0001'))}")


if __name__ == '__main__':
    shared_commission = shared_commission(kuspit())
    monthly_objective = monthly_objective(annual_objective)
    total_assets = total_assets(monthly_objective, shared_commission)
    total_guests = total_guests(total_assets, guest_average)
    annual_guests = annual_guests(total_guests, years())
    monthly_guests = monthly_guests(annual_guests)

    Basics = Basics(annual_objective, guest_average, initial_investment, shared_commission, kuspit(), monthly_objective,
           total_assets, total_guests, years(), interest_rate(), annual_guests, monthly_guests)

    Basics.display()
