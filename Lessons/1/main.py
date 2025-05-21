# Hello World
print("Hello World")

# Nasz pierwszy interaktywny program

print("Hej, jestem Python!")
print("Jak masz na imię?")
imie = input()
print("Cześć", imie, "miło mi Cię poznać!")
print(f"Cześć {imie} miło mi Cię poznać!")

odp = input("Czy chcesz, żebym zrobił Ci quiz? ")

if odp == "Tak":
    print("Ile było wersji Pythona")
    odpNaPytanie1 = input()
    if odpNaPytanie1 == "3":
        print("Brawo! Dobra odpowiedź")
    else:
        print("Niestety nie")
else:
    print("Ok, to kończymy")
