"""
Napisz funkcję, która otrzymuje 3 parametry:
- proporcje_szerokosc
- proporcje_wysokosc
- piksele_szerokosc

Funkcja otrzymuje oczekiwane proporcje ekranu (np. 16:9, 4:3) oraz piksele_szerokosc.
Zadaniem funkcji jest obliczyć ile pikseli powinna mieć wysokość, aby proporcje ekranu były poprawne.
Zwracana liczba powinna być liczbą całkowitą.

Przykłady:
oblicz_wysokosc(16, 9, 1920) -> 16:9 -> 1920 x 1080
oblicz_wysokosc(16, 9, 1280) -> 16:9 -> 1280 x 720
oblicz_wysokosc(4, 3, 1920) -> 4:3 -> 1920 x 1440
"""

def oblicz_wysokosc(proporcje_szerokosc, proporcje_wysokosc, piksele_szerokosc):
    y = piksele_szerokosc * proporcje_wysokosc / proporcje_szerokosc
    return int(y)

print(oblicz_wysokosc(16, 9, 1920))
print(oblicz_wysokosc(16, 9, 1280))
print(oblicz_wysokosc(4, 3, 1920))
