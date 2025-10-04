from uzytkownik import uzytkownik
import math
# imie1 = "Jan"
# nazwisko1 = "Kowlalski"
# wiek1 = 18

# imie2 = "Adam"
# nazwisko2 = "Nowak"
# wiek2 = 16

# imie3 = "Michał"
# nazwisko3 = "Kowal"
# wiek3 = 99

# print(imie1, nazwisko1,wiek1)
# if wiek1 >= 18:
#     print("Osoba jest pełnoletnia!")
# else:
#     print("Osoba nie jest pełnoletnia!")

# print(imie2, nazwisko2,wiek2)
# if wiek2 >= 18:
#     print("Osoba jest pełnoletnia!")
# else:
#     print("Osoba nie jest pełnoletnia!")

# print(imie3, nazwisko3,wiek3)
# if wiek3 >= 18:
#     print("Osoba jest pełnoletnia!")
# else:
#     print("Osoba nie jest pełnoletnia!")

user1 = uzytkownik()
user2 = uzytkownik()
user3 = uzytkownik()
user4 = uzytkownik()

user1.imie = "Jan"
user1.nazwisko = "Kowalski"
user1.wiek = 32

user2.imie = "Adam"
user2.nazwisko = "Nowak"
user2.wiek = 18

user3.imie = "Jeremi"
user3.nazwisko = "Kulka"
user3.wiek = 2

user4.imie = "Albert"
user4.nazwisko = "Ajnsztajn"
user4.wiek = 1505050505050050000505050505050505005505050500505050505050505050505005050505050500000000000000000000050505050055005500555555555500000000

# print(user1.imie, user1.nazwisko, user1.wiek)
# print(user2.imie, user2.nazwisko, user2.wiek)
# print(user3.imie, user3.nazwisko, user3.wiek)

user1.wyswietl()
user2.wyswietl()
user3.wyswietl()
user4.wyswietl()

user1.zmien_wiek(1)
user2.zmien_wiek(34)
user3.zmien_wiek(11)
user4.zmien_wiek(33434334)

#zadanie domowe

# 1. Dodajmy do naszej klasy metodę zmien_wiek()
# Metoda powinna przyjmować w parametrze liczbę a następnie ustawiać wiek
# danego obiektu na przekazaną liczbę.
# 2. Napisz klasę Przedmiot, która będzie posiadać następujące zmienne:
# oceny - lista ocen (musimy stworzyć ją funkcją inaczej wszystkie obiekty będą
# korzystały z tej samej listy, rozwiązaniem jest konstruktor ale my jeszcze go nie
# znamy)
# srednia – średnia wszystkich ocen
# Oraz metody:
# stworz_liste()
# dodaj_ocene(ocena)
# wyswietl_oceny()
# wyswietl_srednia()
# Stwórz kilka obiektów klasy przedmiot np. matematyka, j_polski, historia i
# wywołaj ich metody: