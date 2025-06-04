"""
Pobierz od użytkownika imię, nazwisko, rok urodzenia i wypisz na konsolę informację (dla danych Jan Kowalski, 1996): „Jan Kowalski ma rocznikowo 29 lat.”
Pamiętaj, aby skorzystać z f-stringów i odpowiednio obliczyć wiek na podstawie aktualnego roku.
"""

imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
rok_urodzenia = input("Podaj rok urodzenia: ")
rok_urodzenia = int(rok_urodzenia)

wiek = 2025 - rok_urodzenia
print(f"{imie} {nazwisko} ma rocznikowo {wiek} lat.")