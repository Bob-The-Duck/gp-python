import math

class pole_i_obwod_kola():
    def __init__(self,r:float):
        self.r = r
    def pole(self):
        print(f"Pole koła: {self.r * self.r * math.pi:.2f}")
    def obwod(self):
        print(f"Pole koła: {2 *  math.pi * self.r:.2f}")

kolo = pole_i_obwod_kola(5) ; kolo.pole() ; kolo.obwod()