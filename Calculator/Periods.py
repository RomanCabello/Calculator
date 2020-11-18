#!/usr/bin/env python

class Period:
    def __init__(self, _periodo, _tasa_interes, _years, _inversion_inicial=None):
        self.__periodo = _periodo
        self.__inversion_inicial = _inversion_inicial
        self.__tasa_interes = _tasa_interes
        self.__years = _years

    def intereses_inversion_inicial(self):
        self.__intereses_inversion_inicial = self.__inversion_inicial * (1 + (self.__tasa_interes / 12))

    def fase(self):
        if (self.__periodo <= (12 * self.__years)):
            self.__fase = 1

        else:
            self.__fase = 2

