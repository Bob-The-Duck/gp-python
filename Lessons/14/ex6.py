"""
Napisz program, który zapyta użytkownika o liczbę,
a następnie wypisze na ekranie tyle wyników z rzutu kością sześcienną.

Rzut kością sześcienną to wynik z losowania liczby od 1 do 6 (włącznie).
"""

import random

liczba = int(input("Podaj ile rzutów wykonać: "))

for _ in range(liczba):
    losowaLiczba = random.randint(1,6)
    print(f'Kości zostały rzucone: {losowaLiczba}')