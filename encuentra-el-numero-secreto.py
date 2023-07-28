import random

numero_secret = random.randint(1, 10)
jugador = 0
counter = 0
intentos = 1

print("\n**BIENVENIDO AL JUEGO .DESCUBRE EL NUMERO SECRETO.**")
print("\nLas reglas son sencillas: debes intentar adivinar el numero secreto entre 1 y 10 en un máximo de 3 intentos, si no lo logras perderás el juego, sencillo, no? ;)")
print("\nOk, empecemos...")

while jugador != numero_secret:
    while True:
        try:
            tryy = f"{counter}. Intento, prueba otra vez: "
            jugador = int(input(tryy))
            break
        except ValueError:
            print("\nNo es un numero, bruh.\n")
    
    counter = counter + 1
    
    if jugador == numero_secret:
        print("\nFelicidades, ganaste. :)\n")
        break
    if jugador != numero_secret and counter == 3: 
        print("\nChale, perdiste.\n")
        break
    if counter < 3:
        if jugador != numero_secret:
            intentos = intentos - counter
            chances = f"\nLamento decirte que te equivocaste, te dare un pista...\n"
            print(chances)
    if jugador != numero_secret:
        if jugador < numero_secret:
            print("El numero que ingresaste es menor.\n")
        else:
            print("El numero que ingresaste es mayor.\n")