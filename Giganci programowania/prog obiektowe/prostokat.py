class obwod_i_pole_prostokata():
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y
    def oblicz(self):
        print(f"Obwód: {self.x * 2 + self.y * 2}")
        print(f"Pole: {self.x * self.y}")

prostokat = obwod_i_pole_prostokata(2,3) ; prostokat.oblicz()