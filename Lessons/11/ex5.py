"""
Napisz funkcję, która otrzymuje liczbę całkowitą a zwraca sumę jej cyfr.

Przykład:
Dla liczby 249 otrzymujemy 2+4+9, czyli 15".
"""

def suma_cyfr_mat(liczba: int) -> int:
    liczba = abs(liczba)
    dzielnik = 1
    wynik = 0
    while (dzielnik <= liczba):
        a = liczba // dzielnik
        dzielnik *= 10
        b = liczba // dzielnik * 10
        c = a - b
        wynik += c
    return wynik

print(suma_cyfr_mat(123))

def suma_cyfr_text(liczba: int):
    liczba_str = str(abs(liczba))
    wynik = 0
    for cyfra in liczba_str:
        wynik += int(cyfra)
    return wynik

print(suma_cyfr_text(123))