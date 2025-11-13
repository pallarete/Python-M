# 03 - range()
# Permite crear una secuencia de numeros.Puede ser util para for, pero no solo para eso
import os
os.system('cls')

print('\nRange:')

#genera una secuencia de numeros del 0 al 9
for num in range(10):
  print(num)

#range(inicio, fin)
for num in range(5,10):
  print(num)

#range(inicio, fin,paso)
for num in range(5,10,2):
  print(num)

for num in range(-9,0):
  print(num)

# Cuenta atras
for num in range (10,0,-1):
  print(num)

#Creando listas desde range
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

#Seria para hacer algo cinco veces
for _ in range(5):
  print('Hacer cinco veces algo')

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1: Imprimir números del 1 al 10 ")
for numero in range(1, 11):
  print(numero)


# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2: Imprimir números impares del 1 al 20 ")
for numero in range(1,21):
  if numero %2 != 0:
    print(numero)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3: Imprimir múltiplos de 5")
for numero in range(5,51):
  if numero % 5 ==0:
    print(numero)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4: Imprimir números en orden inverso ")
for numero in range(10, 0, -1):
  print(numero)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5: Suma de números en un rango ")
suma =0
for numero in range(1, 101):
  suma+= numero
print(suma)

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6: Tabla de multiplicar ")
multiplicador = int(input('Introduce un numero: '))
for numero in range(1,11):
  print(f'{multiplicador} * {numero} = { multiplicador * numero}')