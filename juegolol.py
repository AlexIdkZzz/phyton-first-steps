import random

ns = random.randint(1, 10)
jugador = 0
5
while jugador != ns:
    jugador = int(input("Escribe el posible numero: "))
    if jugador < ns:
        print("Tu numero es menor jaja")
    elif jugador > ns:
        print("Tu numero es mayor")
    else:
        print("Ganaste")