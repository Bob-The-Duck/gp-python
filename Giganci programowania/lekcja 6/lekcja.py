'''
Napisz program, który zapyta użytkownika o N ocen cząstkowych, a następnie wyliczy średnią z przedmiotu.

N - liczba ocen wprowadzona przez użytkownika na początku działania programu.

Dodatkowo: Zaokrąglij wynik do całości.
'''

# N = int(input("Ile masz ocen? "))
# suma = 0
# for i in  range(N ,0,-1):
    
#     suma += float(input("Podaj ocene: "))

# wynik = suma / N
# print(f'Średnia: {wynik}, w zaokragleniu: {round(wynik)}')


'''
Przygotuj 3 listy, a następnie wyświetl się w konsoli, aby sprawdzić czy zostały poprawnie przygotowane.
- Listę 5 losowych liczb, które przyjdą Ci do głowy (również z ułamkami).
- Listę minimum 3 ulubionych gier / filmów / piosenek.
- Listę składającą się z 3 list, w których odpowiednio wpiszesz Imię, Nazwisko i Wiek trzech wymyślonych osób.
'''

# lista1 = [1,2222,3.222222,4,6.777777]
# lista2 = ["Star wars - Parszywa Zgraja", "Zelda", "Star Wars - Asoka"]
# lista3 = [["Adam", "Nowak",12],["Jan", "Pawel",2],["Kapcerek", "Srak",6]]

# print(lista1)
# print(lista2)
# print(lista3)

# oceny = []

# while True:
#     odpowiedz = input("Podaj ocenę lub zakończ (q): ")
#     if odpowiedz == "q":
#         break
#     else:
#         ocena = float(odpowiedz)
#         oceny.append(ocena)
#         print(oceny) #testowe wypisywanie tablicy
# suma = sum(oceny)
# srednia = suma / len(oceny)
# print(f"Średnia: {srednia}")

komunikaty = []

pytanie = int(input("Ile?"))

for i in range(pytanie):
    komunikatPytanie = input(f"Komunikat nr {i}: ")
    komunikaty.append(komunikatPytanie)

for index in range(len(komunikaty)):
    print(f"komunikat o indexie {index}: {komunikaty[index]}")


# komunikaty.reverse()
# print(komunikaty)
print("Odwrotnie")
for index in range(len(komunikaty)-1, -1, -1):
    print(komunikaty[index])