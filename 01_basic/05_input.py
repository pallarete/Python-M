# 04 - input()
# Entradad de usuario - Version simplificada
# La funcion input() perimte obtener datos del usuario a traves
#  de la consola
import os
os.system('cls')

# print('Hola como te llamas?')
# nombre = input()
# print(f'Hola {nombre} , encantado de conocerte')
#  Version abreviada
nombre = input('Hola como te llamas?\n')
print(f'Hola {nombre} , encantado de conocerte')

#Todos los inputs son strings, hay que castear
age = input('Cuantos años tienes?\n')
age = int(age)
print(f'Dentro de 20 años tendras { age + 20}')

print('Obtener varios valores a la vez')
country, city = input("'En que pais y ciudad vives?\n").split()

print(f'Vives en {country}, {city}')