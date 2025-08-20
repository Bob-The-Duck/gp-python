"""
Cena atrakcji turystycznej zależy od miesiąca.
Napisz program, który zapyta użytkownika o liczbę biletów oraz miesiąc,
w którym chce odwiedzić park rozrywki i na tej podstawie obliczy koszt transakcji.

Koszt biletu w danym miesiącu (miesiąc jako numer -> koszt biletu):
- 1 -> 50 zł
- 2 -> 50 zł
- 3 -> 100 zł
- 4 -> 100 zł
- 5 -> 200 zł
- 6 -> 200 zł
- 7 -> 250 zł
- 8 -> 200 zł
- 9 -> 200 zł
- 10 -> 100 zł
- 11 -> 100 zł
- 12 -> 50 zł

Wyświetl komunikat:
"Cena biletów: XX zł"

"XX" to wartość liczbowa.

Jeśli wprowadzono niepoprawny numer miesiąca program powinien wyświetlić informację:
"Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie"
"""

try:
    ilosc = int(input("Podaj ilość biletów: "))
    miesiac = int(input("Podaj miesiąc: "))
    cena = 0
    match miesiac:
        case 1 | 2 | 12:
            cena = 50
        case 3 | 4 | 10 | 11:
            cena = 100
        case 5 | 6 | 8 | 9:
            cena = 200
        case 7:
            cena = 250
        case _:
            print("Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie")
            quit()
    
    print(f"Cena biletów: {cena * ilosc} zł")
except:
    print("Podaj wartość liczbową")