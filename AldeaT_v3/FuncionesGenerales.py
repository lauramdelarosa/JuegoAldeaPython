# -*- coding: utf-8 -*-
import random


# Funcion para mostrar por pantalla un string en negrita
def print_red_bold(msg):
    print("\033[31m" + msg + "\033[30m")


# Funcion dibuja una linea punteada en la consola
def print_linea_punteada(width=72):
    print('-' * width)


# funcion que define aleatoriamente a quien atacar con una probabilidad 50% 50%
def eleccion_aleatoria_ataque(obj1, obj2):
    weighted_list = 5 * [id(obj1)] + 5 * [id(obj2)]
    selection = random.choice(weighted_list)

    if selection == id(obj1):
        return obj1

    return obj2
