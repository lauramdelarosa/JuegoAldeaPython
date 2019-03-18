# -*- coding: utf-8 -*-

#libreria para datos aletorios
import random
#libreria para ajustar texto en pantalla
import textwrap
#libreria para ansi escape.
import colorama

 #Funcion para mostrar por pantalla un string en negrita
def print_bold(msg):
   print("\033[1m"+msg+"\033[0m")

#Funcion para mostrar una linea punteada
def print_linea_punteada(width=80):
    print('-'*width)

#Funcion que define un vector chozas y lo llena con datos aleatoria del vector ocupantes
def ocupar_chozas():
    ocupantes = ['enemigo','amigo','no ocupada']
    chozas = []
    while len(chozas) < 5: 
        eleccion_aleatoria = random.choice(ocupantes)
        chozas.append(eleccion_aleatoria)
    return chozas

#Funcion que muestra la introduccion y la mision
def mostrar_mision():
    print_bold("Aldea T")

    msg = ("La guerra entre los humanos y hombres lobo en Hallstatt es un hecho. "
          "Un enorme ejército de hombres lobo se dirigía hacia los territos de los humanos. "
          "Destruían prácticamente todo en su camino. Thomas uno de los valiente caballeros inició un largo viaje "
          "hacia el este a través de un desconocido bosque espeso. Durante dos días y dos noches, se movió con cautela "
          "a través del grueso bosque. En su camino, vio una pequeña aldea. Cansado y con la esperanza de reponer "
          "su stock de alimentos, decidió tomar un desvío. Al acercarse, vio cinco chozas. No había nadie alrededor. "
          "En ese instante, decidió entrar en un choza...")

    print(textwrap.fill(msg, width = 80))
    print_bold("Misión:")
    print("Elige una choza donde poder descansar...")
    print_bold("NOTA:")
    print("¡Cuidado! Hay enemigos rondando la zona")
    print_linea_punteada()

#Funcion que procesa la decision del usuario
def procesar_decision_usuario():
    mensaje_decision_usuario = "Elige una choza, introduce un número entre 1 y 5: "
    decision_usuario = input("\n"+mensaje_decision_usuario)
    choza_elegida = int(decision_usuario)
    return choza_elegida

#Funcion muestra mensaje con informacion de todas las chozas y la escogida por el usuario en negrita
def revelar_ocupantes(choza_elegida, chozas):
    msg=""
    print("Revelando los ocupantes...")
    for i in range(len(chozas)):
        ocupantes_info = "<%d:%s>"%(i+1, chozas[i])
        if i+1 == choza_elegida:
            ocupantes_info = "\033[1m" + ocupantes_info + "\033[0m"
        msg += ocupantes_info + " "
    print("\t" + msg)
    print_linea_punteada()

#Funcion que muestra la salud del caballero y del enemigo
def mostrar_salud(medidor_salud, bold):
    if bold:
        print_bold("Salud Thomas:")
        print_bold("%d"%(medidor_salud['jugador']))
        print_bold("Salud Enemigo:")
        print_bold("%d"%(medidor_salud['enemigo']))
    else:
        print("Salud Thomas:")
        print("%d"%(medidor_salud['jugador']))
        print("Salud Enemigo:")
        print("%d"%(medidor_salud['enemigo']))

#Funcion que resetea la salud del caballero y del enemigo
def reset_medidor_salud(medidor_salud):
    medidor_salud['jugador']=40
    medidor_salud['enemigo']=30

#Funcion que ataca al enemigo
def atacar(medidor_salud):
    lista_golpes = 4*['jugador']+6*['enemigo']
    unidad_herida = random.choice(lista_golpes)
    puntos_vida = medidor_salud[unidad_herida]
    herida = random.randint(10,15)
    medidor_salud[unidad_herida] = max(puntos_vida- herida,0)
    print("¡Ataque!")
    mostrar_salud(medidor_salud,bold=False)


#En la siguiente función se establece un sistema de combate iterativo
def play_game(medidor_salud):
    chozas = ocupar_chozas()
    decision_usuario = procesar_decision_usuario()
    revelar_ocupantes(decision_usuario, chozas)

    if chozas[decision_usuario-1] != 'enemigo':
        print_bold("¡Enhorabuena! ¡Has GANADO!")
    else:
        print_bold('¡Enemigo encontrado!')
        mostrar_salud(medidor_salud, bold=True)
        continuar_ataque = True

        while continuar_ataque:
            continuar_ataque = int(input("...continuar con el ataque? Si(1)/No(0)"))
            if continuar_ataque == 0:
                print_bold("Huyendo con el siguiente estado de salud...")
                mostrar_salud(medidor_salud, bold=True)
                print_bold("¡Game Over!")
                break

            atacar(medidor_salud)

            if medidor_salud['enemigo'] <=0:
                print_bold("¡Thomas ha derrotado a su enemigo!")
                break
            if medidor_salud['jugador'] <=0:
                print_bold("Thomas ha muerto ... :C")
                break



#Funcion para hacer funcionar el programa principal que queremos ejecutar
def run_application():
    colorama.init()
    seguir_jugando = 1
    medidor_salud = {}
    reset_medidor_salud(medidor_salud)
    mostrar_mision()

    while seguir_jugando == 1:
        reset_medidor_salud(medidor_salud)
        play_game(medidor_salud)
        seguir_jugando = int(input("¿Quieres jugar de nuevo? Si(1)/No(0):"))


#Aqui inicia todo
if __name__ == '__main__':
    run_application()