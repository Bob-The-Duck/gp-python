"""
Napisz program, który zapyta i pobierze od użytkownika dwie liczby, a następnie wypisze na konsoli wynik tego działania, podając całości i resztę z dzielenia.
Dla danych 48 i 10: "48 dzielone przez 10 jest równe 4 i 8 reszty."

Jakich operatorów będziesz potrzebować?
- //
- %
"""

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print(f"{a} dzielone przez {b} jest równe {a // b} i {a % b} reszty.")