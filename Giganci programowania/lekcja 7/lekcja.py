# import random

# liczba = int(input("Ile liczb wygenerować? "))
# liczby = []

# for i in range(liczba):
#     nowaLiczba = random.randint(1,1000000000000000)
#     liczby.append(nowaLiczba)
# print(liczby)

# def powitanie(wiad, ile):
#     for i in range(ile):
#         print(f"Nowa wiadomość: {wiad}")


# imie = "gRaŻyNkA"
# ile_razy = 10
# powitanie(imie,ile_razy)

# def pole(a,b):
#     pole_p = a*b
#     print(f"Pole prostokąta to {pole_p}, a pole trójkątu prostokątnego to: {pole_p / 2}")

# pole(4,6)

# import time

# def pasek_ladowania(gotowe, wszystko=100):
#     wykonane = round(10 * gotowe / wszystko)
#     niewykonane = 10-wykonane

#     tekst_wykonane = "#" * wykonane
#     tekst_niewykonane = "-" * niewykonane
#     print(f"\r [{tekst_wykonane}{tekst_niewykonane}]",end=' ')


# for i in range(100):
#     pasek_ladowania(wszystko = 100, gotowe = i)
#     time.sleep(0.1)

# from math import sqrt

# def pole_szesciokata_foremnego(a):
#     pole = 3*sqrt(3)*a**2/2

#     return pole


# poleFigury = pole_szesciokata_foremnego(5)
# print(f"Pole jakiegoś tam trójkąta o boku 5 wynosi: {poleFigury}")

'''
Napisz funkcję obliczającą objętość graniastosłupa prawidłowego, który w podstawie
ma sześciokąt (foremny, wiemy to dzięki słowu "prawidłowy").
'''
from math import sqrt
def pole_czegos_tam(a):
    pole = (3 * sqrt(3)/2) * a ** 2
    return pole
print(pole_czegos_tam(5))