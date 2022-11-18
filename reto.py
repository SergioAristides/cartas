from pygame import *
from cartap import Cartap
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


#coordenadas cartas iniciales
x=60
y=60
#instancias de las pilas
pila1=Pila()
pila2=Pila()


#agregar las cartas a las pilas
for i in range(14):
    if(i<7):
        carta=Cartap("Images/"+str(i+1)+".png",x,y)
        pila1.add(carta)

    else:
        carta=Cartap("Images/"+str(i+1)+".png",x,y)
        pila2.add(carta)



#dibuja las cartas 
def drawPokerPilas(x,y): 
    for i in range(pila1.size):
        pila1.devolverCarta(i).setRect(x,y)
        #recorrerPilas(pila_uno,pila_dos)
        screen.blit(pila1.devolverCarta(i).image,
                        [pila1.devolverCarta(i).getRectX(),pila1.devolverCarta(i).getRectY()])
        y+=50
        
    for j in range(pila2.size):
        if(j==0):
            x=300
            y=60
        pila2.devolverCarta(j).setRect(x,y)
        #recorrerPilas(pila_uno,pila_dos)
        screen.blit(pila2.devolverCarta(j).image,
                        [pila2.devolverCarta(j).getRectX(),pila2.devolverCarta(j).getRectY()])
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

#
cartica_movible=None
def recorrerPilas(x,y):
    cartica_movible=None
    if(pila1.getTop().rect.collidepoint(mouse.get_pos())):
        cartica_movible=pila1.getTop()
        drawPokerPilas(x,y)
        pila1.remove()
                
                #drawCartae(carta_movible)
                #drawCartae(cartica_movible)
    if(pila2.getTop().rect.collidepoint(mouse.get_pos())):
        cartica_movible=pila2.getTop() 
        drawPokerPilas(x,y)
        pila2.remove()
    return cartica_movible


    
def drawCartae(a):
    a.x, a.y = mouse.get_pos()
    screen.blit(a.image, (a.x, a.y ))    
screen.blit(fondo,[0,0])
x1=60
y1=60
cartica=None
bandera=False
bandera2=False
colicion=False
while isRunnig:
    for e in event.get():
        if e.type == QUIT:
            isRunnig=False
        #cuando se presiona    
        if e.type==MOUSEBUTTONDOWN:
            if pila1.getTop().rect.collidepoint(mouse.get_pos())  and bandera == True and cartica!=None or pila2.getTop().rect.collidepoint(mouse.get_pos()) and bandera == True and cartica!=None:
                print("entreeee")
                colicion=True
                if(pila1.getTop().rect.collidepoint(mouse.get_pos())):
                    pila1.add(cartica)
                    cartica=None
                if(pila2.getTop().rect.collidepoint(mouse.get_pos())):
                    pila2.add(cartica)
                    cartica=None
                print("colicion")
            if pila1.getTop().rect.collidepoint(mouse.get_pos()) or pila2.getTop().rect.collidepoint(mouse.get_pos()):
                bandera=False 
            if pila1.getTop().rect.collidepoint(mouse.get_pos()) and bandera==False or pila2.getTop().rect.collidepoint(mouse.get_pos()) and bandera==False:
                cartica=recorrerPilas(x1,y1)
                bandera=True
            
            if pila.collidepoint(mouse.get_pos()):
                drawPokerPilas(x1,y1) 
                print(i)
                bandera2=True
                i+=1

            
    screen.blit(fondo,[0,0])
    if bandera2:
        drawPokerPilas(x1,y1)


    if(cartica!=None and bandera):
        drawCartae(cartica)
        pass
    pintarBoton(screen,GRIS,pila,"Pila")
    pintarBoton(screen,GRIS,cola,"Cola")
    pintarBoton(screen,GRIS,arbol,"Arbol")
    pintarBoton(screen,GRIS,grafo,"Grafo")
    x1=60
    y1=60
    display.flip()
    clock.tick(60)
quit()