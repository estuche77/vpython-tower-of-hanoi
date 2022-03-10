'''
Created on 10/6/2015

@author: Estuche
'''
from visual import *

def user(baseTable, pila, palos, mov, solu):
    
    #Mientras sea verdadero, osea, siempre
    while True:
        rate(60)
        
        #Si hay eventos de mouse en la ecena
        if scene.mouse.events:
            m = scene.mouse.getevent()
            
            #Identifica el palo de donde se inicia el arrastre
            if m.drag:
                mx = m.project(normal = vector(0, 0, 1)).x
                
                #Decide de donde saca el anillo
                if mx + baseTable.length / 2 < 12:
                    origen = 0
                elif mx + baseTable.length / 2 > 24:
                    origen = 2
                else:
                    origen = 1
                
                #Recoje el anillo
                if len(pila[origen]) > 0:           #Si hay algo en la pila
                    select = pila[origen][-1]       #Selecciona el anillo
                    del (pila[origen][-1])          #Lo borra de la pila original
                    
                    #Se arrastra el anillo con el mouse hasta soltarlo
                    while not scene.mouse.events:
                        
                        #Selecciona la pila en donde ira el anillos
                        mx = select.x
                        if mx + baseTable.length / 2 < 12:
                            destino = 0
                        elif mx + baseTable.length / 2 > 24:
                            destino = 2
                        else:
                            destino = 1
                        
                        #Evitar que salga del palo
                        while select.y < palos[origen].length and not scene.mouse.events:
                            rate(60)
                            select.y = scene.mouse.project(normal=vector(0, 0, 1)).y
                            select.x = palos[destino].x
                            
                            #Evita que el anillo se sobreponga a otros objetos
                            while select.y < len(pila[destino]) + 1 and not scene.mouse.events:
                                rate(60)
                                select.y = len(pila[destino]) + 1
                        
                        #Mueve el anillo junto con el mouse
                        select.pos = scene.mouse.project(normal=vector(0, 0, 1))
                        rate(60)
                    
                    #Si la pila tiene algun elemento
                    if len(pila[destino]) > 0:
                        
                        #Si es un movimiento legal
                        if pila[destino][-1].radius > select.radius:
                            select.x = palos[destino].x
                            select.y = 1 + len(pila[destino])
                            pila[destino].append(select)
                            
                            #Si el movimiento es a un palo diferente, se suma 1
                            if destino != origen:
                                mov.text = str(int(mov.text) + 1)
                                solu.text = str(int(solu.text) - 1)
                        
                        #Si no es un movimiento legal
                        else:
                            select.x = palos[origen].x
                            select.y = 1 + len(pila[origen])
                            pila[origen].append(select)
                    
                    #Si la pila no tiene nada   
                    else:
                        select.x = palos[destino].x
                        select.y = 1
                        pila[destino].append(select)
                        mov.text = str(int(mov.text) + 1)
                        solu.text = str(int(solu.text) - 1)
        
                #Si la pila 0 y 2 estan vacias, el juego fue terminado
                if pila[0] == [] and pila[1] == []:
                    text(text = "Juego finalizado", pos = (0, 0.7, 4), align = "center", color = color.white, font = "sans")
                    print "Juego finalizado en", mov.text, "movimientos"
                    
                    #Si se logro en la solucion optima
                    if int(solu.text) == 0:
                        text(text = "Felicidades, se logro la solucion optima!", pos = (0, -1, 6), align = "center", color = color.white, font = "sans")
                    
                    #Reacomodar la camara
                    scene.forward = (0, 0, -1)
                    
                    #Terminar
                    break