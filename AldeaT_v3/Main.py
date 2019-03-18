# -*- coding: utf-8 -*-

#Importamos algunos modulos

import sys
import os
import colorama

#Importamos nuestras clases y funciones

from Ataca_a_los_orcos_V1_0_0 import Juego

#CODIGO principal

if __name__ == '__main__':
    #para resolver el ansi escape (negrita en el terminal)
    colorama.init()
    game = Juego()
    game.play()
