import numpy as np
import random as rm

#Retorna el laberinto como lista de listas
def imp_amb(arch):
    file = open(arch, "r")
    maze = [[int(j) for j in i.split(" ")] for i in file]
    return maze

def Sensor(posy, posx, tab):
    # 0 No mueve  1 Mueve

    """
    0   a1  0   a2  0
    a0  0   0   0   a3
    0   0  2-4  0   0
    a4  0   0   0   a7
    0   a5  0   a6  0
    """
    a0 = (0,posy,posx)
    if posx-2 >= 0 and posy-1 >= 0 and tab[posy-1][posx-2] != 4 and tab[posy-1][posx-2] != 2:
        a0 = (1,posy-1,posx-2)
    a1 = (0,posy,posx)
    if posx-1 >= 0 and posy-2 >= 0 and tab[posy-2][posx-1] != 4 and tab[posy-2][posx-1] != 2:
        a1 = (1,posy-2,posx-1)
    a2 = (0, posy, posx)
    if posx+1 < len(tab) and posy-2 >= 0 and tab[posy-2][posx+1] != 4 and tab[posy-2][posx+1] != 2:
        a2 = (1,posy-2,posx+1)
    a3 = (0,posy,posx)
    if posx+2 < len(tab) and posy-1 >= 0 and tab[posy-1][posx+2] != 4 and tab[posy-1][posx+2] != 2:
        a3 = (1,posy-1,posx+2)
    a4 = (0, posy, posx)
    if posx-2 >= 0 and posy+1 < len(tab) and tab[posy+1][posx-2] != 4 and tab[posy+1][posx-2] != 2:
        a4 = (1,posy+1,posx-2)
    a5 = (0, posy, posx)
    if posx-1 >= 0 and posy+2 < len(tab) and tab[posy+2][posx-1] != 4 and tab[posy+2][posx-1] != 2:
        a5 = (1,posy+2,posx-1)
    a6 = (0, posy, posx)
    if posx+1 < len(tab) and posy+2 < len(tab) and tab[posy+2][posx+1] != 4 and tab[posy+2][posx+1] != 2:
        a6 = (1,posy+2,posx+1)
    a7 = (0, posy, posx)
    if posx+2 < len(tab) and posy+1 < len(tab) and tab[posy+1][posx+2] != 4 and tab[posy+1][posx+2] != 2:
        a7 = (1,posy+1,posx+2)
    
    
    arr = [a0, a1, a2, a3, a4, a5, a6, a7]

    return arr

def puntajeMYC(maze, posY, posX):
    manhattanTotal = 0
    posPosibles = Sensor(posY, posX, maze)
    arrComidaInmediata = []
    #print(posPosibles)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (maze[i][j] == 1 or maze[i][j] == 3 or maze[i][j] == 5):
                manhattanTotal = manhattanTotal + ( abs(i - posY) + abs(j - posX))/3 * maze[i][j]
                for k in posPosibles:
                    #print(k[1],k[2],i,j)
                    if k[0] == 1 and k[1] == i and k[2] == j:
                        arrComidaInmediata.append( (maze[i][j], i, j) )

    arrComidaInmediata.sort(reverse=True)
    #print(arrComidaInmediata)
    if (len(arrComidaInmediata) > 0):
        return (manhattanTotal, arrComidaInmediata[0][0]*2)
    else: 
        return (manhattanTotal, 0)

def fHeuristica(maze, pntMin, pntMax, profund):
    hMax = 0
    hMin = 0

    mTotalMax = 0
    pInmediatoMax = 0

    mTotalMin = 0
    pInmediatoMin = 0


    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (maze[i][j] == 2):
                posMinY = i
                posMinX = j
                mTotalMin, pInmediatoMin = puntajeMYC(maze,posMinY,posMinX)
            elif (maze[i][j] == 4):
                posMaxY = i
                posMaxX = j
                mTotalMax, pInmediatoMax = puntajeMYC(maze,posMaxY,posMaxX)

    #print(pInmediatoMax,pntMax,mTotalMax)
    hMax = pInmediatoMax*0.15 + pntMax*0.7  - mTotalMax*0.05  

    #print(pInmediatoMin,pntMin,mTotalMin)
    hMin = pInmediatoMin*0.15 + pntMin*0.7  - mTotalMin*0.05

    return (hMax - hMin) - profund*0.1 

def ganoAlguien(amb):
    np_amb = np.array(amb)

    if ((np_amb != 0).sum() - 2) == 0:
        return True
    else:
        return False

def Algoritmo(tab,profMax):
    amb = [row[:] for row in tab]

    # Ambiente, profundidad, valorMinMax, puntajeUser, puntajeBot, posPadreY, posPadreX, rangoHijos
    minMax = [[[amb,0,0,0,0,-1,-1, [0,0]]]] # MAX

    aux = 0

    while (aux < profMax ):
        
        minMax.append([]) #Nueva profundidad

        #print(str(aux) + " " + str(len(minMax[aux])))
        
        for posPadreX in range(len(minMax[aux])):
            nodoPadre = minMax[aux][posPadreX]
            
            if not(ganoAlguien(nodoPadre[0])):
                for i in range(len(nodoPadre[0])):
                    for j in range(len(nodoPadre[0][i])):
                        if (nodoPadre[0][i][j] == 2):
                            posMinY = i
                            posMinX = j
                        elif (nodoPadre[0][i][j] == 4):
                            posMaxY = i
                            posMaxX = j

                if aux % 2 != 0:
                    posibilidades = (Sensor(posMinY,posMinX, nodoPadre[0] ))
                    np_posibilidades = np.array(posibilidades)
                    minMax[aux][posPadreX][7] = [len(minMax[aux + 1]), len(minMax[aux + 1]) + (np_posibilidades[:,0] != 0).sum() - 1]
                    for k in range(len(posibilidades)): #[0, 0, 0, 0, 1, 1, 1, 0]
                        if (posibilidades[k][0] == 1):
                            newAmb = [row[:] for row in nodoPadre[0]]
                            posyAct, posxAct = posibilidades[k][1] , posibilidades[k][2]
                            puntaje = newAmb[posyAct][posxAct]
                            newAmb[posyAct][posxAct] = 2 
                            newAmb[posMinY][posMinX] = 0
                            minMax[aux + 1].append([newAmb, aux + 1, fHeuristica(newAmb, nodoPadre[3] + puntaje, nodoPadre[4], aux), nodoPadre[3] + puntaje, nodoPadre[4], aux, posPadreX, []])
                else:
                    posibilidades = (Sensor(posMaxY,posMaxX, nodoPadre[0] )) 
                    np_posibilidades = np.array(posibilidades)
                    minMax[aux][posPadreX][7] = [len(minMax[aux + 1]), len(minMax[aux + 1]) + (np_posibilidades[:,0] != 0).sum() - 1]
                    for k in range(len(posibilidades)): #[0, 0, 0, 0, 1, 1, 1, 0]
                        if (posibilidades[k][0] == 1):
                            newAmb = [row[:] for row in nodoPadre[0]]
                            posyAct, posxAct = posibilidades[k][1] , posibilidades[k][2]
                            puntaje = newAmb[posyAct][posxAct]
                            newAmb[posyAct][posxAct] = 4 
                            newAmb[posMaxY][posMaxX] = 0
                            minMax[aux + 1].append([newAmb, aux + 1, fHeuristica(newAmb, nodoPadre[3], nodoPadre[4] + puntaje, aux) , nodoPadre[3] , nodoPadre[4] + puntaje, aux, posPadreX, []])
        
        aux += 1
    
    #for i in range(len(minMax)):
    #    print("Profundidad: " + str(i) + " Nodos: " + str(len(minMax[i])))
    
    
    #Para mostra los tableros de los nodos

    #Para mostrar los valores minimax de los nodos 

    valHijos = []
    #Subida de los valores heurísticos o de las hojas hasta el nodo inicial
    for i in range(len(minMax) - 2, -1, -1):
        for j in range(len(minMax[i])):
            if len(minMax[i][j][7]) != 0:
                valHijos = [minMax[i+1][k][2] for k in range(minMax[i][j][7][0],minMax[i][j][7][1] + 1)]
            #El siguiente if tiene que estar dentro
                if len(valHijos) != 0:
                    if (i % 2 != 0): #Si es par es porque toca aplicar min a cada uno de los hijos de los nodos
                        minMax[i][j][2] = min(valHijos)
                    else:
                        minMax[i][j][2] = max(valHijos)

    #Muestra el arbol minimax solo con los valores 

    #Seleccionar la mejor opción para el robot
    valorRaiz = minMax[0][0][2] 
    for i in range(len(minMax[1])):
        if valorRaiz == minMax[1][i][2]:
            nodoPadre = minMax[1][i]
            for i in range(len(nodoPadre[0])):
                for j in range(len(nodoPadre[0][i])):
                    if (nodoPadre[0][i][j] == 4):
                        valorMax = [i,j]
                        break
            break

    print("Jugada maestra: " + str(valorMax) + " " + str(valorRaiz))
    return valorMax[0], valorMax[1]

#amb = imp_amb('./ambiente.txt')

#Algoritmo(amb,2)