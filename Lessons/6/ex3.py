"""
Stwórz program, który obsłuży proces dwuetapowego logowania.
Użytkownik zostanie poproszony o wprowadzenie czterocyfrowego PINu.
Jeśli poda błędny PIN, program wyświetli odpowiedni komunikat o błędzie.
W przypadku poprawnego PINu, użytkownik zostanie następnie poproszony o podanie hasła słownego.

PIN: „1234”
Hasło: „Masło”

Czy pin powinien być przechowywany jako tekst czy liczba?
"""

PIN = "1234"
HASLO = "Masło"

user_pin = input("PIN: ")

if PIN == user_pin:
    user_haslo = input("Podaj hasło: ")
    if HASLO == user_haslo:
        print("Zostałeś zalogowany!")
    else:
        print("Błędne hasło!")
else:
    print("Błędny PIN")