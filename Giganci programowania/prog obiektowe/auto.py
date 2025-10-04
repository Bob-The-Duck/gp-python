class samochod():
    licznik1 = 0
    def __init__(self, marka,model,typ_silnika,data_produkcji):
        print("Siema masz nowy obiekt!")
        samochod.licznik1 += 1
        self.marka = marka
        self.model = model
        self.typSilnika = typ_silnika
        self.dataProdukcji = data_produkcji

    def wyswietl(self):
        print(self.marka)
        print(self.model)
        print(self.typSilnika)
        print(self.dataProdukcji)

print(samochod.licznik1)
auto1 = samochod("Fiat","Multipla","kosiarka",2010)
print(samochod.licznik1)
auto2 = samochod("Ford","Mustang","benxyna",2024)
print(samochod.licznik1)

auto1.wyswietl()
auto2.wyswietl()
