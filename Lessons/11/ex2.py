"""
Napisz funkcję, która otrzyma dwa argumenty pierwszym będzie liczba,
którą chcemy podzielić bez reszty a drugim argumentem będzie dzielnik.
Należy sprawdzić czy można dokonać dzielenia, a jeśli tak zwrócić informację czy liczba jest podzielna bez reszty czy nie.
"""

def czy_mozna_podzielic_calkowicie(liczba, dzielnik):
    if dzielnik == 0:
        return "Nie można dzielić przez 0"
    
    if liczba % dzielnik == 0:
        return True
    else:
        return False
    
print(czy_mozna_podzielic_calkowicie(5,0))
print(czy_mozna_podzielic_calkowicie(675,5))