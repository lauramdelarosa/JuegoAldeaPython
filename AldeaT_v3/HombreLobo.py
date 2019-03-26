# -*- coding: utf-8 -*-
from RolDelJugador import RolDelJugador


class HombreLobo(RolDelJugador):
    # constructor donde inializa los atributos del hombre lobo
    def __init__(self, Nombre=''):
        RolDelJugador.__init__(self, Nombre)
        self.max_salud = 80
        self.Medidor_salud = self.max_salud
        self.tipo_rol = 'enemigo'
        self.numero_choza = 0

    # informacion del hombre lobo
    def info(self):
        print("Grrrr..Soy un hombre lobo montador de huargos. Creo que esta noche serás mi cena")
