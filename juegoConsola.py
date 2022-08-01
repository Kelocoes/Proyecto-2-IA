import mainProyecto2 as mp2
import numpy as np

def TurnoUsuario(posyInit, posxInit, posy, posx, tab):
    posibilidades = mp2.Sensor(posyInit, posxInit, tab)

    posPosibles = []
    for i in range(len(posibilidades)):
        if posibilidades[i][0] == 1:
            posyAct, posxAct = posibilidades[i][1] , posibilidades[i][2] 
            posPosibles.append([posyAct, posxAct])
    
    #print(posy,posx)
    #print(posPosibles)
    if [posy,posx] in posPosibles:
        print("Si es posible")
        return 1
    else:
        print("Movimiento erroneo")
        return 0

def BonitoTab(tab):
    print()
    print("  y/x  0 1 2 3 4 5 6 7")
    print()
    for i in range(len(tab)):
        print("", end  = "   " + str(i) + "   ")
        for j in range(len(tab[i])):
            print(tab[i][j], end = " ")
        print()
    print()

#amb = mp2.imp_amb('./ambiente.txt')


def Juego():
    tab = mp2.RNG()
    #tab = mp2.imp_amb('./ambiente.txt')

    for i in range(len(tab[0])):
        for j in range(len(tab[i])):
            if (tab[i][j] == 2):
                posyInitP = i
                posxInitP = j
            elif (tab[i][j] == 4):
                posyInitB = i
                posxInitB = j

    print("Hola, bienvenido a ajedrez raro")
    print("Seleccione la dificultad")
    print("1. Fácil")
    print("2. Normal")
    print("3. Difícil")
    dif = input("")
    if dif == "1":
        dif = 2
    elif dif == "2":
        dif = 4
    else:
        dif = 6
    
    print("Este es el tablero generado!")
    BonitoTab(tab)

    print("Comienza el bot!")
    
    posyNewB, posxNewB = mp2.Algoritmo(tab,dif)
    tab[posyInitB][posxInitB] = 0
    posyInitB = posyNewB
    posxInitB = posxNewB
    tab[posyNewB][posxNewB] = 4
    print("El robot movio a la posicion: " + str([posyNewB,posxNewB]))
    BonitoTab(tab)

    p1 = 0
    p2 = 0
    while(not(mp2.ganoAlguien(tab))):

        posy = input("Inserta la posicion en y\n")
        posx = input("Inserta la posicion en x\n")
        resul = TurnoUsuario(posyInitP,posxInitP,int(posy),int(posx),tab)
        if resul == 1:
            tab[posyInitP][posxInitP] = 0
            posyInitP = int(posy)
            posxInitP = int(posx)
            if (tab[posyInitP][posxInitP] == 1 or tab[posyInitP][posxInitP] == 3 or tab[posyInitP][posxInitP] == 5):
                p1 += tab[posyInitP][posxInitP] 
            tab[posyInitP][posxInitP] = 2
            BonitoTab(tab)

            if(not(mp2.ganoAlguien(tab))):
                #Turno bot
                posyNewB, posxNewB = mp2.Algoritmo(tab,dif)
                tab[posyInitB][posxInitB] = 0
                posyInitB = posyNewB
                posxInitB = posxNewB
                if (tab[posyInitB][posxInitB] == 1 or tab[posyInitB][posxInitB] == 3 or tab[posyInitB][posxInitB] == 5):
                    p2 += tab[posyInitB][posxInitB] 
                tab[posyNewB][posxNewB] = 4
                print("El robot movio a la posicion: " + str([posyInitB,posxInitB]))
                BonitoTab(tab)
            else:
                break
        else:
            BonitoTab(tab)
    print(p1, p2)
    if (p1 > p2):
        print("El ganador fuiste tú!!")
    elif (p1 < p2):
        print("El ganador fue el bot :P")
    else:
        print("Empate!!")

Juego()

