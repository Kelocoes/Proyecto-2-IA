import pygame, sys

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)
 
font = pygame.font.SysFont(None, 40)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu(player, puntaje1, puntaje2):
    while True:
 
        screen.fill((100, 149, 237))
        draw_text('GANADOR', font, pygame.Color('#733735'), screen, 280, 50)
        zanahoria = pygame.image.load('./images/1.png')
        pikachu = pygame.image.load('./images/2.png')
        squirtle = pygame.image.load('./images/4.png')
        
        mensaje = ''
        if (player == 2):
            mensaje = 'Jugador 1'
            screen.blit(zanahoria, pygame.Rect(240, 150, 50, 50))
            screen.blit(pikachu, pygame.Rect(330, 150, 50, 50))
            screen.blit(zanahoria, pygame.Rect(410, 150, 50, 50))
            
        elif (player == 4):
            mensaje = '*** BOT ***'
            screen.blit(zanahoria, pygame.Rect(240, 150, 50, 50))
            screen.blit(squirtle, pygame.Rect(330, 150, 50, 50))
            screen.blit(zanahoria, pygame.Rect(410, 150, 50, 50))
        else: 
            mensaje = 'Empate'
            screen.blit(squirtle, pygame.Rect(260, 150, 50, 50))
            screen.blit(pikachu, pygame.Rect(380, 150, 50, 50))

        screen.blit(pikachu, pygame.Rect(250, 350, 50, 50))
        screen.blit(squirtle, pygame.Rect(250, 400, 50, 50))
        
        draw_text(mensaje, font, pygame.Color('#733735'), screen, 280, 250)
        draw_text('PUNTAJES', font, (0, 0, 0), screen, 280, 300)
        
        draw_text('Jugador 1:', font, pygame.Color('#733735'), screen, 300, 360)
        draw_text(str(puntaje1), font, pygame.Color('white'), screen, 450, 360)
        draw_text('Bot: ', font, pygame.Color('#733735'), screen, 300, 410)
        draw_text(str(puntaje2), font, pygame.Color('white'), screen, 450, 410)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
 
        pygame.display.update()
        mainClock.tick(60)
 