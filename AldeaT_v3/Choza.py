# -*- coding: utf-8 -*-
from FuncionesGenerales import *


class Choza:
    # constructor en donde se inicializa los atributos de la choza
    def __init__(self, numero, ocupantes):
        self.ocupantes = ocupantes
        self.numero = numero
        self.conquistada = False

    def conquistar(self, nuevo_ocupante):
        self.ocupantes = nuevo_ocupante
        self.conquistada = True
        print_red_bold("¡Buena trabajo! La choza %d ha sido conquistada" % self.numero)

    def tipo_de_ocupante(self):
        if self.conquistada:
            tipo_ocupante = 'Conquistada'
        elif self.ocupantes is None:
            tipo_ocupante = 'No ocupada'
        else:
            tipo_ocupante = self.ocupantes.tipo_rol

        return tipo_ocupante
