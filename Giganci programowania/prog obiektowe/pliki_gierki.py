from random import *
import time
import os
clear = lambda: os.system('cls')

nazwy = ["Gerald", "Kvpsztalek", "Zombie","Brajanusz", "Bobik"]
class Postac:
    def __init__(self):
        self.nazwa = ""
        self.zycie = 1
        self.max_zycie = 1
        
    def atakuj(self,przeciwnik):
        atak = randint(0,3)
        if atak == 0:
            print(f"{przeciwnik.nazwa} Unika ataku {self.nazwa} (,ponieważ wypił duzo trunku)")
        else:
            print(f"Weszło jak w masło {przeciwnik.nazwa} (-{atak}) oberwał od {self.nazwa}")
            przeciwnik.nazwa =- atak
class Gracz(Postac):
    def __init__(self,gracz):
        super().__init__()
        self.nazwa = input("Podaj swoją nazwę: ") #choice("Saaszka", "Bożydarek", "Oki Młody Jeżyk", "Ten jeden kolega z klasy", "ur mom destroyer", "kasztanka") #ur mom destroyer fajny kill w wot 2024
        self.zycie = 10
        self.max_zycie = 10
        
        
    def odpoczynek(self):
        while self.zycie >= (self.max_zycie - randint(1,self.max_zycie)) :
            print(f"Regeneruje... {self.zycie}/{self.max_zycie}")
            self.zycie += 1
            time.sleep(0.6)
            clear()
        print("Zregenerowano!")
    def walka(self,przeciwnik):
        walka = True
        while walka:
            print(f"życie: {self.zycie}/{self.max_zycie}")
            print(f"Życie przeciwnikak: {przeciwnik.nazwa}: {przeciwnik.zycie}")
            akcja_walki = input("Atak/Uciekaj/Negocjuj")
            match (akcja_walki):
                case "Atak":
                    self.atakuj(przeciwnik)
                    if przeciwnik.zycie <= 0:
                        print(f"{self.nazwa} zabija {przeciwnik.nazwa}")
                        return True
                    break
                case "atak":
                    self.atakuj(przeciwnik)
                    if przeciwnik.zycie <= 0:
                        print(f"{self.nazwa} zabija {przeciwnik.nazwa}")
                        return True
                    break
                case "Uciekaj":
                    print(f"{self.nazwa} jest cieniasem i ucieka")
                    przeciwnik.atakuj(self)
                    walka = False
                case _:
                    print("Ej ty tam ja nie panimajesz co ty napisoł!")
                
            if self.zycie <= 0:
                print(f"{self.nazwa} jest bambikiem i wywalił sie za zero")
                return False
        return True
                                
            
class Przeciwnik(Postac):
    def __init__(self):
        super().__init__()
        self.nazwa = nazwy[randint(0,len(nazwy))]
        self.zycie = randint(5,15)   
