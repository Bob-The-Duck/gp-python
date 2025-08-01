"""
Przygotuj funkcję, która jako argument otrzymuje string oraz listę stringów, a zwraca napis,
gdzie pomiędzy elementy z listy dokładana jest zawartość pierwszego argumentu.

Wskazówka: skorzystaj z metody `join`

Przykład:
foo("?", ["ala", "ma", "kota"]) -> "ala?ma?kota"
"""

def foo(separator, tablica_wyrazow):
    rezultat = ""
    for wyraz in tablica_wyrazow:
        if wyraz == tablica_wyrazow[-1]:
            rezultat += wyraz
        else:
            rezultat += wyraz + separator
    return rezultat

print(foo("?", ["ala", "ma", "kota"]))

def bar(separator, tablica_wyrazow):
    wynik = separator.join(tablica_wyrazow)
    return wynik

print(bar("?", ["ala", "ma", "kota"]))