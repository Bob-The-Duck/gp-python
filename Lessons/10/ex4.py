"""
Napisz funkcję, która przyjmuje dwa argumenty: `n` - liczba powtórzeń, `a` - liczba startowa.
Funkcja ma generować kolejne kwadraty liczb, zaczynając od `a` i ma wyświetlić `n` kolejnych liczb.
"""

def kwadraty_liczb(n, a):
    for i in range(a, a + n):
        kwadrat = i ** 2
        print(f"Kwadrat liczby {i} wynosi {kwadrat}")

kwadraty_liczb(5, 10)