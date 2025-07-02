"""
Przekształć poprzednie rozwiązanie tak aby po wpisaniu liczby przez użytkownika program wypisywał kolejne liczby, aż do zera. Po tym w konsoli powinien pojawić się napis "BOOM!".

Dla lepszego efektu można skorzystać z time.sleep(INT).

```
import time # importujemy bibliotekę time

time.sleep(1) # wstrzymujemy działanie programu na 1 sekundę
```

"""

import time

liczba = int(input("Nastaw bombę: "))

while liczba > 0:
    print(f"{liczba}")
    time.sleep(1)
    liczba -= 1
    
print("BOOM!")
