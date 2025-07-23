"""
Przygotuj funkcję obliczającą pole prostokąta.
Funkcja ma przyjmować długości boków, a następnie obliczać i wyświetlać pole figury.

Dodatkowo: Funckję obliczająco pole trójkąta prostokątnego.
"""

def pole_prostokata(bok1, bok2):
    pole = bok1 * bok2
    print(f"Pole prostokąta {bok1} x {bok2} wynosi {pole}")

a = int(input("Podaj długość pierwszego boku: "))
b = int(input("Podaj długość drugiego boku: "))

pole_prostokata(a, b)