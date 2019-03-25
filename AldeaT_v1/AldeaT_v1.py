# -*- coding: utf-8 -*-

#libreria para datos aletorios
import random
#libreria para ajustar texto en pantalla
import textwrap
#libreria para ansi escape.
import colorama


if __name__ == '__main__':
    colorama.init()
    # region definicion de variables
    seguir_jugando = 1
    ocupantes = ['enemigo','amigo','no ocupada']
    ancho_linea = 80
    linea_punteada = ancho_linea * '-'
    # endregion

    print(linea_punteada)
    print("\033[1m"+ "Aldea T" + "\033[0m")

    msg = ("La guerra entre los humanos y hombres lobo en Hallstatt es un hecho. "
          "Un enorme ejército de hombres lobo se dirigía hacia los territos de los humanos. "
          "Destruían prácticamente todo en su camino. Thomas uno de los valientes caballeros inició un largo viaje "
          "hacia el este a través de un desconocido bosque espeso. Durante dos días y dos noches, se movió con cautela "
          "a través del grueso bosque. En su camino, vio una pequeña aldea. Cansado y con la esperanza de reponer "
          "su stock de alimentos, decidió tomar un desvío. Al acercarse, vio cinco chozas. No había nadie alrededor. "
          "En ese instante, decidió entrar en un choza...")

    print(textwrap.fill(msg, width=ancho_linea))
    print("\033[1m"+"Misión:"+"\033[0m")
    print("Elige una choza donde poder descansar...")
    print("\033[1m"+"NOTA:"+"\033[0m")
    print("¡Cuidado! Hay enemigos rondando la zona")
    print(linea_punteada)

    while seguir_jugando == 1:
        #definimos un vector chozas y lo llenamos con datos aleatoria del vector ocupantes
        chozas = []
        while len(chozas) < 5:
            eleccion_aleatoria = random.choice(ocupantes)
            chozas.append(eleccion_aleatoria)

        #se guarda la eleccion del usuario
        mesaje_decision_usuario =  "Elige una choza, introduce un número entre 1 y 5: "
        decision_usuario = input("\n"+mesaje_decision_usuario)
        choza_elegida = int(decision_usuario)

        #validamos la eleccion del usuario en el vector chozas y mostramos mensaje
        #con informacion de todas las chozas y la escogida por el usuario en negrita
        print("Descubriendo los ocupantes...")
        msg=""
        for index_ocupante_choza in range(len(chozas)):
            ocupantes_info = "<%d:%s>"%(index_ocupante_choza+1, chozas[index_ocupante_choza])
            if index_ocupante_choza+1 == choza_elegida:
                ocupantes_info = "\033[1m" + ocupantes_info + "\033[0m"
            msg += ocupantes_info + " "
        print("\t" + msg)
        print(linea_punteada)

        #validamos la decision del usuario como ganador o perdedor
        print("\033[1m" + "Entrando en la choza %d..." %choza_elegida + "\033[0m")

        if chozas[choza_elegida-1] == 'enemigo':
            print("\033[1m" + "Thomas ha muerto asesinado por una manada de hombres lobo (Mucha suerte la próxima vez)" + "\033[0m")
        else:
            print("\033[1m" + "¡Felicidades! Thomas ha podido descansar con éxito" + "\033[0m")
        print(linea_punteada)
        seguir_jugando = int(input("¿Quieres jugar de nuevo? Si(1)/No(0):"))
