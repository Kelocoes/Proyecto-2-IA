import pygame as p

import mainProyecto2 as mp2
from Gameover import draw_text
from Gameover import main_menu
import time
##############################################################################
## CONFIGURACION DE LA VENTANA Y CASILLAS ####################################

dif = 0
#tab = mp2.RNG()
tab = mp2.imp_amb('./maze.txt')
WIDTH = HEIGHT = 512
WIDTHSCR = 750
DIMENSION = len(tab)
CAS_TAM = HEIGHT // DIMENSION ## tamaño de casilla 
MAX_FPS = 15
IMAGES = {}

##############################################################################
## Dibujar objetos en la pantalla ############################################
##############################################################################

def dibujarGameStatus(screen, posPosibles, p1, p2, turno):
    dibujarTablero(screen, posPosibles)
    dibujarObjetos(screen)
    dibujarLateral(screen, p1, p2, turno)

## Funcion que pinta las casillas del tablero
def dibujarTablero(screen, posPosibles): 
    colors = [p.Color("#437a41"), p.Color("#64a055")] ## alterna entre los dos verdes
    ## Pinta todo el tablero alternando entre dos verdes
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            color = colors[((i+j) % 2)]
            p.draw.rect(screen, color, p.Rect(j*CAS_TAM, i*CAS_TAM, CAS_TAM, CAS_TAM))
    ## (ilumina) indica aquellas casillas a las que el usuario puede moverse
    for i in posPosibles:
        p.draw.rect(screen, p.Color('#4d553d'), p.Rect(i[1]*CAS_TAM, i[0]*CAS_TAM, CAS_TAM, CAS_TAM))
    
## Function que tiene en cuenta los objetos 1, 2, 3, 4, 5 en el tablero 
def dibujarObjetos(screen): 
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            objeto = tab[i][j]
            if objeto != 0: ## No es casilla vacia? Entonces puede ser  1, 2, 3, 4, 5 (casillas con objeto)
                screen.blit(IMAGES[str(objeto)], p.Rect(j*CAS_TAM, i*CAS_TAM, CAS_TAM, CAS_TAM))

## Funcion que pinta la barra lateral de informacion
def dibujarLateral(screen, p1, p2, turno):
    font = p.font.SysFont(None, 30)
    draw_text('S T A T U S', font, p.Color('white'), screen, 570, 50)
    if (turno == 0):
        draw_text('Estado inicial', font, p.Color('white'), screen, 540, 100)
    elif (turno == 1):
        draw_text('Turno del bot', font, p.Color('white'), screen, 540, 100)
        screen.blit(IMAGES[str(4)], p.Rect(600, 160, 50, 50))
    else: 
        draw_text('Turno del jugador', font, p.Color('white'), screen, 540, 100)
        screen.blit(IMAGES[str(2)], p.Rect(600, 160, 50, 50))
    draw_text(' - - - ', font, p.Color('white'), screen, 600, 250)
    draw_text('P U N T A J E', font, p.Color('white'), screen, 550, 300)
    screen.blit(IMAGES[str(2)], p.Rect(550, 360, 50, 50))
    draw_text('P1: ', font, p.Color('white'), screen, 600, 370)
    draw_text(str(p1), font, p.Color('white'), screen, 660, 370)
    screen.blit(IMAGES[str(4)], p.Rect(550, 400, 50, 50))
    draw_text('BOT:', font, p.Color('white'), screen, 600, 410)
    draw_text(str(p2), font, p.Color('white'), screen, 660, 410)

##############################################################################
##############################################################################

def loadImages():
    objetos = ['1', '2', '3', '4', '5']
    for i in objetos:
        IMAGES[i] = p.image.load('./images/'+i+'.png')

def general(): 
    p.init()
    screen = p.display.set_mode((WIDTHSCR, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('#733735'))
    loadImages()
    posyInitP, posxInitP, posyInitB, posxInitB, dif, turno = Comenzar()
    p1 = p2 = 0
    running = True
    posPosibles = []
    while running:
        ## Turno del Bot
        screen.fill((0, 0, 0))
        if (turno == 1):
            posyNewB, posxNewB = mp2.Algoritmo(tab,dif)
            tab[posyInitB][posxInitB] = 0
            posyInitB = posyNewB
            posxInitB = posxNewB
            if (tab[posyInitB][posxInitB] == 1 or tab[posyInitB][posxInitB] == 3 or tab[posyInitB][posxInitB] == 5):
                p2 += tab[posyInitB][posxInitB] 
            tab[posyNewB][posxNewB] = 4
            ## print("El robot movio a la posicion: " + str([posyInitB,posxInitB]))
            if (mp2.ganoAlguien(tab)):
                running= False
                break
            else: 
                turno = 2 ## se pasa el turno al jugador 

        ## FUNCION INTERMEDIA ILLUMINATE: Se encarga de resaltar aquellas casillas a las que el jugador podria ir, setea posPosibles       
        elif (turno == 2):
            posPosibles = Iluminate(posyInitP, posxInitP, screen)
            turno = 3
        ## Turno del jugador: Depende de evento del mouse ->
        elif (turno == 3):
            for e in p.event.get():
                if e.type == p.QUIT:
                    running: False
                    p.quit()
                    exit()
                elif e.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos() ## (x,y)
                    posx = location[0] // CAS_TAM
                    posy = location[1] // CAS_TAM
                    
                    if [posy, posx] in posPosibles:
                        #print('Posible!')
                        ## Se realiza el respectivo movimiento
                        tab[posyInitP][posxInitP] = 0
                        posyInitP = int(posy)
                        posxInitP = int(posx)
                        if (tab[posyInitP][posxInitP] == 1 or tab[posyInitP][posxInitP] == 3 or tab[posyInitP][posxInitP] == 5):
                            p1 += tab[posyInitP][posxInitP] 
                        tab[posyInitP][posxInitP] = 2
                        posPosibles = [] ## Se resetea posPosibles para poder desmarcar aquellas casillas resaltadas
                        if (mp2.ganoAlguien(tab)):
                            running= False
                            break
                        else: 
                            turno = 1
                    #else: 
                        #print('No posible')
            
        clock.tick(MAX_FPS)
        dibujarGameStatus(screen, posPosibles, p1, p2, turno)
        if (turno == 0):
            dibujarGameStatus(screen, posPosibles, p1, p2, turno)
            p.display.flip()   
            p.time.wait(5000)
            #print("hola")
            turno = 1 
        p.display.flip()   
    
    ##print(p1, p2)
    p.init()
    if (p1 > p2):
        main_menu(2, p1, p2)
    elif (p1 < p2):
        main_menu(4, p1, p2)
    else:
        main_menu(6, p1, p2)
        
##############################################################################
########################## --- Gameplay --- ##################################

def Comenzar():
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
    return posyInitP, posxInitP, posyInitB, posxInitB, dif, 0

def Iluminate(posyInit, posxInit, screen): 

    posibilidades = mp2.Sensor(posyInit, posxInit, tab)
    posPosibles = []
    for i in range(len(posibilidades)):
        if posibilidades[i][0] == 1:
            posyAct, posxAct = posibilidades[i][1] , posibilidades[i][2] 
            posPosibles.append([posyAct, posxAct])
    return posPosibles

        


##############################################################################
if __name__ == "__main__":
    general()
  