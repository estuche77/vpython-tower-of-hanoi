'''
Created on 11/6/2015

@author: Estuche
'''

from vpython import *


def autoMove(origen, destino, pila, palos):

    # Se selecciona el anillo y se borra de la pila de donde se toma
    select = pila[origen][-1]
    del (pila[origen][-1])

    # Variable de movimiento
    dt = 0.1

    # Movimiento vertical, levanta el anillo hasta salir del palo
    while select.pos.y < palos[origen].length + 1:
        rate(2048)
        select.pos = select.pos + vector(0, 1, 0) * dt

    # Movimiento de traslacion al palo correspondiente
    if origen <= destino:
        while select.pos.x <= palos[destino].pos.x - 0.1:
            rate(2048)
            select.pos = select.pos + vector(1, 0, 0) * dt
    else:
        while select.pos.x >= palos[destino].pos.x - 0.1:
            rate(2048)
            select.pos = select.pos + vector(-1, 0, 0) * dt

    # Movimiento vertical, baja el anillo hasta tocar la base, u otro anillo
    while select.pos.y >= len(pila[destino]) + 1:
        rate(2048)
        select.pos = select.pos + vector(0, -1, 0) * dt

    # Se agrega el anillo a la pila de destino
    pila[destino].append(select)
