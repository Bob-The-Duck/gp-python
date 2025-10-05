from pliki_gierki import *
import time
import os
clear = lambda: os.system('cls')


gracz = Gracz("Gracz")
przeciwnik = Przeciwnik()
gra = True

while gra:
    akcja = input("Wybierz akcje (zwiedzaj, odpocznij)")
    match (akcja):
        case "zwiedzaj":
            if randint(0,1) == 0:
                print(f"{gracz.nazwa} znalazł jaskinię")
            else:
                print(f"{gracz.nazwa} natrafił na {przeciwnik.nazwa}")
                gra = gracz.walka(przeciwnik)
        case "odpocznij":
            gracz.odpocznij()
        case _:
            print("Ej ty tam ja nie panimajesz co ty napisoł!")
                    
            