#dodanie modułu pygame
import pygame
import element
import time
#Utworzenie stałych
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600
#wczytanie obrazów do zmiennych
obraz_tla = pygame.image.load('images/background.png')
obraz_bazy_postaci = pygame.image.load('images/base.png') #nowe

pygame.init()
pygame.display.set_caption("Laggy Code Project >>> KREATOR POSTACI :)")
print('''
Dziękujemy za korzystanie z Laggy Code Project!
      KREATOR POSTACI :)

''')
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
pygame.font.init()
czcionka = pygame.font.SysFont('Comic Sans MS', 30)

gra_dziala = True

nakrycie_glowy = element.NakrycieGlowy()
ubranie_element = element.Ubranie()
oczy_element = element.Oczy()
bron_element = element.Bron()

zapisywanie = False

def wypisz_tekst(ekran,tekst,pozycja):
    napis = czcionka.render(tekst,False,(255,255,255))
    ekran.blit(napis,pozycja)

while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            if zdarzenie.key == pygame.K_1:
                nakrycie_glowy.wybierzNastepny()
            if zdarzenie.key == pygame.K_2:
                ubranie_element.wybierzNastepny()
            if zdarzenie.key == pygame.K_3:
                oczy_element.wybierzNastepny()
            if zdarzenie.key == pygame.K_4:
                bron_element.wybierzNastepny()
            if zdarzenie.key == pygame.K_s:
                zapisywanie = True
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False
    
    ekran.blit(obraz_tla,(0,0))
    ekran.blit(obraz_bazy_postaci,(270,130)) #nowe
    ekran.blit(ubranie_element.wybranyObraz(),(270,130)) #nowe
    ekran.blit(oczy_element.wybranyObraz(),(270,130)) #nowe
    ekran.blit(bron_element.wybranyObraz(),(270,130)) #nowe
    ekran.blit(nakrycie_glowy.wybranyObraz(),(270,130)) #nowe

    if zapisywanie == True:
        wypisz_tekst(ekran,f'Laggy Project > KREATOR POSTACI :)',(200,450))
        pygame.image.save(ekran, 'postac.png')
        zapisywanie = False
    wypisz_tekst(ekran,f'[1] Glowa: {nakrycie_glowy.wybrany}',(80,100))
    wypisz_tekst(ekran,f'[2] Ubranie: {ubranie_element.wybrany}',(80,140))
    wypisz_tekst(ekran,f'[3] Oczy: {oczy_element.wybrany}',(80,180))
    wypisz_tekst(ekran,f'[4] Broń: {bron_element.wybrany}',(80,220))

    wypisz_tekst(ekran,f'[S] Zapisz',(80,260))
    

    wypisz_tekst(ekran,f'Laggy Project > KREATOR POSTACI :)',(200,450))
    pygame.display.flip()

    zegar.tick(30)

pygame.quit()
