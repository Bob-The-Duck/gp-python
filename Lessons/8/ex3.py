"""
Napisz program, który wypisze ile lat miałeś/aś w kolejnych latach kalendarzowych od Twojego roku urodzenia.
Program powinien wykorzystać zmienną wiek oraz pętle `for` z instrukcją `range`.
"""

wiek_rocznikowo = 26

for i in range(wiek_rocznikowo + 1):
    rok_kalendarzowy = 2025 - wiek_rocznikowo + i
    wiek_w_danym_roku = i
    print(f"W roku {rok_kalendarzowy} miałeś {wiek_w_danym_roku} lat")