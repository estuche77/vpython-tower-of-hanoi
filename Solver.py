'''
Created on 10/6/2015

@author: Estuche
'''
from vpython import *
import autoMoves

# Sulucionador recursivo de las Torres de Hanoi


def hanoi(Largo, Origen, Auxiliar, Destino, pila, palos):

    if Largo != 0:
        hanoi(Largo - 1, Origen, Destino, Auxiliar, pila, palos)

        # Imprime y llama a la funcion que mueve los discos
        print("Mover el disco ", Largo, " de la torre ",
              Origen + 1, " a la torren", Destino + 1)
        autoMoves.autoMove(Origen, Destino, pila, palos)

        hanoi(Largo - 1, Auxiliar, Origen, Destino, pila, palos)
