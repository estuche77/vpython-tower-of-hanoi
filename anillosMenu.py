'''
Created on 17/6/2015

@author: Estuche
'''
from visual import *
import Solver
import userMoves

#Fucion de menu de anillos
def Anillos():
    
    #Se declaran las constantes de texto para mostrar como menu principal
    tres = text(text = "3", pos = (-6, 12, 0), align = "center", color = color.white, font = "sans")
    cuatro = text(text = "4", pos = (-4, 12, 0), align = "center", color = color.white, font = "sans")
    cinco = text(text = "5", pos = (-2, 12, 0), align = "center", color = color.white, font = "sans")
    seis = text(text = "6", pos = (0, 12, 0), align = "center", color = color.white, font = "sans")
    siete = text(text = "7", pos = (2, 12, 0), align = "center", color = color.white, font = "sans")
    ocho = text(text = "8", pos = (4, 12, 0), align = "center", color = color.white, font = "sans")
    nueve = text(text = "9", pos = (6, 12, 0), align = "center", color = color.white, font = "sans")

    #Se permite al usuario escoger la cantidad de anillos antes de iniciar el juego
    while True:
        rate(30)
        if scene.mouse.clicked:
            
            #Se lee el click y se guarda en una variable su posicion
            m = scene.mouse.getclick()
            loc = m.pos            
            
            #La posicion del click se comparar con el area del texto por medio de 4 datos
            if loc.x > tres.x - tres.width / 2 - 1 and loc.x < tres.x + tres.width / 2 + 1 and loc.y > tres.y - tres.height / 2 - 1 and loc.y < tres.y + tres.height / 2 + 1:
                
                #Esta seccion se encarga de hacer invisible y borrar todo el menu texto
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
                
                #Retorna el numero presionado
                return 3
            
            #La posicion del click se comparar con el area del texto por medio de 4 datos
            elif loc.x > cuatro.x - cuatro.width / 2 - 1 and loc.x < cuatro.x + cuatro.width / 2 + 1 and loc.y > cuatro.y - cuatro.height / 2 - 1 and loc.y < cuatro.y + cuatro.height / 2 + 1:
                
                #Esta seccion se encarga de hacer invisible y borrar todo el menu texto
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
                
                #Retorna el numero presionado
                return 4
            
            #La posicion del click se comparar con el area del texto por medio de 4 datos
            elif loc.x > cinco.x - cinco.width / 2 - 1 and loc.x < cinco.x + cinco.width / 2 + 1 and loc.y > cinco.y - cinco.height / 2 - 1 and loc.y < cinco.y + cinco.height / 2 + 1:
                
                #Esta seccion se encarga de hacer invisible y borrar todo el menu texto
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
                
                #Retorna el numero presionado
                return 5
            
            #La posicion del click se comparar con el area del texto por medio de 4 datos
            elif loc.x > seis.x - seis.width / 2 - 1 and loc.x < seis.x + seis.width / 2 + 1 and loc.y > seis.y - seis.height / 2 - 1 and loc.y < seis.y + seis.height / 2 + 1:
                
                #Esta seccion se encarga de hacer invisible y borrar todo el menu texto
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
                
                #Retorna el numero presionado
                return 6              
            
            #La posicion del click se comparar con el area del texto por medio de 4 datos
            elif loc.x > siete.x - siete.width / 2 - 1 and loc.x < siete.x + siete.width / 2 + 1 and loc.y > siete.y - siete.height / 2 - 1 and loc.y < siete.y + siete.height / 2 + 1:
                
                #Esta seccion se encarga de hacer invisible y borrar todo el menu texto
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
                
                #Retorna el numero presionado
                return 7
            
            #La posicion del click se comparar con el area del texto por medio de 4 datos
            elif loc.x > ocho.x - ocho.width / 2 - 1 and loc.x < ocho.x + ocho.width / 2 + 1 and loc.y > ocho.y - ocho.height / 2 - 1 and loc.y < ocho.y + ocho.height / 2 + 1:
                
                #Esta seccion se encarga de hacer invisible y borrar todo el menu texto
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
                
                #Retorna el numero presionado
                return 8
            
            #La posicion del click se comparar con el area del texto por medio de 4 datos
            elif loc.x > nueve.x - nueve.width / 2 - 1 and loc.x < nueve.x + nueve.width / 2 + 1 and loc.y > nueve.y - nueve.height / 2 - 1 and loc.y < nueve.y + nueve.height / 2 + 1:
                
                #Esta seccion se encarga de hacer invisible y borrar todo el menu texto
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
                
                #Retorna el numero presionado
                return 9

#Fucion de submenu
def subMenu(baseTable, palos, pila, autoTxt, userTxt, cantAnillos):
    
    #Permite al usuario escoger entre dos menus
    while True:
        rate(30)
        
        #Se lee el click y se guarda en una variable su posicion
        if scene.mouse.clicked:
            m = scene.mouse.getclick()
            loc = m.pos
            
            #Texto de autoresolver, se compara su area en 4 variables
            if loc.x > autoTxt.x - autoTxt.width / 2 and loc.x < autoTxt.x + autoTxt.width / 2 and loc.y > autoTxt.y - autoTxt.height / 2 and loc.y < autoTxt.y + autoTxt.height / 2:
                
                #Esta seccion se encarga de hacer invisible y borrar todo el menu texto
                userTxt.visible = False
                del userTxt
                autoTxt.visible = False
                del autoTxt
                text(text = str(2 ** cantAnillos - 1), pos = (-4, 12, 0), align = "center", color = color.white, font = "sans")
                text(text = "movimientos", pos = (1, 12, 0), align = "center", color = color.white, font = "sans")
                
                #Se llama a la funcion perteneciente junto a sus parametros
                Solver.hanoi(cantAnillos, 0, 1, 2, pila, palos)
            
            #Texto de reolver usario, se compara su area en 4 variables
            elif loc.x > userTxt.x - userTxt.width / 2 and loc.x < userTxt.x + userTxt.width / 2 and loc.y > userTxt.y - userTxt.height / 2 and loc.y < userTxt.y + userTxt.height / 2:
                
                #Esta seccion se encarga de hacer invisible y borrar todo el menu texto
                userTxt.visible = False
                del userTxt
                autoTxt.visible = False
                del autoTxt
                
                #Se declaran nuevos texto que se usaran en las siguientes ventanas
                text(text = "Solucion Optima", pos = (-9, 12, 0), align = "center", color = color.white, font = "sans")
                solu = text(text = str(2 ** cantAnillos - 1), pos = (-3, 12, 0), align = "center", color = color.white, font = "sans")
                mov = text(text = str(0), pos = (2, 12, 0), align = "center", color = color.white, font = "sans")
                text(text = "movimientos", pos = (7, 12, 0), align = "center", color = color.white, font = "sans")
                
                #Se llama a la funcion perteneciente junto a sus parametros
                userMoves.user(baseTable, pila, palos, mov, solu)