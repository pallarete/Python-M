"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, 
depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada 
número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números
que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total 
de los huevos que pertenecen a los dinosaurios carnívoros 
(es decir, la suma de todos los números pares en la lista).
"""
import os
os.system('cls')

def huevos_pares(lista)-> int:
  hue_carni =0
  for numero in lista:
    if numero % 2 == 0:
      hue_carni += numero
  return hue_carni

lista = [1,2,3,4,5,6,7,8,9,10]
resultado = huevos_pares(lista)
print(f'El numero total de huevos de dinos carnivoros es: {resultado}')