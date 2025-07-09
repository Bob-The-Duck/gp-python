"""
Napisz program, który wypisze w konsoli tabliczkę mnożenia.
Wykorzystaj funkcję `str(liczba).center(liczba_znaków)` do wyrównania tekstu.
"""

for wiersz in range(1, 11):
    linijka = ""
    for kolumna in range(1, 11):
        linijka += str(wiersz * kolumna).center(4) + "|"
    print(linijka)