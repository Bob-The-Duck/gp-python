"""
Napisz program, który sprawdzi, czy w podanym przez użytkownika wyrazie znajduje się jedna z następujących liter lub ciągów znaków:
- litera „a”
- litera „d”
- ciąg znaków „as”
- ciąg znaków „zzz”

Jeśli znajdzie choć jedno z nich, program powinien wyświetlić komunikat, że wyraz zawiera poszukiwany fragment.
"""

wyraz = input("Podaj jakiś wyraz: ")

if "a" in wyraz or "d" in wyraz or "as" in wyraz or "zzz" in wyraz:
    print(f"{wyraz} zawira przynajmniej jedno z wyszukiwanych haseł")
else:
    print(f"{wyraz} nie zawiera ŻADNEGO z wyszukiwanych haseł")