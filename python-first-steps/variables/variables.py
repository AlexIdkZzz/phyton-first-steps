# Literales de cadena formateados (f-strings para abreviar) 

# Definiendo variable con camelCase
# nombreCompleto = "Juan"

# Definiendo variable con snake_case
nombre_completo = "Juan"

#La variable puede contener lo que sea y el f-string lo convertirá a texto.

# Concatenar con f-string
bienvenida = f"\nHola {nombre_completo}, ¿Como estás?\n"
# La f se escribe antes del texto para que fucionen los corchetes.

# Concatenar con +
# bienvenida = "\nHola " + nombre_completo + "¿Como estás?\n"

del nombre_completo
# 'del' sirve para borrar un dato y limpiar la memoria.

print(bienvenida)

print("ola" in bienvenida) # True
# 'in' busca lo establecido en la variable propuesta.

print("ola" not in bienvenida) # False
# 'not in' busca lo no establecido en la variable propuesta.
# 'in' y 'not in' son operadores de pertenencia.