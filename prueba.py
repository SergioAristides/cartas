from pygame import *
import sys
init()

#dimenciones pantalla
WIDTH=800
HEIGTH=600
size= (WIDTH,HEIGTH)
screen = display.set_mode(size)
display.set_caption("mode")
#colores
BLACK =(0,0,0)
WHITE =(255,255,255)
GREEN =(0,255,0)
BLUE =(255,0,0)
RED =(0,0,255)
YELLOW =(216,255,0)
ORANGE =(255,131,0)
BROWN=(86,44,0)
GRIS=(206,200,194)
fondo=image.load("images/rfondo.png").convert()
fondo2=image.load("images/fondoPoker.jpg").convert()
#variable que mantiene el juego activo
isRunnig=True
#controlador de FPS
clock=time.Clock() 
#Fuente para los botones
myFont=font.SysFont("Pacifico",30)
mapa=Rect(650,60,110,60)
#pinta los botones
def pintarBoton(screen,color,boton,palabra):
    draw.rect(screen,color,boton)
    text=myFont.render(palabra,True,BLACK)
    screen.blit(text,(boton.x+(boton.width-text.get_width())/2,
                    boton.y+(boton.height-text.get_height())/2))
screen.blit(fondo2,[0,0])
while isRunnig:
    for e in event.get():
        if e.type == QUIT:
            isRunnig=False
        if(mapa.collidepoint(mouse.get_pos())):
            screen.blit(fondo2,[0,0])
    clock.tick(60)
quit()