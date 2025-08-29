"""
Napisz funkcję, która przyjmuje 2 argumenty:
- `tekst`, typu `str`,
- `n`, typu `int`,
a zwraca nowy napis, który powstaje poprzez połączenie `tekst` `n` razy.

Szablon funckji

def laczenie_slow(???) -> ???:
    nowy_tekst = ""
    ???
    ???
    return ???

Zastąp wszystkie znaki zapytania "???" odpowiednimi wyrazami/instrukcjami/itd.
"""

def laczenie_slow(tekst: str, n: int) -> str:
    nowy_tekst = ""
    for i in range(n):
        nowy_tekst += tekst
    return nowy_tekst
    # return tekst * n

print(laczenie_slow("Leonard", 3))