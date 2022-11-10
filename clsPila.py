

class Pila:
    def __init__(self):
        self.top=None
        self.stack=[]
    def getTop(self):
        return self.top
    def add(self,dato):
        self.top=dato
        self.stack.append(dato)
        return self.top
    def remove(self):
        #elimina el primer elemento de la pila
        self.stack.pop()
        #self.top ´pasa a ser el self.stack
        self.top= self.stack[-1]
        return self.top
    def __str__(self):
        return str(self.stack)
    def __len__(self):
        return len(self.stack)
    def devolverCarta(self,indice):
        for i in range(13):
            if(i==indice):
                return self.stack[i]