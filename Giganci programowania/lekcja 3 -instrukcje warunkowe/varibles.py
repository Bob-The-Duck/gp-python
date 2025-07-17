# x = int(input("Podaj dzielną: "))
# y = int(input("Podaj dzielnik: "))



# if (y == 0):
#     print("Upss! Wracaj do 3 klasy bo przez 0 nie dzielimy :(")

# else:
#     print(x / y)

# wiek = int(input("podaj wiek"))
# wzrost = int(input("podaj wzrost"))

# if (wiek >= 12 and wzrost >= 130 and wzrost <= 195):
#     print("możesz jechać")

# else:
#     print("nie możesz jechać")

# liczba = int(input("Liczba: "))

# if (liczba > 0):
#     print("Liczba jest większa niż 0")
# elif (liczba < 0):
#     print("Liczba jest mniejsza niż 0")
# else:
#     print("Liczba jest równa 0")

# miesiac = int(input("Podaj numer miesiąca: "))

# if(miesiac == 1 or miesiac == 2 ):
#     print("cena to 150$")
# elif (miesiac == 3 or  miesiac == 4):
#     print("cena to 199$")
# elif (miesiac == 5 or miesiac == 6):
#     print("cena to 249$")
# elif (miesiac == 7 or miesiac == 8 or miesiac == 9):
#     print("cena to 299$")
# elif (miesiac == 10):
#     print("cena to 249$")
# elif (miesiac == 11 or miesiac == 12):
#     print("cena to 199$")
# else:
#     print("niepoprawny nr. miesiąca")


# liczbaJeden = int(input("Podaj liczbę:"))

# print("Wybierz operację")
# print(f''' 
# + → dodawanie
# - → odejmowanie
# * → mnożenie
# / → dzielenie
# ''')

# operacja = input()

# liczbaDruga = int(input("Podaj drugą liczbę: "))

# match operacja:
#     case '+':
#         print(liczbaJeden + liczbaDruga)
#     case '-':
#         print(liczbaJeden - liczbaDruga)
#     case '*':
#         print(liczbaJeden * liczbaDruga)
#     case '/':
#         print(liczbaJeden / liczbaDruga)
#     case _:
#         print("Niepoprawna operacja")

# wyraz = input("Podaj testowany wyraz:")

# if ('a' in wyraz or 'd' in wyraz or 'as' in wyraz or 'zzz' in wyraz):
#     print("wyraz posiada jedno z wyszukiwanych haseł.")
# else:
#         print("wyraz nie posiada ani jedno z wyszukiwanych haseł.")
# import getpass

# login = "trener@giganci.pl"
# haslo = "qwerty"
# twostepverfy = "twojamama1234"

# podanyLogin = input("Podaj login ")
# podaneHaslo = getpass.getpass("Podaj hasło ")

# if (podanyLogin == login and podaneHaslo == haslo):
#     print("podaj kod weryfikacji dwuetapowej: ")
#     userpin = input()
#     if (userpin == twostepverfy):
#         print("Zalogowano!")
#     else:
#         print("kod niepoprawny")
# else:
#     print("Niepoprawne dane!")

"""

Napisz program, który wczyta od użytkownika oceny końcowe z pięciu
przedmiotów: matematyka, polski, angielski, informatyka, wf. Następnie wyliczy
średnią ocen i wyświetli komunikat czy otrzymamy pasek na świadectwie
(aby otrzymać czerwony pasek nasza średnia musi być większa lub równa 4.75).

"""
# mat = int(input("Podaj średnią z matmy: "))
# pol = int(input("Podaj średnią z polskiego: "))
# ang = int(input("Podaj średnią z angielskiego: "))
# inf = int(input("Podaj średnią z informatyki: "))
# wf = int(input("Podaj średnią z wf: "))

# srednia = (mat+pol+ang+inf+wf)/5

# print(f"średnia: {srednia}")


# if (srednia >= 4.75):
#     print("Masz czerwony pasek")
# else:
#     print("Nie masz czerwonego paska")






"""
Napisz program, który wczyta od użytkownika długości trzech boków trójkąta, a

następnie:
1. Sprawdzi, czy taki trójkąt może istnieć:
○ Każdy bok musi być większy od zera.
○ Suma długości dwóch krótszych boków musi być większa niż długość
najdłuższego.
○ Jeśli te warunki nie są spełnione – wyświetl odpowiedni komunikat i
zakończ program.

2. Wyświetli:
○ Najkrótszy i najdłuższy bok.
○ Rodzaj trójkąta ze względu na długości boków:
➤ równoboczny – wszystkie boki równe
➤ równoramienny – dwa boki równe
➤ różnoboczny – wszystkie boki różne
○ Obwód trójkąta.
○ Rodzaj trójkąta ze względu na kąty:
➤ prostokątny – spełnia twierdzenie Pitagorasa
➤ rozwartokątny – największy kąt > 90°
➤ ostrokątny – wszystkie kąty < 90°
"""

import math
a = int(input("Podaj bok 1 "))
b = int(input("Podaj bok 2 "))
c = int(input("Podaj bok 3 "))
najwieksza = 0
najmniejsza = 0
srednia = 0
if (a != 0 or b != 0 or c != 0):
    if(a > b and a>c):
        najwieksza = a
        najwiekszaLitera = 'a'
    elif (b>a and b>c):
        najwieksza= b
        najwiekszaLitera = 'b'
    else:
        najwieksza = c
        najwiekszaLitera = 'c'

    match najwiekszaLitera:
        case 'a':
            if (b > c):
                srednia = b
                najmniejsza = c
            else:
                srednia = c
                najmniejsza = b
            
        case 'b':
            if (a > c):
                srednia = a
                najmniejsza = c
            else:
                srednia = c
                najmniejsza = a
        case 'c':
            if (b > a):
                srednia = b
                najmniejsza = a
            else:
                srednia = a
                najmniejsza = b

    # print(najwieksza)
    # print(srednia)
    # print(najmniejsza)

    czyIstnieje = (srednia + najmniejsza) > najwieksza

    print(czyIstnieje)

    if (czyIstnieje == true):
        print("Ten trójkąt może istnieć!")
    else:
      print("Ten trójkąt nie może istnieć!")  
else:
    print("Podaj boki większe niż 0")

