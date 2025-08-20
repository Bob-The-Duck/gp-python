"""
Zapytaj użytkownika o jego wiek i na tej podstawie wyświetla w konsoli jeden z komunikatów:
- "Jesteś pełnoletni/a".
- "Nie jesteś jeszcze pełnoletni/a. Brakuje Ci XX lat do 18 roku życia".
Zamiast "XX" powinna pojawić się wartość liczbowa.
"""

wiek = int(input("Ile masz lat? "))

if wiek < 18:
    obliczenie = 18 - wiek
    print(f"Nie jesteś jeszcze pełnoletni/a. Brakuje Ci {obliczenie} lat do 18 roku życia")
else:
    obliczenie = wiek - 18
    print(f"Jesteś pełnoletni/a od {obliczenie} lat")