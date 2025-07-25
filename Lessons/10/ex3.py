"""
Napisz funkcję, który obliczy pole koła.
Skorzystaj w tym celu z modułu `math`, który zawiera stałą `pi`.
"""

import math

def pole_kola(r):
    pole = math.pi * r ** 2
    print(f"Pole koła o promieniu {r} wynosi {pole}")

pole_kola(6)
pole_kola(7)
pole_kola(10)
pole_kola(12)

# print(math.pi)