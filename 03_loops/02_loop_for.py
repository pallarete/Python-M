# 01 - Bucles (For)
# Permiten ejecutar un bloque de codigo 
# repetidamente mientras itera un iterable o una lista
import os
os.system('cls')

print('\nBucle for:')

#Iterar una lista
frutas = ['manzana','pera','mandarina']
for fruta in frutas:
  print(fruta)

# Iterar sobre cualquier cosa que sea iterable
cadena = 'alexdev'
for caracter in cadena:
  print(caracter)

# Enumerate()
frutas = ['manzana','pera','mandarina']
for index, value in enumerate( frutas):
  print(f'El indice es {index} y la fruta es {value}')

# Bucles anidados
letras = ['A','B','C']
numeros =[1,2,3]
for letra in letras:
  for numero in numeros:
    print(f'{letra}{numero}')
#Break
print('Break')
animals = ['loro','leon','tigre','perro','gato']
for indice, animal in enumerate(animals):
  print(animal)
  if animal == 'perro':
    print(f'El {animal} esta escondido en el indice {indice}')
    break

#Continue
print('\nContinue:')
animals = ['loro','leon','tigre','perro','gato']
for indice, animal in enumerate(animals):
  if animal == 'perro':
    continue
  print(animal)

# Comprension de listas (list comprehension)
animals = ['loro','leon','tigre','perro','gato']
animals_mayus = [animal.upper()for animal in animals ]
print(animals_mayus)

# Mustra los numeros pares de una lista
pares =[ num for num in [1,2,3,4,5,6,7,8,9,10] if num % 2 == 0]
print(pares)

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
