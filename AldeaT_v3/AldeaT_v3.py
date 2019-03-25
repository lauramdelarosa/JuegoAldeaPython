# -*- coding: utf-8 -*-

import textwrap

from Caballero import Caballero
from Choza import Choza
from Funciones import *
from Orco import Orco


class Juego:
    # Funcion que inicializa las chozas y el jugador
    def __init__(self):
        self.chozas = []
        self.jugador = None

        # Funcion que

    def get_ocupantes(self):
        return [x.tipo_de_ocupante() for x in self.chozas]

    # Funcion que muestra la introduccion y la mision
    def mostrar_mision(self):
        print_bold("Aldea T")

        msg = ("La guerra entre los humanos y hombres lobo en Hallstatt es un hecho. "
               "Un enorme ejército de hombres lobo se dirigía hacia los territos de los humanos. "
               "Destruían prácticamente todo en su camino. Thomas uno de los valiente caballeros inició un largo viaje "
               "hacia el este a través de un desconocido bosque espeso. Durante dos días y dos noches, se movió con cautela "
               "a través del grueso bosque. En su camino, vio una pequeña aldea. Cansado y con la esperanza de reponer "
               "su stock de alimentos, decidió tomar un desvío. Al acercarse, vio cinco chozas. No había nadie alrededor. "
               "En ese instante, decidió entrar en un choza...")

        print(textwrap.fill(msg, 80))
        print_bold("Misión:")
        print("  1. Lucha contra el enemigo.")
        print("  2. Conquista cada una de las chozas hasta que estén bajo tu control")
        print("-" * 72)

    # Funcion que procesa la decision del usuario
    def _procesar_decision(self):
        verifica_decision = True
        decision_usuario = 0
        print("Ocupantes actuales: %s" % self.get_ocupantes())
        while verifica_decision:
            user_choice = input("Elige un número de choza para entrar (1-5): ")
            try:
                decision_usuario = int(user_choice)
            except ValueError as e:
                print("dato incorrecto: %s \n" % e.args)
                continue
            try:
                if self.chozas[decision_usuario - 1].conquistada:
                    print("Esta choza ya está conquistada")
                    print_bold("<INFO: No puedes curarte en las choza que hayas conquistado.>")
                else:
                    verifica_decision = False
            except IndexError:
                print("Entrada no aceptada: ", decision_usuario)
                print("El número debe estar entre 1 y 5.Inténtalo de nuevo")
                continue
        return decision_usuario

    def _ocupar_chozas(self):
        for i in range(5):
            ocupantes = ['enemigo', 'amigo', None]
            eleccion_aleatoria = random.choice(ocupantes)

            if eleccion_aleatoria == 'enemigo':
                nombre = 'Enemigo-' + str(i + 1)  # Colocamos el numero del enemigo como identificador
                self.chozas.append(Choza(i + 1, Orco(nombre)))
            elif eleccion_aleatoria == 'amigo':
                nombre = 'Caballero-' + str(i + 1)
                self.chozas.append(Choza(i + 1, Caballero(nombre)))
            else:
                self.chozas.append(Choza(i + 1, eleccion_aleatoria))

    def play(self):
        self.jugador = Caballero()
        self._ocupar_chozas()
        Contador_chozas_conquistadas = 0

        self.mostrar_mision()
        self.jugador.mostrar_salud(True)

        while Contador_chozas_conquistadas < 5:
            decision_usuario = self._procesar_decision()
            self.jugador.conquistar_choza(self.chozas[decision_usuario - 1])

            if self.jugador.Medidor_salud <= 0:
                print_bold("Sir Gandorel, esperamos que la próxima vez tenga más suerte")
                break

            if self.chozas[decision_usuario - 1].conquistada:
                Contador_chozas_conquistadas += 1

        if Contador_chozas_conquistadas == 5:
            print_bold("¡Enhorabuena! Sir Gandorel ha conquistado la aldea")
