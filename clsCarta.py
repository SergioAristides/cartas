from pygame import *    
class Carta(sprite.Sprite):
    def __init__(self,string):
        super().__init__()
        self.image=image.load(string).convert()
        self.image=transform.scale(self.image,(80,160))
        #self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
