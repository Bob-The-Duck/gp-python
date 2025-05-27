import random
from datetime import datetime

# Random

los = random.randint(1,100) # [1, 100]
los2 = random.randrange(1, 100) # [1, 100)
los3 = random.random() # [0, 1)

print("Los:", los)
print(f"Los2: {los2}")
print(f"Los3: {los3}")

# Datetime

dzis = datetime.today()
print(f"Dzisiejsza data: {dzis}")
print(f"Rok: {dzis.year}")
print(f"Miesiąc: {dzis.month}")
print(f"Dzień: {dzis.day}")

moje_urodziny = datetime(1999, 2, 5)
print(f"Moje urodziny: {moje_urodziny}")

ile_minelo = dzis - moje_urodziny
print(f"Od moich urodziny minęło {ile_minelo.days} dni")