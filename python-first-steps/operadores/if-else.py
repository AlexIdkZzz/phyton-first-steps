edad = 56

if edad >= 18:
    print("Pasale. ;)")
else:
    print("No puedes pasar.")
    
del edad

while True:
    try:
        edad0 = int(input("Ingresa tu edad: "))
        break
    except ValueError:
        print("El valor introducido no es un número. Intenta de nuevo")

if edad0 >= 18:
    print("Pasale. ;)")
else:
    print("No puedes pasar.")
if edad0 >=100:
    print("Que haces acá vejestorio.")