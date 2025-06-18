"""
Jaką liczbę wprowadził użytkownik? Napisz program, który sprawdzi, czy liczba jest dodatnia, ujemna czy równa zero.
"""

liczba = int(input("Podaj liczbę: "))

if liczba == 0:
    print("Twoja liczba to 0")
elif liczba > 0:
    print("Twoja liczba jest dodatnia")
else:
    print("Twoja liczba jest ujemna")