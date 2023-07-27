lista = ["Yael:)", "Alex:)", True, 1.85] # Lista se puede modificar
# tupla = ("Yael:)", "Alex:)", True, 1.85) # Tupla no se puede modificar

#Esto si es Válido
lista[0] = "Hola buenas"

# Esto no es válido
#tupla[0] = "Hola buenas"

# Creando un conjunto set

conjunto = {"Yael:)" ,"Alex:)" ,True, 1.85} # NO almacena datos duplicados, NO hay índice.

#print(conjunto[3]) -> no puede acceder al elemento.

# Creadno un diccionario (dict) (la estructura es key : value).
diccionario = {
    'nombre' : "Yael",
    'apodo' : "Alex",
    'le_gusta_programar' : True,
    'Altura' : 1.85,
    'dato_duplicado' : "Yael"
}

print(diccionario)
print(lista)