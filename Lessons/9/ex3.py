"""
Program zapyta o liczbę elementów, które ma przyjąć, a następnie odczyta od użytkownika tyle komunikatów.
Na koniec wyświetli je w tej samej kolejności.

Dodatkowo: Spróbuj wyświetlić komunikaty w odwrotnej kolejności.
"""

liczba_elementow = int(input("Podaj ilość komunikatów: "))

elementy = []

for i in range(liczba_elementow):
    komunikat = input(f"Podaj komunikat numer {i}: ")
    elementy.append(komunikat)

for index in range(len(elementy)):
    print(f"Komunikat o indexie {index}: {elementy[index]}")

# for element in elementy:
#     print(f"Komunikat: {element}")

# Część dodatkowa
print("Komunikaty w odwrotnej kolejności")
for index in range(len(elementy)-1, -1, -1):
    print(elementy[index])

