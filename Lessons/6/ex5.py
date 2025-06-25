"""
Napisz program, który wczyta od użytkownika oceny końcowe z pięciu przedmiotów:
- matematyka,
- polski,
- angielski,
- informatyka,
- wf.
Następnie wyliczy średnią ocen i wyświetli komunikat czy otrzymamy pasek na świadectwie.
Aby otrzymać czerwony pasek nasza średnia musi być większa lub równa 4.75.
"""

print("Podaj oceny końcowe z następujących przedmiotów:")
ocena_metematyka = int(input("Matematyka: "))
ocena_polski = int(input("Polski: "))
ocena_angielski = int(input("Angielski: "))
ocena_informatyka = int(input("Informatyka: "))
ocena_wf = int(input("WF: "))

suma_ocena = ocena_metematyka + ocena_polski + ocena_angielski + ocena_informatyka + ocena_wf
srednia_ocen = suma_ocena / 5

if srednia_ocen >= 4.75:
    print("Gratulacje, otrzymasz czerwony pasek na świadectwie!")
else:
    print("Niestety, nie otrzymasz czerwonego paska na świadectwie! :(")
    print("Powodzenia w przyszłym roku")

print(f"Twoja średnia ocen to: {srednia_ocen}")