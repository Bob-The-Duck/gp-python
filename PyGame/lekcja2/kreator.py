#dodanie modułu pygame
import pygame
import element
#Utworzenie stałych
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600
#wczytanie obrazów do zmiennych
obraz_tla = pygame.image.load('images/background.png')
obraz_bazy_postaci = pygame.image.load('images/base.png') #nowe

pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

gra_dziala = True

nakrycie_glowy = element.NakrycieGlowy()
ubranie_element = element.Ubranie()
oczy_element = element.Oczy()
bron_element = element.Bron()


while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False
    
    ekran.blit(obraz_tla,(0,0))
    ekran.blit(obraz_bazy_postaci,(270,130)) #nowe
    ekran.blit(ubranie_element.wybranyObraz(),(270,130)) #nowe
    ekran.blit(oczy_element.wybranyObraz(),(270,130)) #nowe
    ekran.blit(bron_element.wybranyObraz(),(270,130)) #nowe
    ekran.blit(nakrycie_glowy.wybranyObraz(),(270,130)) #nowe
    pygame.display.flip()

    zegar.tick(30)

pygame.quit()