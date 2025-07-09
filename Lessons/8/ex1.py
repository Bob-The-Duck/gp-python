"""
Napisz program, który będzie pytać użytkownika o liczby i zliczać ich sumę, aż do wprowadzenia przez użytkownika hasła “koniec”.
Po wpisaniu tego hasła program, powinien opuścić pętle while i wyświetlić sumę tych ocen.
"""

odp = input("Podaj liczbę lub hasło 'koniec': ")
suma = 0

while odp != 'koniec':
    liczba = int(odp)
    suma += liczba
    odp = input("Podaj liczbę lub hasło 'koniec': ")

print(f"Suma ocen: {suma}")
