# -*- coding: utf-8 -*-
from FuncionesGenerales import *
from RolDelJugador import RolDelJugador


class Caballero(RolDelJugador):
    # constructor de la clase en donde inicializamos los atributos de rol caballero
    def __init__(self, Nombre='Thomas'):
        RolDelJugador.__init__(self, Nombre)
        self.max_salud = 100
        self.Medidor_salud = self.max_salud
        self.tipo_rol = 'amigo'

    # informacion del caballero
    def info(self):
        print("¡Mi nombre es Thomas. Soy un caballero de las llanuras meridionales!")

    def conquistar_choza(self, Choza):
        print_red_bold("Entrando en la choza %d..." % Choza.numero)
        es_enemigo = (isinstance(Choza.ocupantes, RolDelJugador) and Choza.ocupantes.tipo_rol == 'enemigo')
        continuar_ataque = 1

        if es_enemigo:
            print_red_bold("¡Enemigo sitiado!")
            self.mostrar_salud(True)
            Choza.ocupantes.mostrar_salud(True)
            while continuar_ataque:
                continuar_ataque = int(input("...continuar ataque? Si(1)/No(0)"))
                if continuar_ataque == 0:
                    self.huir()
                    break

                self.atacar(Choza.ocupantes)

                if Choza.ocupantes.Medidor_salud <= 0:
                    print("")
                    Choza.conquistar(self)
                    break
                if self.Medidor_salud <= 0:
                    print("")
                    break
        else:
            if Choza.tipo_de_ocupante() == 'No ocupada':
                print_red_bold("La choza está vacía")
            else:
                print_red_bold("¡Amigo avistado!")
            Choza.conquistar(self)
            self.curar()

    def huir(self):
        print_red_bold("Escapando del enemigo...")
        self.enemigo = None
