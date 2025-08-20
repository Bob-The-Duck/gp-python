"""
Przygotuj funkcję, która otrzymuje jeden argument: `n` - liczbę elementów.
Funkcja ma zwrócić listę o długości `n` - losowych elementów od 0 do 100.
Wywołaj ją kilka razy, aby sprawdzić, czy za każdym razem zwraca różne wartości.
"""

import random

def losowa_lista(n: int):
    lista = []
    for i in range(n):
        randomowa_liczba = random.randint(0, 100)
        lista.append(randomowa_liczba)
    return lista

print(losowa_lista(5))
print(losowa_lista(5))
print(losowa_lista(5))