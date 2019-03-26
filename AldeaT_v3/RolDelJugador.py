# -*- coding: utf-8 -*-

from ErrorRolJugador import GameUnitError
from FuncionesGenerales import *


# esta clase define el rol del jugador ya sea caballero o hombre lobo
class RolDelJugador:
    def __init__(self, nombre_rol=''):
        self.max_salud = 0
        self.Medidor_salud = 0
        self.nombre = nombre_rol
        self.enemigo = None
        self.tipo_rol = None  # amigo o enemigo

    def info(self):
        pass

    # funcion que elije a quien atacar y hiere en un rango de 20 a 25
    def atacar(self, enemigo):
        atacado = eleccion_aleatoria_ataque(self, enemigo)
        herida = random.randint(20, 25)
        # toma la salud maxima del atacado y le resta la herida.
        atacado.Medidor_salud = max(atacado.Medidor_salud - herida, 0)
        print("¡Ataque! ")
        self.mostrar_salud()
        enemigo.mostrar_salud()

    # esta funcion se encarga de curar al tipo de juagdor y al final muestra la salud
    def curar(self, curacion_completa=True):
        if self.Medidor_salud == self.max_salud:  # Caso en el que la salud sea completa
            return

        if curacion_completa:
            self.Medidor_salud = self.max_salud

        if self.Medidor_salud > self.max_salud:
            self.Medidor_salud = self.max_salud
            raise GameUnitError("Medidor_salud > max_salud!!", 101)

        print_red_bold("¡Has sido curado!")
        self.mostrar_salud(True)

    # funcion que resetea la salud del tipo de jugador a su estado inicial
    def reset_medidor_salud(self):
        self.Medidor_salud = self.max_salud

    # funcion que muestra la salud del tipo de jugador
    def mostrar_salud(self, bold=False):
        # Se presenta un problema si no tenemos ningun enemigo
        msg = "Salud: %s: %d" % (self.nombre, self.Medidor_salud)
        if bold:
            print_red_bold(msg)
        else:
            print(msg)
