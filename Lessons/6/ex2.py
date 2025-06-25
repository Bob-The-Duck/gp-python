"""
Napisz program, który będzie działał jak podstawowy system logowania.

Wykonaj poniższe kroki:
1. Zapisz dane do logowania w zmiennych:
  - LOGIN = "gigant@trener.pl"
  - HASLO = "qwerty"
2. Poproś użytkownika o podanie loginu (za pomocą input()).
3. Poproś użytkownika o podanie hasła.
4. Sprawdź, czy wprowadzone dane są zgodne z zapisanymi loginem i hasłem:
  - jeśli tak: wyświetl komunikat: "Poprawnie zalogowano"
  - jeśli nie: wyświetl komunikat: "Niepoprawny login lub hasło"
"""

import getpass

LOGIN = "gigant@trener.pl"
HASLO = "qwerty"

login = input("Podaj login: ")
hasło = getpass.getpass("Podaj hasło: ")

if login == LOGIN and hasło == HASLO:
    print("Zalogowałeś się na swoję konto")
else:
    print("Nie udało ci się zalogować")
