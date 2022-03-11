'''
Created on 17/6/2015

@author: Estuche
'''
from vpython import *
import Solver
import userMoves

# Fucion de menu de anillos


def Anillos():

    # Se declaran las constantes de texto para mostrar como menu principal
    tres = text(text="3", pos=vector(-6, 12, 0),
                align="center", color=color.white, font="sans")
    cuatro = text(text="4", pos=vector(-4, 12, 0),
                  align="center", color=color.white, font="sans")
    cinco = text(text="5", pos=vector(-2, 12, 0),
                 align="center", color=color.white, font="sans")
    seis = text(text="6", pos=vector(0, 12, 0),
                align="center", color=color.white, font="sans")
    siete = text(text="7", pos=vector(2, 12, 0),
                 align="center", color=color.white, font="sans")
    ocho = text(text="8", pos=vector(4, 12, 0),
                align="center", color=color.white, font="sans")
    nueve = text(text="9", pos=vector(6, 12, 0),
                 align="center", color=color.white, font="sans")

    # Se permite al usuario escoger la cantidad de anillos antes de iniciar el juego
    while True:
        rate(30)
        ev = scene.waitfor('click')

        if ev.event == 'click':

            # La posicion del click se comparar con el area del texto por medio de 4 datos
            if ev.pos.x > tres.pos.x - tres.width / 2 - 1 and ev.pos.x < tres.pos.x + tres.width / 2 + 1 and ev.pos.y > tres.pos.y - tres.height / 2 - 1 and ev.pos.y < tres.pos.y + tres.height / 2 + 1:

                # Esta seccion se encarga de hacer invisible y borrar todo el menu texto
                tres.visible = False
                del tres
                cuatro.visible = False
                del cuatro
                cinco.visible = False
                del cinco
                seis.visible = False
                del seis
                siete.visible = False
                del siete
                ocho.visible = False
                del ocho
                nueve.visible = False
                del nueve

                # Retorna el numero presionado
                return 3

            # La posicion del click se comparar con el area del texto por medio de 4 datos
            elif ev.pos.x > cuatro.pos.x - cuatro.width / 2 - 1 and ev.pos.x < cuatro.pos.x + cuatro.width / 2 + 1 and ev.pos.y > cuatro.pos.y - cuatro.height / 2 - 1 and ev.pos.y < cuatro.pos.y + cuatro.height / 2 + 1:

                # Esta seccion se encarga de hacer invisible y borrar todo el menu texto
                tres.visible = False
                del tres
                cuatro.visible = False
                del cuatro
                cinco.visible = False
                del cinco
                seis.visible = False
                del seis
                siete.visible = False
                del siete
                ocho.visible = False
                del ocho
                nueve.visible = False
                del nueve

                # Retorna el numero presionado
                return 4

            # La posicion del click se comparar con el area del texto por medio de 4 datos
            elif ev.pos.x > cinco.pos.x - cinco.width / 2 - 1 and ev.pos.x < cinco.pos.x + cinco.width / 2 + 1 and ev.pos.y > cinco.pos.y - cinco.height / 2 - 1 and ev.pos.y < cinco.pos.y + cinco.height / 2 + 1:

                # Esta seccion se encarga de hacer invisible y borrar todo el menu texto
                tres.visible = False
                del tres
                cuatro.visible = False
                del cuatro
                cinco.visible = False
                del cinco
                seis.visible = False
                del seis
                siete.visible = False
                del siete
                ocho.visible = False
                del ocho
                nueve.visible = False
                del nueve

                # Retorna el numero presionado
                return 5

            # La posicion del click se comparar con el area del texto por medio de 4 datos
            elif ev.pos.x > seis.pos.x - seis.width / 2 - 1 and ev.pos.x < seis.pos.x + seis.width / 2 + 1 and ev.pos.y > seis.pos.y - seis.height / 2 - 1 and ev.pos.y < seis.pos.y + seis.height / 2 + 1:

                # Esta seccion se encarga de hacer invisible y borrar todo el menu texto
                tres.visible = False
                del tres
                cuatro.visible = False
                del cuatro
                cinco.visible = False
                del cinco
                seis.visible = False
                del seis
                siete.visible = False
                del siete
                ocho.visible = False
                del ocho
                nueve.visible = False
                del nueve

                # Retorna el numero presionado
                return 6

            # La posicion del click se comparar con el area del texto por medio de 4 datos
            elif ev.pos.x > siete.pos.x - siete.width / 2 - 1 and ev.pos.x < siete.pos.x + siete.width / 2 + 1 and ev.pos.y > siete.pos.y - siete.height / 2 - 1 and ev.pos.y < siete.pos.y + siete.height / 2 + 1:

                # Esta seccion se encarga de hacer invisible y borrar todo el menu texto
                tres.visible = False
                del tres
                cuatro.visible = False
                del cuatro
                cinco.visible = False
                del cinco
                seis.visible = False
                del seis
                siete.visible = False
                del siete
                ocho.visible = False
                del ocho
                nueve.visible = False
                del nueve

                # Retorna el numero presionado
                return 7

            # La posicion del click se comparar con el area del texto por medio de 4 datos
            elif ev.pos.x > ocho.pos.x - ocho.width / 2 - 1 and ev.pos.x < ocho.pos.x + ocho.width / 2 + 1 and ev.pos.y > ocho.pos.y - ocho.height / 2 - 1 and ev.pos.y < ocho.pos.y + ocho.height / 2 + 1:

                # Esta seccion se encarga de hacer invisible y borrar todo el menu texto
                tres.visible = False
                del tres
                cuatro.visible = False
                del cuatro
                cinco.visible = False
                del cinco
                seis.visible = False
                del seis
                siete.visible = False
                del siete
                ocho.visible = False
                del ocho
                nueve.visible = False
                del nueve

                # Retorna el numero presionado
                return 8

            # La posicion del click se comparar con el area del texto por medio de 4 datos
            elif ev.pos.x > nueve.pos.x - nueve.width / 2 - 1 and ev.pos.x < nueve.pos.x + nueve.width / 2 + 1 and ev.pos.y > nueve.pos.y - nueve.height / 2 - 1 and ev.pos.y < nueve.pos.y + nueve.height / 2 + 1:

                # Esta seccion se encarga de hacer invisible y borrar todo el menu texto
                tres.visible = False
                del tres
                cuatro.visible = False
                del cuatro
                cinco.visible = False
                del cinco
                seis.visible = False
                del seis
                siete.visible = False
                del siete
                ocho.visible = False
                del ocho
                nueve.visible = False
                del nueve

                # Retorna el numero presionado
                return 9

# Fucion de submenu


def subMenu(baseTable, palos, pila, autoTxt, userTxt, cantAnillos):

    # Permite al usuario escoger entre dos menus
    while True:
        #rate(30)

        # Se lee el click y se guarda en una variable su posicion
        ev = scene.waitfor('click')

        if ev.event == 'click':

            # Texto de autoresolver, se compara su area en 4 variables
            if ev.pos.x > autoTxt.pos.x - autoTxt.width / 2 and ev.pos.x < autoTxt.pos.x + autoTxt.width / 2 and ev.pos.y > autoTxt.pos.y - autoTxt.height / 2 and ev.pos.y < autoTxt.pos.y + autoTxt.height / 2:

                # Esta seccion se encarga de hacer invisible y borrar todo el menu texto
                userTxt.visible = False
                del userTxt
                autoTxt.visible = False
                del autoTxt
                text(text=str(2 ** cantAnillos - 1), pos=vector(-4, 12, 0),
                     align="center", color=color.white, font="sans")
                text(text="movimientos", pos=vector(1, 12, 0),
                     align="center", color=color.white, font="sans")

                # Se llama a la funcion perteneciente junto a sus parametros
                Solver.hanoi(cantAnillos, 0, 1, 2, pila, palos)
                return

            # Texto de reolver usario, se compara su area en 4 variables
            elif ev.pos.x > userTxt.pos.x - userTxt.width / 2 and ev.pos.x < userTxt.pos.x + userTxt.width / 2 and ev.pos.y > userTxt.pos.y - userTxt.height / 2 and ev.pos.y < userTxt.pos.y + userTxt.height / 2:

                # Esta seccion se encarga de hacer invisible y borrar todo el menu texto
                userTxt.visible = False
                del userTxt
                autoTxt.visible = False
                del autoTxt

                # Se declaran nuevos texto que se usaran en las siguientes ventanas
                text(text="Solucion Optima", pos=vector(-9, 12, 0),
                     align="center", color=color.white, font="sans")
                solu = text(text=str(2 ** cantAnillos - 1), pos=vector(-3,
                            12, 0), align="center", color=color.white, font="sans")
                mov = text(text=str(0), pos=vector(2, 12, 0),
                           align="center", color=color.white, font="sans")
                text(text="movimientos", pos=vector(7, 12, 0),
                     align="center", color=color.white, font="sans")

                # Se llama a la funcion perteneciente junto a sus parametros
                userMoves.user(baseTable, pila, palos, mov, solu)
                return
