import numpy as np


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
    if posx-1 >= 0 and posy-2 >= 0 and tab[posy-2][posx-1] != 4 and tab[posy-1][posx-2] != 2:
        a1 = (1,posy-2,posx-1)
    a2 = (0, posy, posx)
    if posx+1 < len(tab) and posy-2 >= 0 and tab[posy-2][posx+1] != 4 and tab[posy-1][posx-2] != 2:
        a2 = (1,posy-2,posx+1)
    a3 = (0,posy,posx)
    if posx+2 < len(tab) and posy-1 >= 0 and tab[posy-1][posx+2] != 4 and tab[posy-1][posx-2] != 2:
        a3 = (1,posy-1,posx+2)
    a4 = (0, posy, posx)
    if posx-2 >= 0 and posy+1 < len(tab) and tab[posy+1][posx-2] != 4 and tab[posy-1][posx-2] != 2:
        a4 = (1,posy+1,posx-2)
    a5 = (0, posy, posx)
    if posx-1 >= 0 and posy+2 < len(tab) and tab[posy+2][posx-1] != 4 and tab[posy-1][posx-2] != 2:
        a5 = (1,posy+2,posx-1)
    a6 = (0, posy, posx)
    if posx+1 < len(tab) and posy+2 < len(tab) and tab[posy+2][posx+1] != 4 and tab[posy-1][posx-2] != 2:
        a6 = (1,posy+2,posx+1)
    a7 = (0, posy, posx)
    if posx+2 < len(tab) and posy+1 < len(tab) and tab[posy+1][posx+2] != 4 and tab[posy-1][posx-2] != 2:
        a7 = (1,posy+1,posx+2)
    
    
    arr = [a0, a1, a2, a3, a4, a5, a6, a7]

    return arr

def Mover(dir,posy,posx):
    if dir == 0:
        posyActual = posy-1
        posxActual = posx-2
    elif dir == 1:
        posyActual = posy-2
        posxActual = posx-1
    elif dir == 2:
        posyActual = posy-2
        posxActual = posx+1
    elif dir == 3:
        posyActual = posy-1
        posxActual = posx+2
    elif dir == 4:
        posyActual = posy+1
        posxActual = posx-2
    elif dir == 5:
        posyActual = posy+2
        posxActual = posx-1
    elif dir == 6:
        posyActual = posy+2
        posxActual = posx+1
    elif dir == 7:
        posyActual = posy+1
        posxActual = posx+2

    return posyActual, posxActual

tab =  [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,3,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

#print(Sensor(2,2,tab))

def TurnoUsuario(posyInit, posxInit, posy, posx, tab):
    posibilidades = Sensor(posyInit, posxInit, tab)

    posPosibles = []
    for i in range(len(posibilidades)):
        if posibilidades[i] == 1:
            posyAct, posxAct = Mover(i+1,posyInit,posxInit)
            posPosibles.append([posyAct, posxAct])
        else:
            posPosibles.append(0)
    
    print(posy,posx)
    print(posPosibles)
    if [posy,posx] in posPosibles:
        print("Si es posible")
        return 1
    else:
        print("Movimiento erroneo")
        return 0

"""
print(np.array(tab))
posyInit = 2
posxInit = 2
while(1):
    posy = input("Inserta la posicion en y\n")
    posx = input("Inserta la posicion en x\n")
    resul = TurnoUsuario(posyInit,posxInit,int(posy),int(posx),tab)
    if resul == 1:
        tab[posyInit][posxInit] = 0
        posyInit = int(posy)
        posxInit = int(posx)
        tab[posyInit][posxInit] = 3
    print(np.array(tab))
"""


def Algoritmo(amb,profMax):

    # Ambiente, profundidad, valorMinMax, puntajeUser, puntajeBot 
    minMax = [[[amb,0,0,0,0,-1,-1]]] # MAX

    aux = 0

    while (aux < 10):
        
        minMax.append([]) #Nueva profundidad

        print(str(aux) + " " + str(len(minMax[aux])))
        for i in range(len(minMax[aux])):
            nodoPadre = minMax[aux][i]
            
            for i in range(len(nodoPadre[0])):
                for j in range(len(nodoPadre[0][i])):
                    if (nodoPadre[0][i][j] == 2):
                        posMinY = i
                        posMinX = j
                    elif (nodoPadre[0][i][j] == 4):
                        posMaxY = i
                        posMaxX = j

            if aux % 2 == 0:
                posibilidades = (Sensor(posMinY,posMinX, nodoPadre[0] )) 
                for k in range(len(posibilidades)): #[0, 0, 0, 0, 1, 1, 1, 0]
                    if (posibilidades[k][0] == 1):
                        newAmb = [row[:] for row in nodoPadre[0]]
                        posyAct, posxAct = posibilidades[k][1] , posibilidades[k][2]
                        puntaje = newAmb[posyAct][posxAct]
                        newAmb[posyAct][posxAct] = 2 
                        newAmb[posMinY][posMinX] = 0
                        minMax[aux + 1].append([newAmb, aux + 1, 0, nodoPadre[3] + puntaje, nodoPadre[4], aux, i])
            else:
                posibilidades = (Sensor(posMaxY,posMaxX, nodoPadre[0] )) 
                for k in range(len(posibilidades)): #[0, 0, 0, 0, 1, 1, 1, 0]
                    if (posibilidades[k][0] == 1):
                        newAmb = [row[:] for row in nodoPadre[0]]
                        posyAct, posxAct = posibilidades[k][1] , posibilidades[k][2]
                        puntaje = newAmb[posyAct][posxAct]
                        newAmb[posyAct][posxAct] = 4 
                        newAmb[posMaxY][posMaxX] = 0
                        minMax[aux + 1].append([newAmb, aux + 1, 0, nodoPadre[3] , nodoPadre[4] + puntaje, aux, i])
        
        aux += 1
    """
    for i in range(len(minMax)):
        print("PROFUNDIDAD " + str(i))
        print(len(minMax[i]))

    for i in range(len(minMax)):
        print("PROFUNDIDAD " + str(i))
        for j in range(len(minMax[i])):
            nodo = minMax[i][j]
            print(np.array(nodo[0]))
    """
    
"""
for i in profundidad:
    if 0 par?: max
        posibilidades(min).append
    if i impar?: min
"""

amb = imp_amb('./ambiente.txt')

Algoritmo(amb,1)