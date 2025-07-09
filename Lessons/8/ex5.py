"""
Napisz program, który zapyta użytkownika o wysokość (liczbę linijek), a następnie wyświetli choinkę / piramidę o podanej wysokości.
Choinka ma składać się z gwiazdek "*" oraz spacji jako znaków białych.
"""

ilosc_linijek = int(input("Podaj wysokość choinki: "))

for i in range(ilosc_linijek):
    gwiazdki = "* " * (i + 1)
    spacje = " " * (ilosc_linijek - i - 1)
    print(spacje + gwiazdki)