 ##  ##   ##  ##   #####     ####    ######   ######     ##     ##
 ## ##    ##  ##   ##  ##   ##  ##       ##     ##      ####    ##
 ####     ##  ##   ##  ##   ##          ##      ##     ##  ##   ##
 ###      ##  ##   #####     ####      ##       ##     ######   ##
 ####     ##  ##   ##           ##    ##        ##     ##  ##   ##
 ## ##    ##  ##   ##       ##  ##   ##         ##     ##  ##   ##
 ##  ##    ####    ##        ####    ######     ##     ##  ##   ######

# i = 0

# while i < 10:
#     print(i)
#     i+=1

# i = int(input("Podaj Liczbę: "))
# a = 0

# while a < i:
#     print(f''' 
#  ##  ##   ##  ##   #####     ####    ######   ######     ##     ##
#  ## ##    ##  ##   ##  ##   ##  ##       ##     ##      ####    ##
#  ####     ##  ##   ##  ##   ##          ##      ##     ##  ##   ##
#  ###      ##  ##   #####     ####      ##       ##     ######   ##
#  ####     ##  ##   ##           ##    ##        ##     ##  ##   ##
#  ## ##    ##  ##   ##       ##  ##   ##         ##     ##  ##   ##
#  ##  ##    ####    ##        ####    ######     ##     ##  ##   ######
          
# ''')
#     a += 1

# import time

# czas = int(input('Ile czasu do BOMBOCLAT: '))

# while czas >= 0:
#     if czas == 0:
#         print(f'''
#  ____   ___  __  __ ____   ___   ____ _        _  _____
# | __ ) / _ \|  \/  | __ ) / _ \ / ___| |      / \|_   _|
# |  _ \| | | | |\/| |  _ \| | | | |   | |     / _ \ | |
# | |_) | |_| | |  | | |_) | |_| | |___| |___ / ___ \| |
# |____/ \___/|_|  |_|____/ \___/ \____|_____/_/   \_\_|
# ''')
#         czas -= 1
#     else:
#         print(czas)
#         czas -= 1
#     time.sleep(1)

# import random

# minimum = 1
# maksimum = 10
# proby = 0
# wylosowana_liczba = random.randint(minimum,maksimum)
# strzelonaLiczba = 0
# while wylosowana_liczba != strzelonaLiczba:
#     strzelonaLiczba = int(input('Podaj Liczbę: '))
#     proby += 1
#     if strzelonaLiczba == wylosowana_liczba:
#         print("wygrałeś!")
#         print(f"próby: {proby}")
#         break
#     elif strzelonaLiczba < wylosowana_liczba:
#         print('za mała')
        
#     else:
#         print("za dużo")
    
Pin = "1234"
Data = "2013"
while True:
    input_pin = input("Pin")
    if input_pin != Pin:
        print("Odmowa dostępu!")
        continue
    input_Data = input("Data")
    if input_Data != Data:
        print("Odmowa dostępu!")
        continue
    else:
        print("Zalogowano!")
        break