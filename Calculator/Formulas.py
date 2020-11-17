#!/usr/bin/env python
import math
from sys import argv

class Basics:
    def __init__(self, _objetivo_anual, _promedio_invitados, _inversion_inicial):
        self.__objetivo_anual = _objetivo_anual
        self.__promedio_invitados = _promedio_invitados
        self.__inversion_inicial = _inversion_inicial
        self.__kuspit = .00625

    def comision_compartida(self):
        return self.__kuspit * .3

    def objetivo_mensual(self):
        return self.__objetivo_anual / 12

    def activos_totales(self):
        return self.objetivo_mensual() / (self.comision_compartida() / 12)

    def invitados_totales(self):
        return self.activos_totales() / self.__promedio_invitados

    def invitados_anuales(self):
        return self.invitados_totales() / 5

    def invitados_mensuales(self):
        return math.ceil(self.invitados_anuales() / 12)

    def display(self):
        print(f"Objetivo Anual: {self.__objetivo_anual}")
        print(f"Promedio de Invitados: {self.__promedio_invitados} \n")
        print(f"objetivo mensual:\t ${self.objetivo_mensual()}")
        print(f"Activos totales:\t ${self.activos_totales()}")
        print(f"Invitados totales:\t ${self.invitados_totales()}")
        print(f"Invitados anuales:\t ${self.invitados_anuales()}")
        print(f"Invitados mensuales:\t ${self.invitados_mensuales()}\n")
        print(f"Inversion inicial:\t${self.__inversion_inicial}")
        print(f"Aportación Mensual:\t${self.__kuspit}")
        print(f"Comisión sowos (sowos):\t${self.__kuspit}")




if __name__ == '__main__':
    script, objetivo_anual, promedio_invitados, inversion_inicial = argv
    Basics(int(objetivo_anual), int(promedio_invitados), int(inversion_inicial)).display()