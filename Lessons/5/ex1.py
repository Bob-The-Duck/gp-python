"""
Stwórzmy program, który obliczy wynik dzielenia. Pamiętaj, że dzielenie przez zero jest niedozwolone.
"""

dzielna = int(input("Wprowadź dzielną: "))
dzielnik = int(input("Wprowadź dzielnik: "))

# if dzielnik == 0:
#     print("Nie wolno dzielić przez zero!")

# if dzielnik != 0:
#     wynik = dzielna / dzielnik
#     print(f"Wynik: {wynik}")

if dzielnik == 0:
    print("Nie wolno dzielić przez zero!")
else:
    wynik = dzielna / dzielnik
    print(f"Wynik: {wynik}")