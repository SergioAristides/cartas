from pygame import *
from clsCarta import Carta
from clsPila import Pila
import sys
init()

#dimenciones pantalla
WIDTH=800
HEIGTH=600
size= (WIDTH,HEIGTH)
screen = display.set_mode(size)
display.set_caption("cartas")
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
#variable que mantiene el juego activo
isRunnig=True
#controlador de FPS
clock=time.Clock() 
#Fuente para los botones
myFont=font.SysFont("Pacifico",30)
#imagen de fondo
fondo=image.load("Images/fondoPoker.jpg").convert()


#instancias de las pilas
pila1=Pila()
pila2=Pila()
#agregar las cartas a las pilas
for i in range(14):
    if(i<7):
        carta=Carta("Images/"+str(i+1)+".png")
        pila1.add(carta)
    else:
        carta=Carta("Images/"+str(i+1)+".png")
        pila2.add(carta)
#coordenadas cartas iniciales
x=60
y=60

#dibuja las cartas 
def drawPokerPilas(pila_uno,pila_dos,x,y):
    """_summary_

    Args:
        pila_uno (_type_): _description_
        pila_dos (_type_): _description_
        x (_type_): _description_
        y (_type_): _description_
    """    
    for i in range(7):
        pila_uno.devolverCarta(i).rect.x=x
        pila_uno.devolverCarta(i).rect.y=y
        screen.blit(pila_uno.devolverCarta(i).image,
                        [pila_uno.devolverCarta(i).rect.x,pila_uno.devolverCarta(i).rect.y])
        y+=50
    
    for j in range(7):
        if(j==0):
            x=300
            y=60
        pila_dos.devolverCarta(j).rect.x=x
        pila_dos.devolverCarta(j).rect.y=y
        screen.blit(pila_dos.devolverCarta(j).image,
                        [pila_dos.devolverCarta(j).rect.x,pila_dos.devolverCarta(j).rect.y])

        y+=50  
#pinta los botones
def pintarBoton(screen,color,boton,palabra):
    draw.rect(screen,color,boton)
    text=myFont.render(palabra,True,BLACK)
    screen.blit(text,(boton.x+(boton.width-text.get_width())/2,
                    boton.y+(boton.height-text.get_height())/2))

#coordenadas de los botones
pila=Rect(500,60,110,60)
cola=Rect(500,180,110,60)
arbol=Rect(500,300,110,60)
grafo=Rect(500,420,110,60)


screen.blit(fondo,[0,0])
while isRunnig:
    for e in event.get():
        if e.type == QUIT:
            isRunnig=False
        #cuando se presiona    
        if e.type==MOUSEBUTTONDOWN and e.button==1:
            if pila.collidepoint(mouse.get_pos()):
                drawPokerPilas(pila1,pila2,x,y)   
        #Se deja de presionar
        if e.type==MOUSEBUTTONUP:
            pass   
    pintarBoton(screen,GRIS,pila,"Pila")
    pintarBoton(screen,GRIS,cola,"Cola")
    pintarBoton(screen,GRIS,arbol,"Arbol")
    pintarBoton(screen,GRIS,grafo,"Grafo")
    y=60
    x=60
    display.flip()
    clock.tick(60)
quit()