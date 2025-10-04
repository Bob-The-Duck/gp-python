class Zwierze():
    def __init__(self,wiek,imie):
        self.wiek = wiek ; self.imie = imie
        
    def wydajeDzwiek(self):
        print(f"{self.imie} Wydał dzwięk")
    
    def jedz(self):
        print(f"{self.imie} Zjadł plastelinę")
    
class Pies(Zwierze):
    def __init__(self,wiek,imie,rasa):
        super().__init__(wiek,imie)
        self.rasa = rasa
    def wypiszRase(self):
        print(f"{self.imie} jest roasowym kundlem, a dokładniej {self.rasa}")


class Kot(Zwierze):
    def __init__(self,wiek,imie,rasa):
        super().__init__(wiek,imie)
        self.rasa = rasa
    def wypiszRase(self):
        print(f"{self.imie} jest roasowym dachowcem, a dokładniej {self.rasa}")
        
'''Stworzyć klasę Ptak i dodać metodę lec(), klasa ma dziedziczyć po klasie
Zwierze, oraz dodać kolejna klasę Orzel, dziedziczaca po Ptak, która ma
mieć metodę poluj(), w której wywołujemy metodę lec() z klasy nadrzędnej.
Następnie tworzymy obiekt klasy Orzel i wywołajmy wszystkie metody:'''   

class Ptak(Zwierze):
    def __init__(self,wiek,imie):
        super().__init__(wiek,imie)
    def lec(self):
        print(f"{self.imie} Polecioł")
        
class Orzel(Ptak):
    def __init__(self,wiek,imie):
        super().__init__(wiek,imie)
    def poloj(self):
        Ptak.lec(self)
        print(f"{self.imie} Zapolował")