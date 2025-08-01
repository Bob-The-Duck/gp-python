"""
Napisz funkcję, która jako argument otrzymuje listę elementów,
w której mogą występować powtórzenia, a zwraca listę unikalnych elementów.

Przykład:
Dla [1,2,3,3,3,3,4,5] oczekujemy [1, 2, 3, 4, 5].
"""

def filtruj(tab: list) -> list:
    wynik = []
    for element in tab:
        if element not in wynik:
            wynik.append(element)
    return wynik

print(filtruj([1,2,3,3,3,3,4,5] ))