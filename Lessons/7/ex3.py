"""
Zgadywanie liczby wylosowanej przez komputer.
Program losuje liczbę, zadaniem użytkownika jest odgadnąć ją.
Komputer odpowiada “za mało”, “za dużo” lub w przypadku trafienia wyświetla informację o wygranej i liczbie tur potrzebnych do wygranej.

Do wylosowania liczby skorzystaj z modułu random i random.randint(MINIMUM, MAXIMUM).
"""

import random

wylosowna_liczba = random.randint(0, 1000)

liczba_podana = -1
liczba_tur = 0

# TESTY
print(wylosowna_liczba)

while liczba_podana != wylosowna_liczba:
    liczba_podana = int(input("Podaj liczbę: "))
    liczba_tur += 1
    if liczba_podana > wylosowna_liczba:
        print("Za dużo")
    elif liczba_podana < wylosowna_liczba:
        print("Za mało")

print(f"Brawo, zgadłeś moją liczbę: {wylosowna_liczba}")
print(f"Zajęło Ci to {liczba_tur} tury")