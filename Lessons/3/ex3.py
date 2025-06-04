"""
Procenty. Pobierz od użytkownika liczbę, a następnie wartość procentową. Program ma za zadanie wyświetlić ile to jest (% z liczby).
"""

liczba = float(input("Podaj liczbę: "))
procent = float(input("Podaj %: "))

wynik = liczba * procent / 100
print(f"{procent}% z liczby {liczba} wynosi {wynik}")