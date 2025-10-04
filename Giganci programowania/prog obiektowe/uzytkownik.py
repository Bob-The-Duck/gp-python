class uzytkownik:
    imie = ""
    nazwisko = ""
    wiek = 0
    
    def zmien_wiek(self, nowyWiek:int):
        setWiek = self.wiek = nowyWiek
        print(f"Nowy wiek: {setWiek}, użytkownika: {self.imie} {self.nazwisko}")
    
    def wyswietl(self):
        print(self.imie, self.nazwisko)

        if self.wiek >= 18:
            print(f"{self.imie} jest pełnoletni, gdyż ma {self.wiek} lata")
        else:
            print(f"{self.imie} nie jest pełnoletni, gdyż ma {self.wiek} lata")
