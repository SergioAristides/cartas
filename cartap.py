from pygame import *    
class Cartap:
    
    def __init__(self,*args):
        if len(args)==0:
            self.image=None
            self.rect=None
        if len(args)==3:
            self.image=image.load(args[0]).convert()
            self.image=transform.scale(self.image,(90,110))
            self.rect=Rect(args[1],args[2],90,110)
    def getRect(self):
        return self.rect
    def setRect(self,x,y):
        self.rect[0]=x
        self.rect[1]=y
    def getRectY(self):
        return self.rect[1]
    def getRectX(self):
        return self.rect[0]