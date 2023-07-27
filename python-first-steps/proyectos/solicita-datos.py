
print('\n**Realice una suma que de como resultado 5**\n')

while True:
    try:
        n1 = int(input("Dime el primer número: "))
        break
    except ValueError:
        print("El valor introducido no es un número. Intenta de nuevo")

while True:
    try:
        n2 = int(input("Dime el segundo número: "))
        break
    except ValueError:
        print("El valor introducido no es un número. Intenta de nuevo")
        
n3 = n1 + n2

n4 = f'\nEl resultado de la suma es {n3}\n'

print(n4)

if(n3 == 5):
    print('\nCorrecto.\n')
else:
    print('\nIncorrecto.\n')
