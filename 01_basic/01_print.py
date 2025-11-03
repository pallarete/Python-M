# 01 - print()
# El modulo print() es el modulo que nos permite imprimir en consola
# Sireve para mostrar informacion en consola y te va a acompañar
# TODA TU VIDA. Desde hoy hasta el fin de los tiempos
import os
os.system('cls')

print('Hola mundo')
# El modulo print puede recibir  el separador que queramos:
print('Python', 'es','brutal', sep='-')

# Para imprimir en una sola linea dos prints diferentes
# Le decimos que renderize lo que queramos con end =
print('Esto se imprime ', end='')
print('en una linea')
