"""
Napisz program, który zapyta użytkownika o N ocen cząstkowych, a następnie wyliczy średnią z przedmiotu.

N - liczba ocen wprowadzona przez użytkownika na początku działania programu.

Dodatkowo: Zaokrąglij wynik do całości.
"""

N = int(input("Podaj ilość ocen [int]: "))

suma = 0

for i in range(N):
    suma += float(input("Podaj ocenę cząstkową: "))

wynik = suma / N

print(f"Twoja średnia to {wynik}, a w zaokrągleniu to {round(wynik)}")