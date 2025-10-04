class trojkat():
    def __init__(self,a,b,c,h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def obwod(self):
        O = self.a + self.b + self.c
        print(f"Obwód: {O}")
    def pole(self):
        P = (self.a * self.h )/2
        print(f"Pole: {P}")
        
        
trojkat1 = trojkat(5,6,9,2); trojkat1.obwod(); trojkat1.pole()

PI = 3.14

class Figura():
    def __init__(self,pole,obwod):
        self.Pole = pole
        self.Obwod = pole
        pole = 0
        pbwod = 0
    def wyswietlObwod(self):
        print(self.Obwod)
    def wyswietlPole(self):
        print(self.Pole)
        
class Kolo(Figura):
    def __init__(self, r):
        super.__init__(self)
        self.promien = r
 
    def obliczPole(self):
        self.Pole = PI * self.promien * self.promien
        self.wyswietlPole(self)
    def obliczObwod(self):
        self.Obwod = 2 * PI * self.promien
        self.wyswietlObwod(self)
    
 
class Prostokat(Figura):
    def __init__(self, x, y):
        super.__init__(self)
        self.x = x
        self.y = y
        
        # self.pole = x*y
        # self.obwod = 2*x + 2*y
    
    
    def obliczPole(self):
        self.Pole = self.x * self.y
        self.wyswietlPole(self)
    
    def obliczObwod(self):
        self.Obwod = 2*self.x + 2*self.y
        self.wyswietlPole(self)
        