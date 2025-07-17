# kom. jedno linjikowy

'''
===============================================================
                            to kom.
                            to też
                            i to 
                            xD
===============================================================
'''
# n = 11

# print(type(n))

# m = 'hejo!'

# print(type(m))

# o = True

# print(type(o))

# p = 6.56

# print(type(p))

# b = 3.2
# a = int(b)

# print(a)

# c = 3

# d = float(c)

# #e = float('10.5')

# print(d)

# f = int(False)
# print(f)

# g = int(True)
# print(g)



'''
toJestNazwaZmiennej - CamelCase > podonie jak PascalCase
ToJsetNazwaZmiennej - PascalCase > klasy i obiekty
to_jest_nazwa_zmiennej - SnakeCase > zmienne i funkcje
TO_JEST_NAZWA_ZMIENNEJ - UpperCase > > używamy do stałych
'''


# wiek = input("Ile masz lat? ")
# print(wiek)
# print(type(wiek))

# wzrost = input("Wzrost w metrach: ")
# print(wzrost)
# print(type(wzrost))

# Zapytanie = input("Czy jesteś pełnoletni (T/N) ")


# if Zapytanie == 'T':
#     Zapytanie = True
#     print(Zapytanie)
#     print(type(Zapytanie))
# else:
#     Zapytanie = False
#     print(Zapytanie)
#     print(type(Zapytanie))    

# imie = "wojtek"
# print(imie)
# print(type(imie))

# x = input("Podaj liczbę: ")
# try: 
#     x = int(x)
#     print(f"✅ Udało się! Wynik {x}")
# except:
#     print("🤡 Czego próbujesz pajacu ?!")

# import math

# a = 10
# b = 7
# print(+a)
# print(a+b)
# print(-a)
# print(a - b)
# print(a * b)
# print(a /b)
# print(10 / 1)
# print(a % b) # operator modulo > zwraca wynik dizelenia jednej liczby przez drugą
# print(a // b) #operator dzielenia całkowitego, zwraca dzielenia pierwszej liczby przez drugą, zaokrąglonego do dołu do liczby całkowitej
# print(3 ** 2)

# print(math.sqrt(255)) # pierwiastkowanie wymaga biblioteki math

# x = a * b
# x = x + 1 #pierwszy sposob dodawania
# x += 1
# x = x -1
# x -= 1
# x = x * a
# x *= a

# imie = input("imie: ")
# print(imie)
# print(type(imie))

# lata = input("lata: ")
# print(lata)
# print(type(lata))

# wiekk = input("Czy jesteś 18+? (True/False): ")
# print(wiekk)
# print(type(wiekk))



# print(True + True) # Dane logicne zamieniane: True >> 1 , a False >> 0

# #Dodawanie stringów:

# print('WItaj' + 'Gigancie')
# print(3* 'cos') # cos cos cos

# tekst = 'tekst'
# nowy_tekst = 'nowy'
# nowy_tekst += tekst
# print(nowy_tekst) #łączumy stringi

# n=10
# m=25

# print('Wynik mnożenia ',n, 'przez',m, 'to:',n * m)
# print(f'Wynik mnożenia {n} przez {m} to: {n * m} ')#lepszy sposób

# print(abs(-10))#wartość bezwzgledna
# print(max(1,2,3,4,5,6,7,8,9,-9))#najwieksza liczba
# print(min(1,2,3,4,5,6,7,8,9,-9))#najmniejsza liczba
# print(round(4.00876453))#zaokraglenie
# print(len('Kiełbasa'))#ILOŚĆ ELEMENTÓW W ZBIORZE


# liczba1 = int(input("Liczba 1: "))
# liczba2 = int(input("Liczba 2: "))

# print(f"Wynik: {liczba1 / liczba2}, Reszta: {liczba1 % liczba2}")


# liczba1 = int(input("Liczba1: "))
# procent = int(input("Procent z Liczby: "))

# print(procent/100 * liczba1)



# krawedz = int(input("podaj krawędź: "))

# print(f"Odjętość: {krawedz ** 3} cm3")
# print(f"Pole powierzchni: {6 * krawedz ** 2} cm3")

# czas = int(input("Podaj Czas Przebytej Trasy: "))
# dlugosc = int(input("Podaj długość Trasy: "))


# print(f"Średnia prędkość: {dlugosc / czas}")

# ilosc_osob = int(input("Osoby: "))
# ilosc_komp = int(input("Komputery: "))

# print(ilosc_komp / ilosc_osob)


# import math

# promien = int(input("Podaj promien: "))

# print(f"Pole koła: {math.pi * promien ** 2} ,a obwód koła: {2 * math.pi * 5}")


# import pyfiglet
# from rich.console import Console
# from rich.text import Text
# from pyfiglet import Figlet


# def menu():



#     f = Figlet(font=f"Graffiti")
#     print(f.renderText(f"RollerCoster"))
#     print() #odstep

#     print("Wybierz kolejkę:")
#     print("1. Kolejka junior")
#     print("2. Kolejka senior")
#     print("3. Kolejka max")




# menu()
# kolejka = int(input())
# if kolejka == 1:
#         wymaganyWzrost = 110
    
# elif kolejka == 2:
#         wymaganyWzrost = 150

# elif kolejka == 3: 
#     wymaganyWzrost = 180
# else:
#      print("[-] Upss! Nie znaleziono kolejki:(")
    
# wzrost = int(input("Podaj swój wzrost: "))

# try:
#     if wzrost >= wymaganyWzrost:
#         print("[+] Jeeeeeej! Możesz jechać :)")


#     else:
#         print("[-] Ups! Masz za mały wzrost :(")

# except:
#     print("🤡 Coś zepsułeś pajacu!!!")



print("Wybierz kolejkę:")
print("1. Kolejka junior")
print("2. Kolejka senior")
print("3. Kolejka max")

wybranaKolejka = int(input("[?] Wybierz kolejkę:"))
wzrost = int(input("[?] Podaj wzrost:"))
wiek = int(input("[?] Podaj wiek:"))

# if wybranaKolejka == 1:
#     if(wzrost >= 110):
#         if(wiek >= 6):
#             print("[+] Jeeeeeej! Możesz jechać :)")
        
#         else:
#             print("[-] Ups! Jesteś za młody:(")

#     else:
#         print("[-] Ups! Masz za mały wzrost :(")

# elif wybranaKolejka == 2:
#     if(wzrost >= 150):
#         if(wiek >= 10):
#             print("[+] Jeeeeeej! Możesz jechać :)")
        
#         else:
#             print("[-] Ups! Jesteś za młody:(")

#     else:
#         print("[-] Ups! Masz za mały wzrost :(")


# elif wybranaKolejka == 3:
#     if(wzrost >= 180):
#         if(wiek >= 14):
#             print("[+] Jeeeeeej! Możesz jechać :)")
        
#         else:
#                 print("[-] Ups! Jesteś za młody:(")

#     else:
#         print("[-] Ups! Masz za mały wzrost :(")


# niżej jest wersja gdzie warunki sa połączone niestety kosztem że nie możemy wyświetlić który warunek jest nie spaełniany

if wybranaKolejka == 1:
    if(wzrost >= 110 and wiek >= 6):
        print("[+] Jeeeeeej! Możesz jechać :)")
    else:
        print("[-] Ups! Nie spełnaisz wymagań!")

elif wybranaKolejka == 2:
    if(wzrost >= 150 and wiek >= 12):
        print("[+] Jeeeeeej! Możesz jechać :)")
    else:
        print("[-] Ups! Nie spełnaisz wymagań!")

elif wybranaKolejka == 3:
    if(wzrost >= 180 and wiek >= 14):
        print("[+] Jeeeeeej! Możesz jechać :)")
    else:
        print("[-] Ups! Nie spełnaisz wymagań!")


# AND -  warunek I warunek, cos i cos
# OR - warunek lub warunek, cos lub cos
# NOT - zaprzeczenie warunku

print(True, 25 < 140 and 10 == 10)
print(True, 100 >= 1 or 2 > 10)
print(False, 25 >= 14 and 10 != 10)
print(False, -1 < 3 and 2 < 9 and 10 == 15)
print(True, 20.05 < 21 < 10 or -10 < 20 < 150 <= 150)
print(False, 1 < 10 and 2 < 15 and -50 == 42)
print(True, not 2 == 10)
