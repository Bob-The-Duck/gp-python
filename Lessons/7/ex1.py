"""
Napisz program, który wczyta od użytkownika liczbę całkowitą i wyświetli na ekranie dokładnie tyle komunikatów “Giganci Programowania”.
"""

liczba = int(input("Podaj liczbę całkowitą: "))

# Metoda z licznikiem

print("\nMetoda z licznikiem\n")
licznik = 0

while licznik < liczba:
    print("Giganci Programowania")
    licznik += 1

# Metoda z odejmowaniem

print("\nMetoda z odejmowaniem\n")

while liczba > 0:
    print("Giganci Programowania")
    liczba -= 1