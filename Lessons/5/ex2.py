"""
Spróbuj zaimplementować program, który ułatwi podejmowanie decyzji operatorom rollercoaster'ów wykorzystując instrukcję warunkową if-else:

Napisz program, który powie Ci czy dany uczestnik może skorzystać z nowej atrakcji. Ograniczenia:
- minimalny akceptowalny wiek to 12 lat,
- minimalny akceptowalny wzrost to 130 cm,
- maksymalny akceptowalny wzrost to 195 cm.

Program zapyta użytkownika o jego wiek i wzrost, a następnie wyświetli komunikat, czy wolno mu skorzystać z atrakcji.
"""

wiek = int(input("Podaj wiek: "))
wzrost = int(input("Podaj wzrost [cm]: "))

# if wiek >= 12 and wzrost >= 130 and wzrost <= 195:
if wiek >= 12 and 130 <= wzrost <= 195:
    print("Możesz skorzystać z rollercoaster'a")
else:
    print("Nie możesz skorzystać z rollercoaster'a")