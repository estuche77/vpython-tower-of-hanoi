'''
Created on 10/6/2015

@author: Estuche
'''

#Se importan librerias y demas modulos
from visual import *
import anillosMenu


def mainwin():
    #Se declaran las caracteristicas de la ventana
    scene.x = 100
    scene.y = 100
    scene.height = 768
    scene.width = 1366
    scene.title = "Torres de Hanoi"
    
    #Se declaran caracteristicas de la ecena
    scene.background = color.gray(0.1)
    scene.lights = [distant_light(direction = (0.22, 0.44, 0.88), color = color.gray(0.8))]
    #scene.userspin = False
    #scene.userzoom = False
    scene.center = (0, 5, 0)
    scene.forward = (0, -1, -3)
    
    #Se inicia las columnas
    colIzq = cylinder(pos = (-12, 0, 0), axis = (0, 10, 0), radius = 0.4, color = (1.0,0.5,0), material = materials.wood)
    colCen = cylinder(pos = (0, 0, 0), axis = (0, 10, 0), radius = 0.4, color = (1.0,0.5,0), material = materials.wood)
    colDer = cylinder(pos = (12, 0, 0), axis = (0, 10, 0), radius = 0.4, color = (1.0,0.5,0), material = materials.wood)
    
    #Se inicia la base
    baseTable = box(pos = (0, 0.15, 0), axis = (35, 0, 0), color = (1.0, 0.5, 0), width = 12, height = 0.5, material = materials.wood)
    
    #Se declaran variables globales
    palos = [colIzq, colCen, colDer]
    anillos = []
    
    #La lista de colore de anillos usada a la hora de crear anillos
    colores = [(0.4, 0, 0), color.red, color.orange, color.yellow, color.green, color.cyan, color.blue, color.magenta, color.white]
    
    #Se llama la funcion que muestra un menu para elegir la cantidad de anillos a resolver
    cantAnillos = anillosMenu.Anillos()
    
    #Se inicializan los anillos
    for i in range(9 - cantAnillos, 9):
        anillos.append(ring (pos = (colIzq.x, len(anillos) + 1, 0), radius = 0.5 * (10 - i), thickness = 0.6, axis = (0, 1, 0), color = colores[i]))
    
    #Se apilan los anillos
    pila = [anillos, [], []]
    
    #Declara una flecha indicadora donde iran los anillos
    arrow(pos = colDer.pos + (0, 14, 0), axis = (0, -1, 0), length = 2, shaftwidth = 0.4, headwidth = 0.8, color = color.green)
    
    #Declara texto para ser usado como constante de menu
    autoTxt = text(text = "Auto Resolver", pos = (-6, 12, 0), align = "center", color = color.white, font = "sans")
    userTxt = text(text = "Empezar", pos = (6, 12, 0), align = "center", color = color.white, font = "sans")
    
    #Se llama la funcion del submenu de los anillos
    anillosMenu.subMenu(baseTable, palos, pila, autoTxt, userTxt, cantAnillos)

mainwin()