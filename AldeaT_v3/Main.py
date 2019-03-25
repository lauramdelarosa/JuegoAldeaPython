# -*- coding: utf-8 -*-

# Importamos algunos modulos

# libreria para ansi escape.
import colorama

# Importamos nuestras clases y funciones
from AldeaT_v3 import Juego

# Aqui inicia todo
if __name__ == '__main__':
    colorama.init()
    game = Juego()
    game.play()
