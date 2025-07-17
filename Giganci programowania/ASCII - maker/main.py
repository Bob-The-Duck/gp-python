import pyfiglet
from rich.console import Console
from rich.text import Text
from pyfiglet import Figlet
import time

def main():
    f = Figlet(font="big")
    print(f.renderText("ASCII-GEN"))
    print() #odstep


    nazwa = input("Podaj nzawę: ")

    print(f'[✅] Ustawiono nzawę na: {nazwa}')

    rodzaj = input("[❓]Podaj rodzaj (napisz --list aby otzrymać pełną listę rodzajów): ")

    if rodzaj == '--list':

    # Czcionka Standard (domyślna, bardzo czytelna)
        print("--- Standard ---")
        standard_text = pyfiglet.figlet_format("Witaj Swiecie!")
        print(standard_text)

        # Czcionka Big (większa wersja Standard)
        print("--- Big ---")
        big_text = pyfiglet.figlet_format("Big Test", font="big")
        print(big_text)

        # Czcionka Slant (pochyły tekst)
        print("--- Slant ---")
        slant_text = pyfiglet.figlet_format("Python", font="slant")
        print(slant_text)

        # Czcionka Block (kanciasta i wyrazista)
        print("--- Block ---")
        block_text = pyfiglet.figlet_format("Klocki", font="block")
        print(block_text)

        # Czcionka Bubble (zabawne 'bańki')
        print("--- Bubble ---")
        bubble_text = pyfiglet.figlet_format("BAŃKI", font="bubble")
        print(bubble_text)

        # Czcionka Digital (przypomina wyświetlacz cyfrowy)
        print("--- Digital ---")
        digital_text = pyfiglet.figlet_format("CYFROWE", font="digital")
        print(digital_text)

        # Czcionka Banner (bardzo szeroka i efektowna)
        print("--- Banner ---")
        banner_text = pyfiglet.figlet_format("BANNER", font="banner")
        print(banner_text)

        # Czcionka Graffiti (swobodny, artystyczny styl)
        print("--- Graffiti ---")
        graffiti_text = pyfiglet.figlet_format("GRAFFITI", font="graffiti")
        print(graffiti_text)

        # Czcionka Fuzzy (trochę 'rozmyta' lub 'futrzana')
        print("--- Fuzzy ---")
        fuzzy_text = pyfiglet.figlet_format("Fuzzy", font="fuzzy")
        print(fuzzy_text)

        # Czcionka Rectangles (litery z prostokątów)
        print("--- Rectangles ---")
        rect_text = pyfiglet.figlet_format("Kwadraty", font="rectangles")
        print(rect_text)

        rodzaj = input("[❓] Podaj rodzaj: ")








    

    print(f'[✅] Ustawiono rodzaj na: {rodzaj}')


    print("[🔁] Generowanie...")
    time.sleep(3)

    try :


        kod = f''' 
        import pyfiglet
        from rich.console import Console
        from rich.text import Text
        from pyfiglet import Figlet


        f = Figlet(font=f"{rodzaj}")
        print(f.renderText(f"{nazwa}")) 
        print() #odstep
        '''

        print(kod)
        print("[✅] Kod wygenerowany!")

        print("[✅] Wygenerowany napis:")
        f = Figlet(font=f"{rodzaj}")
        print(f.renderText(f"{nazwa}")) 
        print() #odstep


        print("[🐞] Pamiętaj aby zainstalować pyfiglet! (pip install pyfiglet)")
    except:
        ValueError("[❌] Upss! Sprawdź czy podałeśpoprawne dane.")   

    
    main()
main()