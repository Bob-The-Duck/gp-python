"""
Przygotuj 3 listy, a następnie wyświetl się w konsoli, aby sprawdzić czy zostały poprawnie przygotowane.
- Listę 5 losowych liczb, które przyjdą Ci do głowy (również z ułamkami).
- Listę minimum 3 ulubionych gier / filmów / piosenek.
- Listę składającą się z 3 list, w których odpowiednio wpiszesz Imię, Nazwisko i Wiek trzech wymyślonych osób.
"""

lista1 = [1, 2222, 3.222222, 4, 6.777777]
print(lista1)

best = ['Anonymus Hacker Simulator', 'Elon Musk', 'Hobbit']
print(best)

dane = [["Stasiek", "Trocha", 13], ["Adam", "Nowak", 45], ["Bartłomiej", "Kręgielewski", 26]]
print(dane)

####################

import random
a = []
for i in range(5):
    a.append(random.randint(1,100))
print(a)