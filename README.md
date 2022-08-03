# Proyecto-2-IA

# Pasos para utilizarlo
Si deseas ejecutar nuestro juego, solo tienes que escribir en tu terminal lo siguiente:

    python tablero.py

O simplemente ejecutar el archivo mencionado anteriormente.

Recuerda tener python instalado al igual que la librería de pygame.

# Heuristica

La heuristica de este programa toma en cuenta 4 factores: 

    La distancia de manhattan desde el bot a todos los items del tablero (MHT)
    
    El puntaje en los posibles estados del tablero (PNT)
    
    La posicion de ventaja en los posibles estados del tablero, entiendase por posicion de ventaja
    una posicion en la cual es posible obtener mas puntaje (VT)
    
    Los turnos hasta dicho estado del tablero (T)
    
    La heuristica tambien es calculada para las hipoteticas posiciones del jugador, y se resta a la heuristica del bot
    para tener en cuenta las posibles jugadas maestras del jugador
    
    Heuristica del jugador (HJ)
    Heuristica del bot (HB)
    Heuristica total (HT)
    
    HJ = PNT*0.7 + VT*0.15 - MHT*0.05
    HB = PNT*0.7 + VT*0.15 - MHT*0.05
    
    HT = (HB - HJ) - T*0.1
    
    
    
